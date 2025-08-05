import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sqlite3
import unittest
from app.database import connect

class TestDatabase(unittest.TestCase):

    def test_connection(self):
        conn = connect()
        self.assertIsInstance(conn, sqlite3.Connection)
        conn.close()

    def test_tables_exist(self):
        conn = connect()
        cursor = conn.cursor()
        tables = ['users', 'transactions', 'budgets']
        for table in tables:
            cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'")
            self.assertIsNotNone(cursor.fetchone())
        conn.close()

if __name__ == '__main__':
    unittest.main()
