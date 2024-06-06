import pytest
from models.user import User

def test_update_user():
    # Create a user
    user = User.create_user("original@example.com", "password123", "John", "Doe")
    
    # Verify initial state
    user_info = user.get_user()
    assert user_info["email"] == "original@example.com"
    assert user_info["firstname"] == "John"
    assert user_info["lastname"] == "Doe"
    
    # Update user's attributes
    user.update_user("updated@example.com", "newpassword", "Jane", "Smith")
    
    # Verify updated state
    updated_user_info = user.get_user()
    assert updated_user_info["email"] == "updated@example.com"
    assert updated_user_info["firstname"] == "Jane"
    assert updated_user_info["lastname"] == "Smith"
    assert updated_user_info["password"] == "newpassword"
    
    # Verify that email uniqueness is enforced
    try:
        User.create_user("updated@example.com", "anotherpassword", "Another", "User")
    except ValueError as e:
        assert str(e) == "Email already in use"

if __name__ == "__main__":
    pytest.main()
