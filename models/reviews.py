#!/usr/bin/python3
"""Module for reviews class"""
from datetime import datetime


class Reviews():
    """Methods for reviews"""
    count = 0
    def __init__(self, feedback="", ratings=None):
        self.__reviewid = Reviews.count
        self.__feedback = feedback
        self.__ratings = ratings
        self.__created_at = datetime
        self.__updated_at = datetime
        Reviews.count += 1
    def create_review(self, feedback, ratings):
        self.__feedback = feedback
        self.__ratings = ratings
        self.__updated_at = datetime
    def update_review(self, feedback, ratings):
        self.__feedback = feedback
        self.__ratings = ratings
        self.__updated_at = datetime
    def get_review(self):
        return "Review: " + self.__feedback + " ratings: " + str(self.__ratings)
    def delete_review(self):
        del self
        Reviews.count -= 1

review1 = Reviews("nice", 5)
print(review1.get_review())