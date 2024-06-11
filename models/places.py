#!/usr/bin/python3
"""Module for places class"""
from datetime import datetime
from models.user import User
import uuid


class Places:
    """Methods for Places"""
    places_by_id = {}

    def __init__(self, description, address, city, latitude, longitude, host,
                 number_of_rooms, bathrooms, price_per_night, max_guests, amenities, reviews):
        self.__placeid = uuid.uuid4()
        # Validate geographical coordinates
        self.__validate_coordinates(latitude, longitude)
        self.__description = description
        self.__address = address
        self.__city = city
        self.__latitude = latitude
        self.__longitude = longitude
        self.__host = host.get()['id']
        self.__number_of_rooms = number_of_rooms
        self.__bathrooms = bathrooms
        self.__price_per_night = price_per_night
        self.__max_guests = max_guests
        self.__amenities = set(amenities)
        self.__reviews = reviews
        self.__created_at = datetime.now()
        self.__updated_at = datetime.now()
        Places.places_by_id[self.__placeid] = self
        host.add_place(self)
         # Validate price per night and max guests
        self.__validate_price_per_night(price_per_night)
        self.__validate_max_guests(max_guests)

    @classmethod
    def create(cls, description, address, city, latitude, longitude, host: User,
                     number_of_rooms, bathrooms, price_per_night, max_guests, amenities, reviews):
        return cls(description, address, city, latitude, longitude, host, number_of_rooms, bathrooms, price_per_night, max_guests, amenities, reviews)

    def get(self):
        created_at_str = self.__created_at.strftime("%Y-%m-%d %H:%M:%S:%f")
        updated_at_str = self.__updated_at.strftime("%Y-%m-%d %H:%M:%S:%f")
        return {
            "id": str(self.__placeid),  # Convert UUID to string for serialization
            "description": self.__description,
            "address": self.__address,
            "city": self.__city,
            "latitude": self.__latitude,
            "longitude": self.__longitude,
            "host": self.__host,
            "number_of_rooms": self.__number_of_rooms,
            "bathrooms": self.__bathrooms,
            "price_per_night": self.__price_per_night,
            "max_guests": self.__max_guests,
            "amenities": list(self.__amenities),
            "reviews": self.__reviews,
            "created_at": created_at_str,
            "updated_at": updated_at_str
        }
    def update(self, description=None, address=None, city=None, latitude=None, longitude=None,
                     host=None, number_of_rooms=None, bathrooms=None, price_per_night=None, max_guests=None,
                     amenities=None, reviews=None):
        if host is not None and host != self.host:
            raise ValueError("Host cannot be reassigned")
        if latitude is not None or longitude is not None:
            self.__validate_coordinates(latitude, longitude)
        if price_per_night is not None:
            self.__validate_price_per_night(price_per_night)
        if max_guests is not None:
            self.__validate_max_guests(max_guests)
        if description is not None:
            self.__description = description
        if address is not None:
            self.__address = address
        if city is not None:
            self.__city = city
        if latitude is not None:
            self.__latitude = latitude
        if longitude is not None:
            self.__longitude = longitude
        if number_of_rooms is not None:
            self.__number_of_rooms = number_of_rooms
        if bathrooms is not None:
            self.__bathrooms = bathrooms
        if price_per_night is not None:
            self.__price_per_night = price_per_night
        if max_guests is not None:
            self.__max_guests = max_guests
        if amenities is not None:
            self.__amenities = amenities
        if reviews is not None:
            self.__reviews = reviews
        self.__updated_at = datetime.now()

    def delete(self):
        del Places.places_by_id[self.__placeid]
        del self
    def add_amenity(self, amenity):
        if amenity in self.__amenities:
            raise ValueError("Amenity already added to this place")
        self.__amenities.add(amenity)
        self.__updated_at = datetime.now()
    def remove_amenity(self, amenity):
        if amenity not in self.__amenities:
            raise ValueError("Amenity not found in this place")
        self.__amenities.remove(amenity)
        self.__updated_at = datetime.now()
    def __validate_coordinates(self, latitude, longitude):
        if not (-90 <= latitude <= 90):
            raise ValueError("Latitude must be between -90 and 90 degrees")
        if not (-180 <= longitude <= 180):
            raise ValueError("Longitude must be between -180 and 180 degrees")
    
    def __validate_price_per_night(self, price_per_night):
        if not (price_per_night > 0):
            raise ValueError("Price per night must be greater than zero")
    
    def __validate_max_guests(self, max_guests):
        if not (max_guests > 0):
            raise ValueError("Maximum guests must be greater than zero")
