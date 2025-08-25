from utils.database import DatabaseManager
from services.authenication import UserAuthenticate
import sys
from services.tracker import Tracker
from services.reports import Report

if __name__ == "__main__":
    login_status = False
    db = DatabaseManager()
    auth = UserAuthenticate(db)
    track = Tracker(db)
    report = Report(db)

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
            user_action = int(
                input(
                    """
what you want to?
                            
    1. Add a new transaction?
    2. Display all transactions?
    3. Update an existing transaction?
    4. Delete transaction?
    5. Want to see your monthly report?
    6. Want to see your yearly report?
        
Enter a number referencing above actions: """
                )
            )
        except:
            print("Invalid Input!")
            sys.exit()

        if user_action == 1:
            track.add_transaction(user_id) # pyright: ignore[reportPossiblyUnboundVariable]
        elif user_action == 2:
            track.display_transactions(user_id) # pyright: ignore[reportPossiblyUnboundVariable]
        elif user_action == 3:
            track.update_transaction()
        elif user_action == 4:
            track.delete_transaction()
        elif user_action == 5:
            report.monthly_report(user_id) # pyright: ignore[reportPossiblyUnboundVariable]
        elif user_action == 6:
            report.yearly_report(user_id) # pyright: ignore[reportPossiblyUnboundVariable]