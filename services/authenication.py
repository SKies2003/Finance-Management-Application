from utils.database import DatabaseManager

class UserAuthenticate():
    def __init__(self, db: DatabaseManager):
        self.db = db
    
    def user_registration(self):
        username = input("Enter a unique username: ").strip()
        while len(username) < 6:
            print("Invalid username! Must be greater than 5 characters.\n")
            username = input("Enter a unique username: ").strip()
        
        password = input("Enter a password: ").strip()
        while len(password) < 6:
            print("Invalid password! Must be greater than 5 characters.\n")
            password = input("Enter a password: ").strip()
        
        return self.db.sign_up(username, password)
    
    def user_login(self):
        username = input("Enter a unique username: ").strip()
        while len(username) < 6:
            print("Invalid username! Must be greater than 5 characters.\n")
            username = input("Enter a unique username: ").strip()
        
        password = input("Enter a password: ").strip()
        while len(password) < 6:
            print("Invalid password! Must be greater than 5 characters.\n")
            password = input("Enter a password: ").strip()
        
        return self.db.login(username, password)