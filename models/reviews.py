#!/usr/bin/python3
"""Module for reviews class"""
from datetime import datetime

class Reviews():
    """Methods for reviews"""
    count = 0

    def __init__(self, feedback="", ratings=None):
        Reviews.count += 1  # Increment count only on instantiation
        self.__reviewid = Reviews.count
        self.__feedback = feedback
        self.__ratings = ratings
        self.__created_at = datetime.now()
        self.__updated_at = datetime.now()

    @classmethod
    def create_review(cls, feedback, ratings):
        new_review = cls(feedback, ratings)
        return new_review

    def update_review(self, feedback, ratings):
        self.__feedback = feedback
        self.__ratings = ratings
        self.__updated_at = datetime.now()

    def get_review(self):
        return f"Review ID: {self.__reviewid}, Feedback: {self.__feedback}, Ratings: {self.__ratings}"

    def delete_review(self):
        del self
        Reviews.count -= 1

# Example usage:
review1 = Reviews("nice", 5)
print(review1.get_review())

review2 = Reviews.create_review("great", 4)
print(review2.get_review())
