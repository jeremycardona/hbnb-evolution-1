#!/usr/bin/python3
"""test user creation validation"""
from models.user import User


# Helper function to validate email format
def is_valid_email(email):
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Test valid user instantiation
try:
    user1 = User.create_user("validuser@example.com", "password123", "John", "Doe")
    assert user1.get_user()["email"] == "validuser@example.com"
    assert is_valid_email(user1.get_user()["email"])
    print("User creation with valid inputs: PASSED")
except Exception as e:
    print("User creation with valid inputs: FAILED")
    print(e)

# Test invalid email format
try:
    user2 = User.create_user("invalidemail", "password123", "Jane", "Doe")
except ValueError as e:
    assert str(e) == "Email already in use" or str(e) == "Invalid email format"
    print("User creation with invalid email format: PASSED")

# Test missing required fields (email)
try:
    user3 = User.create_user(None, "password123", "Jane", "Doe")
except TypeError as e:
    print("User creation with missing email: PASSED")

# Test missing required fields (password)
try:
    user4 = User.create_user("user4@example.com", None, "Jane", "Doe")
except TypeError as e:
    print("User creation with missing password: PASSED")

# Test missing required fields (first name)
try:
    user5 = User.create_user("user5@example.com", "password123", None, "Doe")
except TypeError as e:
    print("User creation with missing first name: PASSED")

# Test missing required fields (last name)
try:
    user6 = User.create_user("user6@example.com", "password123", "Jane", None)
except TypeError as e:
    print("User creation with missing last name: PASSED")

# Test creating a user with an email that already exists
try:
    user7 = User.create_user("validuser@example.com", "password456", "Jack", "Smith")
except ValueError as e:
    assert str(e) == "Email already in use"
    print("User creation with duplicate email: PASSED")
