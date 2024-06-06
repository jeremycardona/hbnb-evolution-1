#!/usr/bin/python3
"""Module for testing create place"""
import pytest
from models.places import Places
from models.user import User
from models.city import City
from models.country import Country
def test_create_place_with_all_required_fields():
    host = User("host@example.com", "password", "Alice", "Wonder")
    place = Places.create_place(
        "Beautiful apartment", "123 Main St", "New York", 40.7128, -74.0060, host, 
        2, 1, 150, 4, ["WiFi"], ["Great place!"]
    )
    place_details = place.get_place()
    assert place_details["description"] == "Beautiful apartment"
    assert place_details["address"] == "123 Main St"
    assert place_details["city"] == "New York"
    assert place_details["latitude"] == 40.7128
    assert place_details["longitude"] == -74.0060
    assert place_details["host"]["email"] == "host@example.com"
    assert place_details["number_of_rooms"] == 2
    assert place_details["bathrooms"] == 1
    assert place_details["price_per_night"] == 150
    assert place_details["max_guests"] == 4
    assert "WiFi" in place_details["amenities"]
    assert "Great place!" in place_details["reviews"]

def test_create_place_missing_required_field():
    host = User("host2@example.com", "password", "Bob", "Builder")
    with pytest.raises(TypeError):
        Places.create_place(
            description="Cozy House",
            address="456 Elm St",
            city="San Francisco",
            latitude=37.7749,
            longitude=-122.4194,
            host=host,
            number_of_rooms=3,
            bathrooms=2,
            price_per_night=200,
            max_guests=6,
            amenities=None,  # Missing amenities
            reviews=["Amazing stay!"]
        )

def test_update_place():
    host = User("host4@example.com", "password", "Dora", "Explorer")
    place = Places.create_place(
        "Modern Apartment", "321 Oak St", "Los Angeles", 34.0522, -118.2437, host, 
        2, 2, 180, 4, ["WiFi"], ["Fantastic place!"]
    )
    place.update_place(description="Updated Modern Apartment")
    assert place.get_place()["description"] == "Updated Modern Apartment"

def test_delete_place():
    host = User("host5@example.com", "password", "Eve", "Adams")
    place = Places.create_place(
        "Luxurious Villa", "654 Maple St", "Miami", 25.7617, -80.1918, host, 
        5, 4, 500, 10, ["Pool", "Jacuzzi"], ["Best vacation ever!"]
    )
    place_id = place.get_place()["placeid"]
    place.delete_place()
    assert place_id not in Places.places_by_id

def test_add_amenity():
    host = User("host6@example.com", "password", "Frank", "Smith")
    place = Places.create_place(
        "Charming Cottage", "987 Cedar St", "Boston", 42.3601, -71.0589, host, 
        3, 2, 200, 5, ["WiFi"], ["Lovely stay!"]
    )
    place.add_amenity("Fireplace")
    assert "Fireplace" in place.get_place()["amenities"]

def test_add_duplicate_amenity():
    host = User("host7@example.com", "password", "Grace", "Lee")
    place = Places.create_place(
        "Cozy Cabin", "111 Birch St", "Denver", 39.7392, -104.9903, host, 
        2, 1, 120, 3, ["WiFi"], ["Great getaway!"]
    )
    with pytest.raises(ValueError):
        place.add_amenity("WiFi")

def test_remove_amenity():
    host = User("host8@example.com", "password", "Hank", "Green")
    place = Places.create_place(
        "Rustic Lodge", "222 Pine St", "Seattle", 47.6062, -122.3321, host, 
        4, 3, 350, 7, ["Pool", "Sauna"], ["Amazing place!"]
    )
    place.remove_amenity("Sauna")
    assert "Sauna"
