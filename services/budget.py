from utils.database import DatabaseManager

class Budget:
    def __init__(self, db: DatabaseManager):
        self.db = db
    
    def set_budget(self, user_id: int):
        while True:
            try:
                category = input("Enter category you want to set budget for: ").strip().lower()
                if len(category) == 0:
                    print("category cannot be empty")
                else:
                    break
            except ValueError:
                print("category cannot be empty")
        while True:
            try:
                amount = float(input("Set budget amount: "))
                break
            except ValueError:
                print("Invalid Input! Enter a number.")
        return self.db.set_budget(user_id, category, amount)