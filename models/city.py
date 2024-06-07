#!/usr/bin/python3
"""Module for city"""
from models.country import Country
from datetime import datetime
import uuid


class City:
    """Methods for city"""
    count = 0
    cities_by_id = {}

    def __init__(self, cityname, country: Country):
        self.__cityid = uuid.uuid4()
        self.cityname = cityname
        self.country = country
        self.__created_at = datetime.now()
        self.__updated_at = datetime.now()
        City.cities_by_id[self.__cityid] = self
        City.count += 1
    @classmethod
    def create(cls, cityname, country: Country):
        new_city = cls(cityname, country)
        return new_city

    def update(self, cityname, country: Country):
        if not isinstance(country, Country):
            raise ValueError("country must be a valid Country instance")
        self.cityname = cityname
        self.country = country
        self.__updated_at = datetime.now()

    def get(self):
        created_at_str = self.__created_at.strftime("%Y-%m-%d %H:%M:%S:%f")
        updated_at_str = self.__updated_at.strftime("%Y-%m-%d %H:%M:%S:%f")
        return {
            "id": str(self.__cityid),
            "cityname": self.cityname,
            "country": self.country.get_country(),
            "created at": created_at_str,
            "updated at": updated_at_str
        }

    def delete(self):
        del City.cities_by_id[self.__cityid]
        City.count -= 1
        del self
