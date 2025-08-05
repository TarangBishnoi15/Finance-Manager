from getpass import getpass
from app.database import connect

def register():
    conn = connect()
    cur = conn.cursor()
    username = input("Choose a username: ")
    password = getpass("Choose a password: ")

    try:
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("✅ Registration successful!")
    except Exception as e:
        print("❌ Registration failed:", e)
    finally:
        conn.close()

def login():
    conn = connect()
    cur = conn.cursor()
    username = input("Username: ")
    password = getpass("Password: ")
    cur.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
    user = cur.fetchone()
    conn.close()

    if user:
        print("✅ Login successful!")
        return user[0]
    else:
        print("❌ Invalid credentials.")
        return None
