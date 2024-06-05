#!/usr/bin/python3
"""Module for places class"""
from datetime import datetime
from user import User
import uuid


class Places:
    """Methods for Places"""
    places_by_id = {}

    def __init__(self, description, address, city, latitude, longitude, host: User,
                 number_of_rooms, bathrooms, price_per_night, max_guests, amenities, reviews):
        if not isinstance(host, User):
            raise ValueError("Host must be a valid User")
        self.__placeid = uuid.uuid4()  # Generate a unique UUID for each place
        self.__description = description
        self.__address = address
        self.__city = city
        self.__latitude = latitude
        self.__longitude = longitude
        self.__host = host
        self.__number_of_rooms = number_of_rooms
        self.__bathrooms = bathrooms
        self.__price_per_night = price_per_night
        self.__max_guests = max_guests
        self.__amenities = amenities
        self.__reviews = reviews
        self.__created_at = datetime.now()
        self.__updated_at = datetime.now()
        Places.places_by_id[self.__placeid] = self
        host.add_place(self)

    @classmethod
    def create_place(cls, description, address, city, latitude, longitude, host: User,
                     number_of_rooms, bathrooms, price_per_night, max_guests, amenities, reviews):
        return cls(description, address, city, latitude, longitude, host, number_of_rooms, bathrooms, price_per_night, max_guests, amenities, reviews)

    def get_place(self):
        created_at_str = self.__created_at.strftime("%Y-%m-%d %H:%M:%S:%f")
        updated_at_str = self.__updated_at.strftime("%Y-%m-%d %H:%M:%S:%f")
        return {
            "placeid": str(self.__placeid),  # Convert UUID to string for serialization
            "description": self.__description,
            "address": self.__address,
            "city": self.__city,
            "latitude": self.__latitude,
            "longitude": self.__longitude,
            "host": self.__host.get_user(),
            "number_of_rooms": self.__number_of_rooms,
            "bathrooms": self.__bathrooms,
            "price_per_night": self.__price_per_night,
            "max_guests": self.__max_guests,
            "amenities": self.__amenities,
            "reviews": self.__reviews,
            "created_at": created_at_str,
            "updated_at": updated_at_str
        }

    def update_place(self, description=None, address=None, city=None, latitude=None, longitude=None,
                     number_of_rooms=None, bathrooms=None, price_per_night=None, max_guests=None,
                     amenities=None, reviews=None):
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

    def delete_place(self):
        self.__host.remove_place(self)  # Remove this place from the host's list of places
        del Places.places_by_id[self.__placeid]
        del self

# Example usage
# Assuming you have a User class with methods add_place and remove_place

# Example user
host = User("example@example.com", "abc123", "John", "Smith")

# Create a place
place1 = Places.create_place(
    "Cozy Apartment", "123 Main St", "New York", 40.7128, -74.0060, host, 
    2, 1, 150, 4, ["WiFi", "Kitchen"], ["Great place!", "Very clean"]
)
print(place1.get_place())

# Output the unique place ID
print(f"Place ID for the cozy apartment: {place1.get_place()['placeid']}")

# Create another place
place2 = Places.create_place(
    "Modern Condo", "456 Elm St", "San Francisco", 37.7749, -122.4194, host,
    3, 2, 250, 6, ["Pool", "Gym"], ["Awesome stay!", "Highly recommend"]
)
print(place2.get_place())
print(f"Place ID for the modern condo: {place2.get_place()['placeid']}")

# Get all place IDs
print("All place IDs:", list(Places.places_by_id.keys()))

