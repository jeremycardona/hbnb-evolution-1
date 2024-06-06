#!/usr/bin/python3
"""Module for testing Places class"""
import pytest
from datetime import datetime
from models.places import Places
from models.user import User

# Mock User class for testing
class MockUser:
    def __init__(self, email):
        self.email = email
        self.places = []

    def add_place(self, place):
        self.places.append(place)

    def remove_place(self, place):
        self.places.remove(place)

def test_valid_coordinates():
    host = MockUser("host@example.com")
    place = Places.create_place(
        "Test Place", "123 Test St", "Test City", 40.7128, -74.0060, host, 
        2, 1, 150, 4, ["WiFi"], ["Great place!"]
    )
    assert place.get_place()["latitude"] == 40.7128
    assert place.get_place()["longitude"] == -74.0060

def test_invalid_latitude():
    host = MockUser("host@example.com")
    with pytest.raises(ValueError, match="Latitude must be between -90 and 90 degrees"):
        Places.create_place(
            "Invalid Place", "789 Elm St", "Invalid City", 100, -87.6298, host,
            2, 1, 120, 3, ["WiFi"], ["Great place!"]
        )

def test_invalid_longitude():
    host = MockUser("host@example.com")
    with pytest.raises(ValueError, match="Longitude must be between -180 and 180 degrees"):
        Places.create_place(
            "Invalid Place", "789 Elm St", "Invalid City", 41.8781, -200, host,
            2, 1, 120, 3, ["WiFi"], ["Great place!"]
        )

def test_valid_price_per_night():
    host = MockUser("host@example.com")
    place = Places.create_place(
        "Test Place", "123 Test St", "Test City", 40.7128, -74.0060, host, 
        2, 1, 150, 4, ["WiFi"], ["Great place!"]
    )
    assert place.get_place()["price_per_night"] == 150

def test_invalid_price_per_night():
    host = MockUser("host@example.com")
    with pytest.raises(ValueError, match="Price per night must be greater than zero"):
        Places.create_place(
            "Invalid Place", "789 Elm St", "Invalid City", 41.8781, -87.6298, host,
            2, 1, -120, 3, ["WiFi"], ["Great place!"]
        )

def test_valid_max_guests():
    host = MockUser("host@example.com")
    place = Places.create_place(
        "Test Place", "123 Test St", "Test City", 40.7128, -74.0060, host, 
        2, 1, 150, 4, ["WiFi"], ["Great place!"]
    )
    assert place.get_place()["max_guests"] == 4

def test_invalid_max_guests():
    host = MockUser("host@example.com")
    with pytest.raises(ValueError, match="Maximum guests must be greater than zero"):
        Places.create_place(
            "Invalid Place", "789 Elm St", "Invalid City", 41.8781, -87.6298, host,
            2, 1, 120, 0, ["WiFi"], ["Great place!"]
        )

