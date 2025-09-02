import pytest
from utils.database import DatabaseManager
from services.tracker import Tracker

@pytest.fixture
def db():
    db = DatabaseManager(":memory:")
    yield db
    db.close()

def test_add_transaction(monkeypatch, db, capsys):
    user_id = db.sign_up("testuser", "password", "user", 22, "Female", "1234567890", "ABCDE1234F")
    tracker = Tracker(db)

    inputs = iter(["Income", "salary", "90000"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    tracker.add_transaction(user_id)
    captured = capsys.readouterr()
    assert "saved" in captured.out