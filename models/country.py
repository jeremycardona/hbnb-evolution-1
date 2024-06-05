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
        self.countryid = Country.count
        self.countryname = countryname
        Country.__country_names.add(countryname.lower())
        Country.count += 1

    @classmethod
    def create_country(cls, countryname):
        if countryname.lower() in cls.__country_names:
            raise ValueError(f"Country '{countryname}' already exists")
        new_country = cls(countryname)
        return new_country

    def update_country(self, countryname):
        if countryname.lower() in Country.__country_names:
            raise ValueError(f"Country '{countryname}' already exists")
        Country.__country_names.remove(self.countryname.lower())
        self.countryname = countryname
        Country.__country_names.add(countryname.lower())

    def get_country(self):
        return {
            "countryid": self.countryid,
            "countryname": self.countryname
        }

    def delete_country(self):
        Country.__country_names.remove(self.countryname.lower())
        del self
        Country.count -= 1

    def get_id(self):
        return self.countryid

# Example usage:
try:
    puertorico = Country("Puerto Rico")
    print(puertorico.get_country())

    puertorico.update_country("PR")
    print(puertorico.get_country())

    usa = Country.create_country("United States")
    print(usa.get_country())

    # This will raise a ValueError because "United States" already exists
    mexico = Country.create_country("United States")
except ValueError as e:
    print(e)

print(f"Total countries: {Country.count}")
