import sqlite3

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
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                transaction_type TEXT CHECK(transaction_type IN ('Income', 'Expense')),
                category TEXT,
                amount REAL NOT NULL,
                date TEXT DEFAULT (DATE('now')),
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
    
    def display_transactions(self, user_id: int):
        self.cursor.execute("SELECT transaction_id, transaction_type, category, amount, date FROM transactions WHERE user_id = ?", (user_id, ))
        all_transactions = self.cursor.fetchall()
        print("\nYour all transactions:\nPlease note the transaction id if you want to update it's content\n")
        for i in all_transactions:
            print("Transaction id:", i[0])
            print(i[1], "category:", i[2])
            print("Amount:", i[3])
            print("Transaction added on", i[4])
            print()
    
    def update_transaction(self, transaction_id:int, column: str, update: str|float):
        self.cursor.execute(f"UPDATE transactions SET {column} = ? WHERE transaction_id = ?", (update, transaction_id))
        self.conn.commit()
    
    def delete_transaction(self, transaction_id: int):
        self.cursor.execute("DELETE FROM transactions WHERE transaction_id = ?", (transaction_id,))
        self.conn.commit()
    
    def reporting
    
    def close(self):
        self.cursor.close()
        self.conn.close()