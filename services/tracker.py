from utils.database import DatabaseManager

class Tracker:
    def __init__(self, db: DatabaseManager):
        self.db = db
    
    def transaction_type(self):
        income_expense = input("Enter type of transaction made (Income/Expense): ").strip().capitalize()
        lst = ["Income", "Expense"]
        while income_expense not in lst:
            print("Invalid transaction type received!")
            income_expense = input("Enter type of transaction made (Income/Expense): ").strip().capitalize()
        return income_expense
    
    def category(self):
        while True:
            try:
                category = input("Enter category (food, salary, fuel, travel, food, profit): ").strip().lower()
                if len(category) == 0:
                    print("category cannot be empty")
                else:
                    break
            except ValueError:
                print("category cannot be empty")
        return category
    
    def amount(self):
        while True:
            try:
                amount = float(input("Enter the amount of transaction made: "))
                break
            except ValueError:
                print("Invalid value found for column amount!")
        return amount
    
    def transaction_id(self):
        while True:
            try:
                transaction_id = int(input("Enter your transaction id: "))
                if transaction_id < 1:
                    print("transaction id must be a postive integer.")
                else:
                    break
            except ValueError:
                print("transaction id must be a postive integer.")
        return transaction_id
    
    def add_transaction(self, user_id: int):
        income_expense = self.transaction_type()
        category = self.category()
        amount = self.amount()
        budget_amount = self.db.get_budget(user_id, category)
        spent_amount = self.db.get_expense(user_id, category)
        if budget_amount is not None and spent_amount is not None:
            remain = budget_amount - (spent_amount + amount)
            if remain >= 0:
                print("You are", remain, "to cross your budget limit.")
            elif remain < 0:
                print("You are", abs(remain), "over the budget limit.")
        print(f"\nYour {income_expense} of {amount} for {category} is saved.")
        return self.db.add_transaction(user_id, income_expense, category, amount)
    
    def display_transactions(self, user_id: int):
        return self.db.display_transactions(user_id)

    def update_transaction(self):
        transaction_id = self.transaction_id()

        while True:
            try:
                choice = int(input("What u want to update \n1. type of transaction \n2. category \n3. amount ? "))
                if choice < 1 or choice > 3:
                    print("Choose from given options.")
                else:
                    break
            except ValueError:
                print("Invalid input! Enter 1, 2 or 3 only.")

        if choice == 1:
            income_expense = self.transaction_type()
            print("Your transaction with id", transaction_id, "has been updated as", income_expense)
            return self.db.update_transaction(transaction_id, "transaction_type", income_expense)
        
        if choice == 2:
            category = self.category()
            print("Your transaction with id", transaction_id, "has been updated as", category)
            return self.db.update_transaction(transaction_id, "category", category)
        
        if choice == 3:
            amount = self.amount()
            print("Amount for your transaction with id", transaction_id, "has been updated to", amount)
            return self.db.update_transaction(transaction_id, "amount", amount)
        
    def delete_transaction(self):
        transaction_id = self.transaction_id()
        print("Your transaction with id", transaction_id, "has been deleted!")
        return self.db.delete_transaction(transaction_id)