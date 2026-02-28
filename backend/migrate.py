import sqlite3
import os

db_path = r'/Users/karthik/Desktop/Style-Ai-main-3/backend/data/app.db'
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    try:
        conn.execute("ALTER TABLE users ADD COLUMN gender TEXT")
        print("Successfully added gender column to users.")
    except Exception as e:
        print(f"Migration error or already updated: {e}")
    conn.commit()
    conn.close()
