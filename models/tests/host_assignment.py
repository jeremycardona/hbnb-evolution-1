#!/usr/bin/python3
import pytest
from models.places import Places
from models.user import User
from models.city import City


def test_place_host_assignment():
    # Create initial host and place
    initial_host = User("initial_host@example.com", "password123", "Initial", "Host")
    city = City("Initial City")
    place = Places.create_place(
        "Initial description", "123 Main St", city, 37.7749, -122.4194, initial_host, 2, 1, 100, 4, ["WiFi"], []
    )
    assert place.get_place()["host"]["email"] == "initial_host@example.com"

    # Create new host
    new_host = User("new_host@example.com", "password456", "New", "Host")

    # Reassign host
    place.reassign_host(new_host)
    assert place.get_place()["host"]["email"] == "new_host@example.com"
    assert "initial_host@example.com" not in [p.get_place()["host"]["email"] for p in initial_host.places]
    assert place in new_host.places

def test_place_host_reassignment():
    # Create initial host and place
    initial_host = User("initial_host@example.com", "password123", "Initial", "Host")
    city = City("Initial City")
    place = Places.create_place(
        "Initial description", "123 Main St", city, 37.7749, -122.4194, initial_host, 2, 1, 100, 4, ["WiFi"], []
    )

    # Attempt reassigning to a non-User host
    with pytest.raises(ValueError):
        place.reassign_host("Not a user")

    # Ensure the host is still the initial host
    assert place.get_place()["host"]["email"] == "initial_host@example.com"
