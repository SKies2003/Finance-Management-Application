import sqlite3
import calendar

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
        );
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
            );
            """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            UNIQUE (user_id, category),
            FOREIGN KEY (user_id) REFERENCES authenticate(id) ON DELETE CASCADE
        );
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
    
    def update_transaction(self, transaction_id:int, column: str, update: str|float) -> None:
        self.cursor.execute(f"UPDATE transactions SET {column} = ? WHERE transaction_id = ?", (update, transaction_id))
        self.conn.commit()
    
    def delete_transaction(self, transaction_id: int) -> None:
        self.cursor.execute("DELETE FROM transactions WHERE transaction_id = ?", (transaction_id,))
        self.conn.commit()
    
    def monthly_report(self, user_id: int, year: int, month: int) -> None:
        sql = """
        SELECT category, SUM(amount) as total 
        FROM transactions
        WHERE user_id = ? AND strftime('%Y', date) = ? AND strftime('%m', date) = ?
        GROUP BY category
        ORDER BY total
        """
        self.cursor.execute(sql, (user_id, str(year), f"{month:02d}"))
        monthly_report = self.cursor.fetchall()
        if len(monthly_report) > 0:
            print("\nMonthly report:")
            print("Categories", "Amount")
            for i in monthly_report:
                print(i[0], "=", i[1])
        
        sql = """
        SELECT transaction_type, SUM(amount) as total
        FROM transactions
        WHERE user_id = ? AND strftime('%Y', date) = ? AND strftime('%m', date) = ?
        GROUP BY transaction_type
        """
        self.cursor.execute(sql, (user_id, str(year), f"{month:02d}"))
        transact = self.cursor.fetchall()
        if len(transact) == 1:
            if transact[0][0] == 'Expense':
                print(f"You overspent {abs(transact[0][1])} this month")
            else:
                print(f"You saved {transact[0][1]} this month")
        elif len(transact) == 2:
            if transact[0][0] == 'Expense':
                print("You saved", transact[1][1]-transact[0][1], "this month")
            else:
                print("You saved", transact[0][1]-transact[1][1], "this month")
        else:
            print("No transaction saved for this month.")
    
    def yearly_report(self, user_id: int, year: int) -> None:
        sql = """
        SELECT strftime('%m', date) as month, transaction_type, SUM(amount) as total
        FROM transactions
        WHERE user_id = ? AND strftime('%Y', date) = ?
        GROUP BY month, transaction_type
        ORDER BY month
        """
        self.cursor.execute(sql, (user_id, str(year)))
        yearly_report = self.cursor.fetchall()
        if len(yearly_report) > 0:
            print("month-by-month totals for whole year: \n")
            savings = 0
            for i in yearly_report:
                print(calendar.month_name[int(i[0])], i[1], "=", i[2])
                if i[1] == 'Expense':
                    savings -= i[2]
                else:
                    savings += i[2]
            if savings >= 0:
                print("You saved", savings, "this year")
            else:
                print("You overspent", abs(savings), "this year")
        else:
            print("No transaction saved for this year.")
    
    def set_budget(self, user_id: int, category: str, amount: float) -> None:
        self.cursor.execute("""
                            INSERT INTO budgets (user_id, category, amount) VALUES
                            (?, ?, ?)
                            ON CONFLICT (user_id, category)
                            DO UPDATE SET amount = excluded.amount""", (user_id, category, amount,))
        self.conn.commit()

    def get_budget(self, user_id: int, category: str):
        self.cursor.execute("SELECT amount FROM budgets WHERE user_id = ? AND category = ?", (user_id, category))
        amount = self.cursor.fetchone()
        if amount is not None:
            return amount[0]
    
    def get_expense(self, user_id: int, category: str):
        self.cursor.execute("SELECT SUM(amount) as total FROM transactions WHERE user_id = ? AND category = ?", (user_id, category))
        total = self.cursor.fetchone()
        if total is not None:
            return total[0]

    def close(self):
        self.cursor.close()
        self.conn.close()