#!/usr/bin/python3
"""Module for country"""
from datetime import datetime


class Country():
    """Methods for country"""
    count = 0
    def __init__(self, countryname=""):
        self.countryid = Country.count
        self.countryname = countryname
        Country.count += 1
    def create_country(self, countyname):
        self.countryname = countyname
    def update_country(self, countryname):
        self.countryname = countryname
    def get_country(self):
        return self.countryname
    def delete_country(self):
        del self
        Country.count -= 1
    def get_id(self):
        return self.countryid

puertorico = Country("Puerto rico")
print(puertorico.get_country())