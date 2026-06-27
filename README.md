# 👁️ Face Recognition Attendance System

## 🧠 Overview
The **Face Recognition Attendance System** is a Python-based application that uses **face_recognition** (built on dlib's pre-trained ResNet model) to automatically mark attendance based on facial identification.

It captures faces from a live camera feed, compares them with stored face encodings, and records attendance details (name, date, and time) in a **SQLite3 database** — eliminating the need for manual attendance marking.

What sets this apart from most face-recognition attendance tutorials/projects is how it handles the people it *doesn't* recognize. Most basic implementations just label an unrecognized person "Unknown" and move on, losing that moment entirely. This system instead **captures and queues unrecognized faces for later identification**, so no one who showed up gets silently dropped just because they weren't registered yet.

---

## 💡 Features

- 👥 **Multi-Person Detection** — Recognizes and marks attendance for multiple people in a single frame, not just one face at a time.
- 🆕 **Unknown Face Capture & Deferred Naming** — When the system sees a face it doesn't recognize, it automatically saves a snapshot and queues it in a `pending_users` table instead of discarding the moment. Run `assign_pending.py` afterward to review captured faces and assign each one a name, registering them as a recognized user for future sessions.
- 🚫 **Same-Day Duplicate Prevention** — A person is only marked present once per day, even if they walk past the camera repeatedly. Session-level debouncing also prevents the same unrecognized stranger from generating dozens of duplicate snapshots while standing in frame.
- 👤 **Automatic Face Detection & Recognition** — Uses `face_recognition` (dlib-based) for accurate identification.
- 🧾 **Attendance Logging** — Stores date and time for each recognized individual in a SQLite3 database.
- 🗄️ **User Registration System** — Register new users with their facial data and name, either upfront via `register.py` or after the fact via `assign_pending.py`.
- 🧩 **Offline Functionality** — Fully local; no internet connection or cloud service required.
- 📸 **Real-Time Processing** — Detects and identifies faces from a webcam feed in real time.

---

## 🔍 How This Differs From Typical Face Recognition Attendance Tools

Most face-recognition attendance projects follow the same rigid flow: register a person's face up front → recognize them later → if a face isn't recognized, show "Unknown" and discard it. That works fine in a demo, but it breaks down in any real scenario where someone shows up who hasn't been registered yet — a new student joining a class, a guest, a new employee on day one. The system has no memory of that person ever appearing.

This project changes that flow:

| Typical implementation | This system |
|---|---|
| Unknown face → ignored, no record kept | Unknown face → photo captured + timestamped, queued for review |
| Registration must happen *before* recognition | Registration can happen *after the fact*, using the actual moment they were seen |
| Single-face-at-a-time logic in many tutorials | Detects and marks attendance for multiple people in the same frame |
| No safeguard against repeat camera passes | Same-day duplicate prevention, plus per-session debouncing for repeated unknown faces |

In short: nobody who actually showed up in front of the camera is lost from the record, even if they weren't a registered user yet.

---

## 🧩 Tech Stack

| Component | Technology Used |
|------------|-----------------|
| **Programming Language** | Python 3.x |
| **Face Recognition** | `face_recognition` (dlib ResNet-based encodings) |
| **Image Processing** | OpenCV |
| **Database** | SQLite3 |
| **Data Storage** | Local files for face encodings/snapshots, SQLite for attendance + pending records |

---

## 🚀 Usage

1. **Register known users (optional upfront step)**
```bash
   python register.py --name "Jane Doe" --id jane01
```

2. **Run live recognition**
```bash
   python recognize.py
```
   Recognized faces are marked present automatically. Unrecognized faces are captured and queued for review.

3. **Review and name captured unknown faces**
```bash
   python assign_pending.py
```
   Walks through each captured face, lets you assign a name and ID, and registers them for future recognition.

---

## ⚠️ Note
This is a portfolio/learning project. For production use in any setting with real access-control or privacy implications, additional safeguards (liveness/anti-spoofing detection, encrypted storage of face data, consent handling) would be needed.
