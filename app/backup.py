# app/backup.py
import sqlite3
import shutil
import os
from datetime import datetime

DB_PATH = "db/finance.db"
BACKUP_DIR = "backups"

def backup_database():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_DIR, f"backup_{timestamp}.db")
    shutil.copy(DB_PATH, backup_file)
    print(f"✅ Backup created: {backup_file}")

def restore_database(backup_file):
    if not os.path.exists(backup_file):
        print("❌ Backup file does not exist.")
        return
    
    shutil.copy(backup_file, DB_PATH)
    print(f"✅ Database restored from: {backup_file}")
