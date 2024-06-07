#!/usr/bin/python3
"""Module for country"""
from datetime import datetime

class Country():
    """Methods for country"""
    count = 0
    __country_names = set()

    def __init__(self, countryname=""):
        if countryname.lower() in Country.__country_names:
            raise ValueError(f"Country '{countryname}' already exists")
        self.countryname = countryname
        Country.__country_names.add(countryname.lower())
        Country.count += 1

    @classmethod
    def create(cls, countryname):
        if countryname.lower() in cls.__country_names:
            raise ValueError(f"Country '{countryname}' already exists")
        new_country = cls(countryname)
        return new_country

    def update(self, countryname):
        if countryname.lower() in Country.__country_names:
            raise ValueError(f"Country '{countryname}' already exists")
        Country.__country_names.remove(self.countryname.lower())
        self.countryname = countryname
        Country.__country_names.add(countryname.lower())

    def get(self):
        return {
            "countryname": self.countryname
        }

    def delete(self):
        Country.__country_names.remove(self.countryname.lower())
        del self
        Country.count -= 1
