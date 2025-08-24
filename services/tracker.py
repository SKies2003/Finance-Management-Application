from utils.database import DatabaseManager

class Tracker:
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
    
    def display_transactions(self, user_id: int):
        return self.db.display_transactions(user_id)

    def update_transaction(self):
        transaction_id = int(input("Enter your transaction id: "))
        choice = int(input("What u want to update \n1. type of transaction \n2. category \n3. amount ? "))
        if choice == 1:
            income_expense = input("Enter type of transaction made (Income/Expense): ").strip().capitalize()
            lst = ["Income", "Expense"]
            while income_expense not in lst:
                print("Invalid transaction type received!")
                income_expense = input("Enter type of transaction made (Income/Expense): ").strip().capitalize()
            print("Your transaction with id", transaction_id, "has been updated as", income_expense)
            return self.db.update_transaction(transaction_id, "transaction_type", income_expense)
        
        if choice == 2:
            category = input("Enter category of transaction made (food, shopping, salary, profit etc.): ").strip().lower()
            print("Your transaction with id", transaction_id, "has been updated as", category)
            return self.db.update_transaction(transaction_id, "category", category)
        
        if choice == 3:
            while True:
                try:
                    amount = float(input("Enter the amount of transaction made: "))
                    break
                except ValueError:
                    print("Invalid value found for column amount!")
            print("Amount for your transaction with id", transaction_id, "has been updated to", amount)
            return self.db.update_transaction(transaction_id, "amount", amount)
        
    def delete_transaction(self):
        transaction_id = int(input("Enter your transaction id: "))
        print("Your transaction with id", transaction_id, "has been deleted!")
        return self.db.delete_transaction(transaction_id)