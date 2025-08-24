from utils.database import DatabaseManager
from services.authenication import UserAuthenticate
import sys
from services.tracker import Tracker

if __name__ == "__main__":
    login_status = False
    db = DatabaseManager()
    auth = UserAuthenticate(db)
    track = Tracker(db)

    choice = input("SignUp or Login: ").lower().strip()
    print()
    if choice == "signup":
        user_id = auth.user_registration()
        while user_id is None:
            print()
            user_id = auth.user_registration()
        login_status = True

    elif choice == "login":
        user_id = auth.user_login()
        while user_id is None:
            print()
            user_id = auth.user_login()
        login_status = True

    if login_status:
        try:
            user_action = int(input("""
what you want to?
                            
    1. Add a new transaction?
    2. Display all transactions?
    3. Update an existing transaction?
    4. Delete transaction?
        
Enter a number referencing above actions: """))
        except:
            print("Invalid Input!")
            sys.exit()
    
        if user_action == 1:
            track.add_transaction(user_id)
        elif user_action == 2:
            track.display_transactions(user_id)
        elif user_action == 3:
            track.update_transaction()
        elif user_action == 4:
            track.delete_transaction()
