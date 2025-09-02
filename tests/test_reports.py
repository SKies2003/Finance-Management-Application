import pytest
from utils.database import DatabaseManager
from services.reports import Report

@pytest.fixture
def db():
    db = DatabaseManager(":memory:")
    yield db
    db.close()

def test_monthly_yearly_report(db, monkeypatch, capsys):
    user_id = db.sign_up("username", "password", "user", 20, "Male", "9874563210", "QWERT1234Q")
    db.add_transaction(user_id, "Income", "profit", 54000)

    report = Report(db)

    # mock year and month input
    monkeypatch.setattr("builtins.input", lambda _: "1")
    month = report.month_check(2025)
    assert month == 1

    db.monthly_report(user_id, 2025, 1)
    db.yearly_report(user_id, 2025)