#!/usr/bin/python3
""" Module for user class"""
from datetime import datetime
import uuid

class User():
    """Methods for User"""
    count = 0
    __users_by_email = {}

    def __init__(self, email=None, password=None, firstname=None, lastname=None):
        self.__userid = uuid.uuid4()  # Generate a random UUID for user id
        self.__email = email
        self.__password = password
        self.firstname = firstname
        self.lastname = lastname
        self.__created_at = datetime.now()
        self.__updated_at = datetime.now()
        self.places = []  # List to hold places hosted by the user
        if email:
            User.__users_by_email[email] = self
            User.count += 1

    @classmethod
    def create(cls, email, password, firstname, lastname):
        if email in cls.__users_by_email:
            raise ValueError("Email already in use")
        new_user = cls(email, password, firstname, lastname)
        return new_user

    def update(self, email, password, firstname, lastname):
        if email != self.__email and email in User.__users_by_email:
            raise ValueError("Email already in use")
        del User.__users_by_email[self.__email]
        self.__email = email
        self.__password = password
        self.firstname = firstname
        self.lastname = lastname
        self.__updated_at = datetime.now()
        User.__users_by_email[email] = self

    def get(self):
        created_at_str = self.__created_at.strftime("%Y-%m-%d %H:%M:%S:%f")
        updated_at_str = self.__updated_at.strftime("%Y-%m-%d %H:%M:%S:%f")
        return {
            "id": str(self.__userid),  # Convert UUID to string for JSON serialization
            "email": self.__email,
            "password": self.__password,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "created_at": created_at_str,
            "updated_at": updated_at_str
        }
   
    def delete(self):
        del self
        User.count -= 1

    def add_place(self, place):
        self.places.append(place)

    def remove_place(self, place):
        self.places.remove(place)

    @classmethod
    def get_emails(cls):
        return list(cls.__users_by_email.keys())


