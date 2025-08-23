from utils.database import DatabaseManager

class Track:
    def __init__(self, db: DatabaseManager):
        self.db = db
    
    def add_transaction(self, user_id: int):
        income_expense = input("Enter type of transaction made (Income/Expense): ").strip().capitalize()
        lst = ["Income", "Expense"]
        while income_expense not in lst:
            print("Invalid transaction type received!")
            income_expense = input("Enter type of transaction made (Income/Expense): ").strip().capitalize()
        
        category = input("Enter category of transaction made (food, shopping, salary, profit etc.): ").strip().lower()

        while True:
            try:
                amount = float(input("Enter the amount of transaction made: "))
                break
            except ValueError:
                print("Invalid value found for column amount!")
        print(f"\nYour {income_expense} of {amount} for {category} is saved.")
        return self.db.add_transaction(user_id, income_expense, category, amount)