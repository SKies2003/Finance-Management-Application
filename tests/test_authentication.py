import pytest
from utils.database import DatabaseManager
from services.authenication import UserAuthenticate

@pytest.fixture
def db():
    db = DatabaseManager(":memory:")
    yield db
    db.close()

def test_user_registration_login(db, monkeypatch):
    auth = UserAuthenticate(db)

    inputs = iter(["testuser", "password", "user", 25, "Male", "1234567891", "ABCDE1234F"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    user_id = auth.user_registration()
    assert user_id is not None

    inputs = iter(["testuser", "password"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    login_id = auth.user_login()
    assert login_id == user_id