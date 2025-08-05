# app/transactions.py
import datetime
from app.database import connect
from app import budget

def add_transaction(user_id):
    t_type = input("Type (income/expense): ").lower()
    category = input("Category (e.g., Food, Salary, Rent): ")
    amount = float(input("Amount: "))
    date = input("Date (YYYY-MM-DD, leave empty for today): ")

    if not date:
        date = str(datetime.date.today())
    
    if t_type == "expense":
        budget.check_budget(user_id, category, amount)

    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO transactions (user_id, type, category, amount, date)
        VALUES (?, ?, ?, ?, ?)''',
        (user_id, t_type, category, amount, date))
    conn.commit()
    conn.close()
    print("✅ Transaction added successfully!")

def view_transactions(user_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        SELECT id, type, category, amount, date
        FROM transactions
        WHERE user_id = ?
        ORDER BY date DESC
    ''', (user_id,))
    records = cur.fetchall()
    conn.close()

    if not records:
        print("No transactions found.")
        return

    print("\n📄 Your Transactions:")
    for row in records:
        print(f"ID: {row[0]} | {row[1].capitalize()} | {row[2]} | ₹{row[3]:.2f} | {row[4]}")

def delete_transaction(user_id):
    view_transactions(user_id)
    t_id = input("Enter ID of transaction to delete: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute('DELETE FROM transactions WHERE id = ? AND user_id = ?', (t_id, user_id))
    conn.commit()
    conn.close()
    print("🗑️ Transaction deleted.")

def update_transaction(user_id):
    view_transactions(user_id)
    t_id = input("Enter ID of transaction to update: ")
    category = input("New Category: ")
    amount = float(input("New Amount: "))
    date = input("New Date (YYYY-MM-DD): ")

    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        UPDATE transactions
        SET category = ?, amount = ?, date = ?
        WHERE id = ? AND user_id = ?
    ''', (category, amount, date, t_id, user_id))
    conn.commit()
    conn.close()
    print("✏️ Transaction updated.")
