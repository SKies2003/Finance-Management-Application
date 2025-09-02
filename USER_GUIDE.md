# Running the Application

Start the program:

```terminal
python main.py
```

You'll be asked:

```terminal
Signup or Login:
```

## SignUp

1. **USERNAME & PASSWORD:** Must be atleast 6 characters (Remember username and password, you need it everytime.)
2. **NAME:** Must be greater atleast 3 characters
3. **AGE:** Must be an numeric value
4. **GENDER:** Must be one out of **Male** or **Female**
5. **MOBILE NO.:** Must be 10 numeric values
6. **PAN NO.:** Must be of 10 character length in CAPITAL or UPPERCASE (eg. XXXXX1234X)

## Login

Use existing username & password

## Menu Options

After successful signup or login, you’ll see:

1. **Add a transaction** → Record income/expense with category and amount.
2. **Display transactions** → View all your transactions with IDs.
3. **Update transaction** → Modify type, category, or amount of a transaction.
4. **Delete transaction** → Remove a transaction by ID.
5. **Monthly report** → View category totals and savings/overspending for a month.
6. **Yearly report** → View month-by-month totals and overall yearly savings.
7. **Set budget** → Define or update budget for a category.
8. **Backup** → Save db.sqlite into backup.sqlite.
9. **Restore** → Replace db.sqlite with backup.sqlite.

> Press any other key to quit the program.

### Database

Each user’s data is isolated by login

- Default file: **db.sqlite**
- Backup file: **backup.sqlite**

#### Backup & Restore

1. Option 8 → Create backup (**backup.sqlite**)
2. Option 9 → Restore from backup

⚠️ Restoring will overwrite your database. Always back up before restoring.

### Running Tests

To run all unit tests:

```terminal
python -m pytest -v
```

- Tests are located in the test/ folder.
- They use an in-memory SQLite database (:memory:), so your real data stays safe.

### Best Practices

- Use consistent category names (food, salary, travel, etc.)
- Regularly backup your database.
- Set budgets early to track overspending.

#### Example Walkthrough

```terminal
SignUp or Login: signup
Enter a unique username: testuser
Enter a password: password
Enter your name: John
Enter your age: 28
Enter Male/Female: Male
Enter your contact number: 9876543210
Enter your 10 digit PAN Number: ABCDE1234F

User registered successfully!

what you want to?

1. Add a new transaction
2. Display all transactions
...
```
