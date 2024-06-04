#!/usr/bin/python3
"""Module for city"""
from country import Country
from datetime import datetime


class City(Country):
    """methods for city"""
    count = 0
    def __init__(self, cityname, country: Country):
        self.cityid = City.count
        self.cityname = cityname
        self.country = country
        self.countryid = country.get_id()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        City.count += 1
    def create_city(self, cityname):
        self.cityname = cityname
        self.updated_at = datetime.now()
    def update_city(self, cityname, country: Country):
        self.cityname = cityname
        self.countryid = country
        self.updated_at = datetime.now()
    def get_city(self):
        return f"country and city:  {self.country.get_country()} {self.cityname}"
    def delete_city(self):
        del self
        City.count -= 1

puertorico = Country("puerto rico")
isabela = City("isabela", puertorico)
print(isabela.get_city())