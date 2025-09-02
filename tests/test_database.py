import os
import pytest
from utils.database import DatabaseManager

@pytest.fixture
def db():
    db = DatabaseManager(":memory:") # in-memory DB (Exists in RAM and vanishes once program ends)
    yield db
    db.close()

def test_signup_login(db):
    user_id = db.sign_up("testuser", "password", "test", 25, "Male", "1234567890", "ABCDE1234F")
    assert user_id is not None

    login_id = db.login("testuser", "password")
    assert login_id == user_id

def test_add_display_transactions(db, capsys):
    user_id = db.sign_up("user1", "password1", "test1", 30, "Female", "1234567890", "ABCDE1234F")
    db.add_transaction(user_id, "Income", "salary", 50000)
    db.display_transactions(user_id)
    captured = capsys.readouterr()
    assert "salary" in captured.out

def test_backup_restore(tmp_path):
    db_file = tmp_path / "db.sqlite"
    db = DatabaseManager(str(db_file))
    user_id = db.sign_up("user2", "password2", "test2", 45, "Male", "1234567890", "ABCDE1234F")
    db.backup(str(tmp_path / "backup.sqlite"))
    db.close()

    # restore into new instance
    db2 = DatabaseManager(str(db_file))
    assert db2.restore(str(tmp_path / "backup.sqlite"))
    login_id = db2.login("user2", "password2")
    assert login_id is not None
    db2.close()