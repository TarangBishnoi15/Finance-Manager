# app/budget.py
import datetime
from app.database import connect

def set_budget(user_id):
    category = input("Enter category to set budget for: ").strip().lower()
    amount = float(input("Enter monthly budget amount: ₹"))
    
    today = datetime.date.today()
    year = today.year
    month = today.month

    conn = connect()
    cursor = conn.cursor()

    # Check if a budget already exists
    cursor.execute('''
        SELECT id FROM budgets
        WHERE user_id = ? AND category = ? AND year = ? AND month = ?
    ''', (user_id, category, year, month))
    result = cursor.fetchone()

    if result:
        cursor.execute('''
            UPDATE budgets SET amount = ?
            WHERE id = ?
        ''', (amount, result[0]))
        print(f"📝 Budget updated for '{category}' to ₹{amount:.2f}.")
    else:
        cursor.execute('''
            INSERT INTO budgets (user_id, category, amount, year, month)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, category, amount, year, month))
        print(f"✅ Budget set for '{category}' to ₹{amount:.2f}.")

    conn.commit()
    conn.close()

def check_budget(user_id, category, new_expense_amount):
    today = datetime.date.today()
    year = today.year
    month = today.month

    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT amount FROM budgets
        WHERE user_id = ? AND category = ? AND year = ? AND month = ?
    ''', (user_id, category.lower(), year, month))
    budget = cursor.fetchone()

    if budget:
        budget_limit = budget[0]

        # Calculate current spending
        cursor.execute('''
            SELECT SUM(amount) FROM transactions
            WHERE user_id = ? AND category = ? AND type = 'expense'
            AND strftime('%Y', date) = ? AND strftime('%m', date) = ?
        ''', (user_id, category.lower(), str(year), str(month).zfill(2)))
        total_spent = cursor.fetchone()[0] or 0

        if total_spent + new_expense_amount > budget_limit:
            print("⚠️ Warning: This expense exceeds your monthly budget for this category!")

    conn.close()
