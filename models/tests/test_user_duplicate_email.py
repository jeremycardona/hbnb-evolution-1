# test_user_duplicate_email.py

from models.user import User

# Test creating multiple users with the same email
def test_duplicate_email():
    # Create the first user
    try:
        user1 = User.create_user("duplicate@example.com", "password123", "John", "Doe")
        assert user1.get_user()["email"] == "duplicate@example.com"
        print("First user creation with duplicate email: PASSED")
    except Exception as e:
        print("First user creation with duplicate email: FAILED")
        print(e)

    # Attempt to create a second user with the same email
    try:
        user2 = User.create_user("duplicate@example.com", "password456", "Jane", "Smith")
        print("Second user creation with duplicate email: FAILED")
    except ValueError as e:
        assert str(e) == "Email already in use"
        print("Second user creation with duplicate email: PASSED")
    except Exception as e:
        print("Second user creation with duplicate email: FAILED")
        print(e)

if __name__ == "__main__":
    test_duplicate_email()
