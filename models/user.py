#!/usr/bin/python3
""" Module for user class"""
from datetime import datetime


class User():
    """Methods for User"""
    count = 0
    def __init__(self, email=None, password=None, firstname=None, lastname=None):
        self.__email = email
        self.__password = password
        self.firstname = firstname
        self.lastname = lastname
        self.__created_at = datetime.now()
        self.__updated_at = datetime.now()
        self.places = []  # List to hold places hosted by the user
        User.count += 1

    def create_user(self, email, password, firstname, lastname):
        self.__email = email
        self.__password = password
        self.firstname = firstname
        self.lastname = lastname
        self.__updated_at = datetime.now()
    def update_user(self, email, password, firstname, lastname):
        self.__email = email
        self.__password = password
        self.firstname = firstname
        self.lastname = lastname
        self.__updated_at = datetime.now()
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

host = User("example@example.com", "abc123", "John", "Smith")
print(host.get_user())

reviewee = User()
print(reviewee.get_user())

