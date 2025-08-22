import sqlite3

class DatabaseManager:
    def __init__(self, db_name = "db.sqlite"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS authenticate (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS profile (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                gender TEXT CHECK(gender IN ('Male', 'Female')),
                mobile_number TEXT UNIQUE,
                pan TEXT UNIQUE
            )
            """)

    def sign_up(self, username: str, password: str):
        try:
            self.cursor.execute("INSERT INTO authenticate (username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
            print("User registered successfully!")
            return True
        except sqlite3.IntegrityError:
            print("User with this username already exists!")
            return False

    def create_profile(self, name: str, age: int, gender: str, mobile_number: str, pan: str):
        try:
            self.cursor.execute("INSERT INTO profile (name, age, gender, mobile_number, pan) VALUES (?, ?, ?, ?, ?)", (name, age, gender, mobile_number, pan))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("User with this mobile number/pan already exists!")
            return False
    
    def login(self, username: str, password: str):
        try:
            self.cursor.execute("SELECT password FROM authenticate WHERE username = ?", (username,))
            db_password = self.cursor.fetchone()
            if db_password is not None:
                return db_password[0] == password
        except TypeError:
            return None
    
    def close(self):
        self.cursor.close()
        self.conn.close()