from app.database import connect

def generate_report(user_id):
    print("\n📅 Report Options:")
    print("1. Monthly Report")
    print("2. Yearly Report")
    choice = input("Choose report type: ")

    if choice == '1':
        month = input("Enter month (MM): ")
        year = input("Enter year (YYYY): ")
        date_filter = f"{year}-{month.zfill(2)}"
    elif choice == '2':
        year = input("Enter year (YYYY): ")
        date_filter = f"{year}"
    else:
        print("❌ Invalid choice.")
        return

    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        SELECT type, SUM(amount)
        FROM transactions
        WHERE user_id = ? AND date LIKE ?
        GROUP BY type
    ''', (user_id, f"{date_filter}%"))

    rows = cur.fetchall()
    conn.close()

    income = expense = 0
    for row in rows:
        if row[0] == 'income':
            income = row[1]
        elif row[0] == 'expense':
            expense = row[1]

    print(f"\n📊 Financial Report for {date_filter}")
    print(f"Total Income  : ₹{income:.2f}")
    print(f"Total Expenses: ₹{expense:.2f}")
    print(f"Savings       : ₹{income - expense:.2f}")
