from utils.database import DatabaseManager

class Main:
    def __init__(self):
        self.db = DatabaseManager()
    
    def user_registration(self):
        username = input("Enter a unique username: ")
        password = input("Enter a password: ")
        return self.db.sign_up(username, password)
    
    def create_profile(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        gender = input("Enter Male/Female: ").capitalize()
        mobile_number = input("Enter your 10 digit mobile number: ")
        pan = input("Enter your pan number: ")
        self.db.create_profile(name, age, gender, mobile_number, pan)
    
    def close(self):
        self.db.close()

if __name__ == "__main__":
    app = Main()
    while not app.user_registration():
        print()
    app.create_profile()
    app.close()