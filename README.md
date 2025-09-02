<h1 align = "center">Personal Finance Tracker</h1>

<p align = "center"><b>A simple command-line finance manager built with Python and SQLite.<br>
This app helps you record income/expenses, set budgets, and generate financial reports — all stored locally and safely.</b></p>

### Features

- **User authentication:** Sign up and Login
- **Transactions:** add, view, update, delete
- **Reports:** monthly & yearly summaries
- **Budgets:** set spending limits per category
- **Backup & Restore:** keep your data safe
- **Unit tests included (using pytest)**

### Installation

Requires: **Python 3.8+**

```bash
# Clone repository
git clone https://github.com/SKies2003/Finance-Management-Application.git
cd Finance-Management-Application

# Install test dependency (for developers)
pip install pytest
```

### Usage

**Run the app:**

```terminal
python main.py
```

**Choose to SignUp or Login, then follow the menu:**

```terminal
1. Add a new transaction
2. Display all transactions
3. Update an existing transaction
4. Delete transaction
5. See monthly report
6. See yearly report
7. Set a monthly budget
8. Backup database
9. Restore database
```

### Example

```terminal
Signup or Login: signup
Enter a unique username: testuser
Enter a password: password
Enter your name: John
Enter your age: 28
Enter Male/Female: Male
Enter your contact number: 9876543210
Enter your 10 digit PAN Number: ABCDE1234F

User registered successfully!
```

## Documentation

Full instructions are available in the [User guide](USER_GUIDE.md)

### Project Structure

```bash
project_root/
│── main.py                  # Main entry point
│── utils/
│   └── database.py          # Database manager (SQLite)
│── services/
│   ├── authenication.py     # User registration & login
│   ├── tracker.py           # Transactions
│   ├── reports.py           # Reports
│   └── budget.py            # Budgets
│── test/                    # Unit tests
│   ├── test_database.py
│   ├── test_authentication.py
│   ├── test_tracker.py
│   ├── test_reports.py
│   └── test_budget.py
│── USER_GUIDE.md       # Full manual
```
