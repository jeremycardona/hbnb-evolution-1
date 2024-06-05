#!/usr/bin/python3
"""Module for city"""
from country import Country
from datetime import datetime


class City:
    """Methods for city"""
    count = 0
    cities_by_id = {}

    def __init__(self, cityname, country: Country):
        self.__cityid = City.count
        self.cityname = cityname
        self.country = country
        self.__countryid = country.get_id()
        self.__created_at = datetime.now()
        self.__updated_at = datetime.now()
        City.cities_by_id[self.__cityid] = self
        City.count += 1
    @classmethod
    def create_city(cls, cityname, country: Country):
        new_city = cls(cityname, country)
        return new_city

    def update_city(self, cityname, country: Country):
        if not isinstance(country, Country):
            raise ValueError("country must be a valid Country instance")
        self.cityname = cityname
        self.country = country
        self.__countryid = country.get_id()
        self.__updated_at = datetime.now()

    def get_city(self):
        created_at_str = self.__created_at.strftime("%Y-%m-%d %H:%M:%S:%f")
        updated_at_str = self.__updated_at.strftime("%Y-%m-%d %H:%M:%S:%f")
        return {
            "cityid": self.__cityid,
            "cityname": self.cityname,
            "country": self.country.get_country(),
            "countryid": self.__countryid,
            "created at": created_at_str,
            "updated at": updated_at_str
        }

    def delete_city(self):
        del City.cities_by_id[self.__cityid]
        City.count -= 1
        del self

    @classmethod
    def get_ids(cls):
        return list(cls.cities_by_id.keys())

# Example usage
puertorico = Country("Puerto Rico")
isabela = City("Isabela", puertorico)
print(isabela.get_city())

# Output the unique city IDs
print(f"City ID for Isabela: {isabela.get_city()['cityid']}")

# Create another city

sanjuan = City.create_city("San juan", puertorico)
sanjuan2 = City.create_city("San juan", puertorico)
print(f"City ID for San Juan: {sanjuan.get_city()['cityid']}")
# Get all city IDs
print("All city IDs:", City.get_ids())