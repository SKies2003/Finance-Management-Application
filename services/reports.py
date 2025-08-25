from utils.database import DatabaseManager
from datetime import datetime

class Report:
    def __init__(self, db: DatabaseManager):
        self.db = db
    
    def year_check(self):
        while True:
            try:
                self.year = int(input("Enter year: "))
                self.max_year = datetime.now().year
                if 2015 <= self.year <= self.max_year:
                    break
                else:
                    print("Year cannot be before 2015 and after", self.max_year)
            except ValueError:
                print("Invalid input! Please enter a number.")
        return self.year
    
    def month_check(self, year: int):
        while True:
            try:
                self.month = int(input("Enter month in numbers: "))
                max_year = datetime.now().year
                max_month = datetime.now().month
                if year == max_year and 1 <= self.month <= max_month:
                    break
                elif year < max_year and 1 <= self.month <= 12:
                    break
                else:
                    print("Month cannot be 0 or less and greater than", max_month)
            except ValueError:
                print("Invalid input! Please enter a number.")
        return self.month
    
    def monthly_report(self, user_id: int):
        year = self.year_check()
        month = self.month_check(year)
        return self.db.monthly_report(user_id, year, month)
    
    def yearly_report(self, user_id: int):
        year = self.year_check()
        return self.db.yearly_report(user_id, year)