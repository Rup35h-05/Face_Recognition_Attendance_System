"""
assign_pending.py

Lets you review faces that were captured automatically during recognition
(people the system didn't recognize) and assign them a name + ID, turning
them into a registered user. Run this after a recognition session.

Usage:
    python assign_pending.py
"""

import cv2
from pathlib import Path
from db import init_db, get_pending_faces, remove_pending_face, add_user

FACES_DIR = Path("faces")
FACES_DIR.mkdir(exist_ok=True)

init_db()


def review_pending_faces():
    pending = get_pending_faces()

    if not pending:
        print("[INFO] No pending faces to review.")
        return

    print(f"[INFO] {len(pending)} unrecognized face(s) found.\n")

    for pending_id, img_path, captured_at in pending:
        img = cv2.imread(img_path)
        if img is None:
            print(f"[WARN] Could not load {img_path}, skipping.")
            remove_pending_face(pending_id)
            continue

        cv2.imshow(f"Pending face - captured {captured_at}", img)
        cv2.waitKey(1)

        print(f"Captured at: {captured_at}")
        name = input("  Enter name for this person (or leave blank to skip): ").strip()
        cv2.destroyAllWindows()

        if not name:
            print("  Skipped.\n")
            continue

        user_id = input("  Enter a unique ID for this person: ").strip()
        if not user_id:
            print("  No ID entered, skipping.\n")
            continue

        # Move the snapshot into the main faces folder so it's used for
        # future recognition, then register the user and clear the pending entry.
        new_path = FACES_DIR / f"{user_id}_0.jpg"
        Path(img_path).rename(new_path)

        add_user(name, user_id, str(new_path))
        remove_pending_face(pending_id)
        print(f"  Registered {name} ({user_id}).\n")


if __name__ == "__main__":
    review_pending_faces()
