#!/usr/bin/python3
"""Module for user, places, and city classes"""
from datetime import datetime
import uuid


class User:
    """Methods for User"""
    users_by_id = {}

    def __init__(self, email, password, first_name, last_name):
        self.userid = uuid.uuid4()  # Generate a unique UUID for each user
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.places = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        User.users_by_id[self.userid] = self

    def add_place(self, place):
        self.places.append(place)

    def remove_place(self, place):
        self.places.remove(place)

    def get_user(self):
        created_at_str = self.created_at.strftime("%Y-%m-%d %H:%M:%S:%f")
        updated_at_str = self.updated_at.strftime("%Y-%m-%d %H:%M:%S:%f")
        return {
            "userid": str(self.userid),  # Convert UUID to string for serialization
            "email": self.email,
            "password": self.password,
            "firstname": self.first_name,
            "lastname": self.last_name,
            "created_at": created_at_str,
            "updated_at": updated_at_str
        }

    def update_email(self, new_email):
        self.email = new_email
        self.updated_at = datetime.now()


class City:
    """Methods for City"""
    cities_by_id = {}

    def __init__(self, name):
        self.cityid = uuid.uuid4()  # Generate a unique UUID for each city
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        City.cities_by_id[self.cityid] = self

    def get_city(self):
        created_at_str = self.created_at.strftime("%Y-%m-%d %H:%M:%S:%f")
        updated_at_str = self.updated_at.strftime("%Y-%m-%d %H:%M:%S:%f")
        return {
            "cityid": str(self.cityid),  # Convert UUID to string for serialization
            "name": self.name,
            "created_at": created_at_str,
            "updated_at": updated_at_str
        }

    def update_name(self, new_name):
        self.name = new_name
        self.updated_at = datetime.now()


class Places:
    """Methods for Places"""
    places_by_id = {}

    def __init__(self, description, address, city: City, latitude, longitude, host: User,
                 number_of_rooms, bathrooms, price_per_night, max_guests, amenities, reviews):
        if not isinstance(city, City):
            raise ValueError("City must be a valid City")
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
    def create_place(cls, description, address, city: City, latitude, longitude, host: User,
                     number_of_rooms, bathrooms, price_per_night, max_guests, amenities, reviews):
        return cls(description, address, city, latitude, longitude, host, number_of_rooms, bathrooms, price_per_night, max_guests, amenities, reviews)

    def get_place(self):
        created_at_str = self.__created_at.strftime("%Y-%m-%d %H:%M:%S:%f")
        updated_at_str = self.__updated_at.strftime("%Y-%m-%d %H:%M:%S:%f")
        return {
            "placeid": str(self.__placeid),  # Convert UUID to string for serialization
            "description": self.__description,
            "address": self.__address,
            "city": self.__city.get_city(),
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

# Example city
ny_city = City("New York")

# Create a place
place1 = Places.create_place(
    "Cozy Apartment", "123 Main St", ny_city, 40.7128, -74.0060, host, 
    2, 1, 150, 4, ["WiFi", "Kitchen"], ["Great place!", "Very clean"]
)
print(place1.get_place())

# Output the unique place ID
print(f"Place ID for the cozy apartment: {place1.get_place()['placeid']}")

# Create another place
sf_city = City("San Francisco")
place2 = Places.create_place(
    "Modern Condo", "456 Elm St", sf_city, 37.7749, -122.4194, host,
    3, 2, 250, 6, ["Pool", "Gym"], ["Awesome stay!", "Highly recommend"]
)
print(place2.get_place())
print(f"Place ID for the modern condo: {place2.get_place()['placeid']}")

# Get all place IDs
print("All place IDs:", list(Places.places_by_id.keys()))

# Get all city IDs
print("All city IDs:", list(City.cities_by_id.keys()))

