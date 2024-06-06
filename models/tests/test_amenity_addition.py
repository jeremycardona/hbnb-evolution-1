#!/usr/bin/python3
"""Module for testing amenity addition verifying that duplicates cannot be added to the same place"""
import pytest
from places import Places
from user import User
from city import City
from country import Country
from amenity import Amenity
def test_add_amenities_to_place():
    # Create a user and a city
    host = User("host@example.com", "password123", "Alice", "Wonder")
    country = Country("Alice")
    city = City("Wonderland", country)

    # Create a place
    place = Places.create_place(
        "Charming place", "123 Imaginary Rd", city, 51.5074, -0.1278, host, 3, 2, 150, 6, ["WiFi"], []
    )

    # Add a new amenity
    place.add_amenity("Pool")
    assert "Pool" in place.get_place()["amenities"]

    # Attempt to add the same amenity again
    with pytest.raises(ValueError):
        place.add_amenity("Pool")

def test_remove_amenity_from_place():
    # Create a user and a city
    host = User("host@example.com", "password123", "Alice", "Wonder")
    country = Country("xmen")
    city = City("Wonderland", country)

    # Create a place
    place = Places.create_place(
        "Charming place", "123 Imaginary Rd", city, 51.5074, -0.1278, host, 3, 2, 150, 6, ["WiFi", "Pool"], []
    )

    # Remove an existing amenity
    place.remove_amenity("Pool")
    assert "Pool" not in place.get_place()["amenities"]

    # Attempt to remove a non-existing amenity
    with pytest.raises(ValueError):
        place.remove_amenity("NonExistingAmenity")
