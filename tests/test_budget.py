import pytest
from utils.database import DatabaseManager
from services.budget import Budget

@pytest.fixture
def db():
    db = DatabaseManager(":memory:")
    yield db
    db.close()

def test_set_budget(db, monkeypatch):
    user_id = db.sign_up("testuser", "testpassword", "testuser", 25, "Female", "1234567890", "ASDFG1234A")

    budget = Budget(db)

    inputs = iter(["shopping", 2500])
    monkeypatch.setattr("builtins.input", lambda _:next(inputs))

    budget.set_budget(user_id)
    saved = db.get_budget(user_id, "shopping")
    assert saved == 2500