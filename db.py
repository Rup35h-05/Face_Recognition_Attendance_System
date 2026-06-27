import sqlite3

DB_PATH = "attendance.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    # Create users table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            img_path TEXT NOT NULL
        )
    """)
    # Create attendance table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            date TEXT,
            time TEXT,
            status TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)
    # Create pending_users table for unrecognized faces awaiting a name
    cur.execute("""
        CREATE TABLE IF NOT EXISTS pending_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            img_path TEXT NOT NULL,
            captured_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    print("[INFO] Database initialized.")

def add_user(name, user_id, img_path):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO users (id, name, img_path) VALUES (?, ?, ?)",
                (user_id, name, img_path))
    conn.commit()
    conn.close()
    print(f"[INFO] Added user: {name} ({user_id})")

def add_pending_face(img_path, captured_at):
    """Save a snapshot of an unrecognized face to review/name later."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO pending_users (img_path, captured_at) VALUES (?, ?)",
                (img_path, captured_at))
    conn.commit()
    conn.close()
    print(f"[INFO] New unrecognized face saved: {img_path}")

def get_pending_faces():
    """Return all unrecognized faces still waiting to be named."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, img_path, captured_at FROM pending_users ORDER BY captured_at")
    rows = cur.fetchall()
    conn.close()
    return rows

def remove_pending_face(pending_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DELETE FROM pending_users WHERE id=?", (pending_id,))
    conn.commit()
    conn.close()

# Only one __main__ block
if __name__ == "__main__":
    init_db()
