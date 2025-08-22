from utils.database import DatabaseManager
from services.authenication import UserAuthenticate
from services.profile import UserProfile

if __name__ == "__main__":
    db = DatabaseManager()
    auth = UserAuthenticate(db)
    profile = UserProfile(db)

    choice = input("SignUp or Login: ").lower().strip()
    print()
    if choice == "login":
        login_status = auth.user_login()
        if login_status:
            print("Welcome Back!\n")
        elif login_status is False:
            print("Invalid password!\n")
        else:
            print("User not found!\n")
    
    elif choice == "signup":
        while not auth.user_registration():
            print()
        print()
        while not profile.profile_details():
            print()
        print("Profile setup completed!")