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
        
        name = input("Enter your name: ").strip()
        while len(name) < 3:
            print("Name must contain more than 2 characters.\n")
            name = input("Enter your name: ").strip()

        while True:
            try:
                age = int(input("Enter your age: "))
                break
            except ValueError:
                print("Age must be numbers not characters!\n")

        gender = input("Enter Male/Female: ").capitalize()
        while gender not in ["Male", "Female"]:
            print("Invalid gender! Please enter Male or Female.\n")
            gender = input("Enter Male/Female: ").capitalize()
        
        mobile_no = input("Enter your contact number: ")
        while not (mobile_no.isdigit() and len(mobile_no) == 10):
            print("Invalid contact number! Must be 10 digts.\n")
            mobile_no = input("Enter your contact number: ")
        
        pan = input("Enter your 10 digit PAN Number: ")
        while not (len(pan) == 10 and pan[:5].isupper() and pan[6:9].isdigit() and pan[-1].isupper()):
            print("Invalid PAN id provided! Please enter correct PAN ID.\n")
            pan = input("Enter your 10 digit PAN Number: ")
        
        return self.db.sign_up(username, password, name, age, gender, mobile_no, pan)
    
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