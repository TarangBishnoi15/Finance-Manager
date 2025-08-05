import sqlite3

def connect():
    return sqlite3.connect("db/finance.db")

def setup_database():
    conn = connect()
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        type TEXT CHECK(type IN ('income', 'expense')),
        category TEXT,
        amount REAL,
        date TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS budgets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        category TEXT,
        amount REAL,
        month TEXT,
        year TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )''')

    conn.commit()
    conn.close()
