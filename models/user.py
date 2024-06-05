#!/usr/bin/python3
""" Module for user class"""
from datetime import datetime


class User():
    """Methods for User"""
    count = 0
    __users_by_email = {}
    def __init__(self, email=None, password=None, firstname=None, lastname=None):
        self.__email = email
        self.__password = password
        self.firstname = firstname
        self.lastname = lastname
        self.__created_at = datetime.now()
        self.__updated_at = datetime.now()
        self.places = []  # List to hold places hosted by the user
        User.__users_by_email[email] = self
        User.count += 1

    def create_user(self, email, password, firstname, lastname):
        if email in User.__users_by_email:
            raise ValueError("Email already in use")
        self.__email = email
        self.__password = password
        self.firstname = firstname
        self.lastname = lastname
        self.__updated_at = datetime.now()
        User.__users_by_email[email] = self
    def update_user(self, email, password, firstname, lastname):
        if email != self.email and email in User.users_by_email:
            raise ValueError("Email already in use")
        del User.users_by_email[self.email]
        self.email = email
        self.__email = email
        self.__password = password
        self.firstname = firstname
        self.lastname = lastname
        self.__updated_at = datetime.now()
        User.__users_by_email[email] = self
    def get_user(self):
        if (self.firstname and self.lastname):
            return self.firstname + " " + self.lastname
        else:
            return None
    def delete_user(self):
        del self
        User.count -= 1
    def add_place(self, place):
        self.places.append(place)
    def remove_place(self, place):
        self.places.remove(place)
    def get_user_email(self):
        return self.__email
    @classmethod
    def get_emails(cls):
        return cls.__users_by_email.keys()


try:
    host = User("example@example.com", "abc123", "John", "Smith")
    print(host.get_user_email())

    jeremy = User()
    jeremy.create_user("new@example.com", "def456", "Jeremy", "Smith")
    print(jeremy.get_user_email())
    # This will raise a ValueError
    jeremy.create_user("example@example.com", "ghi789", "Jeremy", "Smith")
    print(jeremy.get_user_email())

    print(User.get_emails())

except ValueError as e:
    print(e)