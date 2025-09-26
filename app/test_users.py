from users import get_users

def test_users():
    users = get_users()
    assert isinstance(users,list)
    assert len(users) >= 15
