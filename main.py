# main.py
from app import database, auth, transactions, reports, budget, backup

def main_menu(user_id):
    while True:
        print("\n🔸 Main Menu")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. View Financial Report")
        print("6. Set Budget")
        print("7. Backup Database")
        print("8. Restore Database")
        print("9. Logout")
        choice = input("Select an option: ")

        if choice == '1':
            transactions.add_transaction(user_id)
        elif choice == '2':
            transactions.view_transactions(user_id)
        elif choice == '3':
            transactions.update_transaction(user_id)
        elif choice == '4':
            transactions.delete_transaction(user_id)
        elif choice == '5':
            reports.generate_report(user_id)
        elif choice == '6':
            budget.set_budget(user_id)
        elif choice == '7':
            backup.backup_database()
        elif choice == '8':
            file = input("Enter backup file path (e.g., backups/backup_YYYYMMDD_HHMMSS.db): ")
            backup.restore_database(file)
        elif choice == '9':
            print("👋 Logged out.")
            break
        else:
            print("❌ Invalid choice.")

def main():
    database.setup_database()
    print("📊 Personal Finance Manager")
    print("1. Register")
    print("2. Login")
    choice = input("Choose an option: ")

    user_id = None
    if choice == '1':
        auth.register()
    elif choice == '2':
        user_id = auth.login()

    if user_id:
        main_menu(user_id)

if __name__ == "__main__":
    main()
