#!/usr/bin/python3
"""Module for country"""
from datetime import datetime

class Country:
    """Methods for country"""
    count = 0
    __country_names = set()
    __country_codes = set()

    def __init__(self, countryname, code):
        if countryname.lower() in Country.__country_names:
            raise ValueError(f"Country name '{countryname}' already exists")
        if code in Country.__country_codes:
            raise ValueError(f"Country code '{code}' already exists")

        self.countryname = countryname
        self.code = code
        Country.__country_names.add(countryname.lower())
        Country.__country_codes.add(code)
        Country.count += 1

    @classmethod
    def create(cls, countryname, code):
        if countryname.lower() in cls.__country_names:
            raise ValueError(f"Country name '{countryname}' already exists")
        if code in cls.__country_codes:
            raise ValueError(f"Country code '{code}' already exists")
        new_country = cls(countryname, code)
        return new_country

    def update(self, countryname, code):
        if countryname.lower() in Country.__country_names and countryname.lower() != self.countryname.lower():
            raise ValueError(f"Country name '{countryname}' already exists")
        if code in Country.__country_codes and code != self.code:
            raise ValueError(f"Country code '{code}' already exists")

        Country.__country_names.remove(self.countryname.lower())
        Country.__country_codes.remove(self.code)
        self.countryname = countryname
        self.code = code
        Country.__country_names.add(countryname.lower())
        Country.__country_codes.add(code)

    def get(self):
        return {
            "name": self.countryname,
            "code": self.code
        }

    def delete(self):
        Country.__country_names.remove(self.countryname.lower())
        Country.__country_codes.remove(self.code)
        Country.count -= 1
