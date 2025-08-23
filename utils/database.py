import sqlite3
from typing import Optional

class DatabaseManager:
    def __init__(self, db_name = "db.sqlite"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS authenticate (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            name TEXT,
            age INTEGER,
            gender TEXT CHECK(gender IN ('Male', 'Female')),
            contact_no TEXT UNIQUE,
            pan TEXT unique
        )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                transaction_type TEXT CHECK(transaction_type IN ('Income', 'Expense')),
                category TEXT,
                amount REAL,
                date TEXT DEFAULT CURRENT_DATE,
                FOREIGN KEY (user_id) REFERENCES authenticate(id) ON DELETE CASCADE
            )
            """)

    def sign_up(self, username: str, password: str, name: str, age: int, gender: str, contact_no: str, pan: str):
        try:
            self.cursor.execute("INSERT INTO authenticate (username, password, name, age, gender, contact_no, pan) VALUES (?, ?, ?, ?, ?, ?, ?)", (username, password, name, age, gender, contact_no, pan))
            self.conn.commit()
            user_id = self.cursor.lastrowid
            print("User registered successfully!")
            return user_id
        except sqlite3.IntegrityError:
            print("User with this username already exists!")
            return None
    
    def login(self, username: str, password: str):
        try:
            self.cursor.execute("SELECT password FROM authenticate WHERE username = ?", (username,))
            db_password = self.cursor.fetchone()
            if db_password[0] == password:
                self.cursor.execute("SELECT id FROM authenticate WHERE username = ?", (username,))
                user_id = self.cursor.fetchone()
                return user_id[0]
            else:
                print("Invalid password!")
        except:
            print("user not found!")
            return None

    def add_transaction(self, user_id: int, transaction_type: str, category: str, amount: float):
        self.cursor.execute("INSERT INTO transactions (user_id, transaction_type, category, amount) VALUES (?, ?, ?, ?)", (user_id, transaction_type, category, amount))
        self.conn.commit()
        return True
    
    def close(self):
        self.cursor.close()
        self.conn.close()