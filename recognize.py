import cv2
import face_recognition
import sqlite3
import numpy as np
from pathlib import Path
from datetime import datetime, date
from db import init_db, add_pending_face

DB_PATH = "attendance.db"
UNKNOWN_DIR = Path("unknown_faces")
UNKNOWN_DIR.mkdir(exist_ok=True)
init_db()

# Load all registered faces
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute("SELECT id, name, img_path FROM users")
users = cur.fetchall()
conn.close()

known_encodings = []
known_ids = []
known_names = []

for user_id, name, img_path in users:
    img = face_recognition.load_image_file(img_path)
    encs = face_recognition.face_encodings(img)
    if len(encs) > 0:
        known_encodings.append(encs[0])
        known_ids.append(user_id)
        known_names.append(name)

# Start webcam
cam = cv2.VideoCapture(0)
print("[INFO] Starting face recognition. Press Q to quit.")

def mark_attendance(user_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    today = date.today().isoformat()
    cur.execute("SELECT * FROM attendance WHERE user_id=? AND date=?", (user_id, today))
    if cur.fetchone() is None:
        now = datetime.now().strftime("%H:%M:%S")
        cur.execute("INSERT INTO attendance (user_id, date, time, status) VALUES (?, ?, ?, ?)",
                    (user_id, today, now, "Present"))
        conn.commit()
        print(f"[INFO] Marked {user_id} present at {now}")
    conn.close()

# Encodings of unknown faces already captured this session, so the same
# stranger doesn't get a new snapshot saved on every single frame.
captured_unknown_encodings = []

def already_captured(encoding, tolerance=0.5):
    if not captured_unknown_encodings:
        return False
    distances = face_recognition.face_distance(captured_unknown_encodings, encoding)
    return bool(np.any(distances <= tolerance))

def capture_unknown_face(frame, top, right, bottom, left, encoding):
    face_img = frame[top:bottom, left:right]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    img_path = UNKNOWN_DIR / f"unknown_{timestamp}.jpg"
    cv2.imwrite(str(img_path), face_img)
    add_pending_face(str(img_path), datetime.now().isoformat())
    captured_unknown_encodings.append(encoding)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, boxes)

    for (top, right, bottom, left), encoding in zip(boxes, encodings):
        matches = face_recognition.compare_faces(known_encodings, encoding)
        name = "Unknown"
        user_id = None
        if True in matches:
            match_idx = np.where(matches)[0][0]
            name = known_names[match_idx]
            user_id = known_ids[match_idx]
            mark_attendance(user_id)
        elif not already_captured(encoding):
            capture_unknown_face(frame, top, right, bottom, left, encoding)

        # Draw rectangle
        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, name, (left, top-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    cv2.imshow("Face Recognition Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
