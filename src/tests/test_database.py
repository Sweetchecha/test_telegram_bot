from database import save_user, log_message, Session

def test_save_user():
    save_user(12345, "Test User", "testuser")
    session = Session()
    user = session.query(User).filter_by(telegram_id=12345).first()
    assert user is not None
    assert user.first_name == "Test User"
    session.close()
