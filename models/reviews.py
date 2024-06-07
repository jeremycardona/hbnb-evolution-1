#!/usr/bin/python3
"""Module for reviews class"""
from datetime import datetime
import uuid
from models.user import User
from models.places import Places

class Reviews:
    """Methods for reviews"""
    count = 0

    def __init__(self, feedback, ratings, user: User, place: Places):
        Reviews.count += 1  # Increment count only on instantiation
        self.__reviewid = uuid.uuid4()  # Generate a unique UUID for each review
        self.__feedback = feedback
        self.__ratings = ratings
        self.__user = user
        self.__place = place
        self.__created_at = datetime.now()
        self.__updated_at = datetime.now()

    @classmethod
    def create(cls, feedback, ratings):
        new_review = cls(feedback, ratings)
        return new_review

    def update(self, feedback, ratings):
        self.__feedback = feedback
        self.__ratings = ratings
        self.__updated_at = datetime.now()

    def get(self):
        created_at_str = self.__created_at.strftime("%Y-%m-%d %H:%M:%S:%f")
        updated_at_str = self.__updated_at.strftime("%Y-%m-%d %H:%M:%S:%f")
        return {
            "id": str(self.__reviewid),  # Convert UUID to string for serialization
            "feedback": self.__feedback,
            "ratings": self.__ratings,
            "created_at": created_at_str,
            "updated_at": updated_at_str
        }

    def delete(self):
        del self
        Reviews.count -= 1

