#!/usr/bin/python3
"""Main application entry point"""

from models.user import User
from models.places import Places
from persistence.data_manager import DataManager

def main():
    # Initialize DataManager
    data_manager = DataManager()

    # Create a new user
    user1 = User.create("test1@example.com", "password1", "Jeremy", "Cardona")
    user2 = User.create("test2@example.com", "pass", "Will", "Pepe")
    # Save user1 using DataManager
    data_manager.save(user1)
    data_manager.save(user2)
    # Retrieve user by ID
    retrieved_user = data_manager.get(user1.get()['id'], 'User')
    print("Retrieved User:", retrieved_user)
    
    # Update user1
    user1.update("new_email@example.com", "newpassword", "Updated", "User1")
    data_manager.update(user1)

    # Retrieve updated user
    updated_user = data_manager.get(user1.get()['id'], 'User')
    print("Updated User:", updated_user)

    
    # Delete user1
    deleted_user = data_manager.get(user1.get()['id'], 'User')
    data_manager.delete(user1.get()['id'], 'User')

    # Confirm deletion
    
    print("Deleted User:", deleted_user)

if __name__ == "__main__":
    main()
