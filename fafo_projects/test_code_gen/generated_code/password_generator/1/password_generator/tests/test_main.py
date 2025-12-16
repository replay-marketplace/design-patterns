import main

def test_generate_password():
    password = main.generate_password(10)
    assert len(password) == 10, 'Password length should be 10.'