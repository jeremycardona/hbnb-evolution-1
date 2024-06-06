#!/usr/bin/python3
import pytest
from user import User
from places import Places


def test_create_place_with_required_fields():
    host = User("host@example.com", "password", "Alice", "Wonder")
    place = Places.create_place(
        "Beautiful apartment", "123 Main St", "San Francisco", 37.7749, -122.4194, host,
        2, 1, 100, 4, ["WiFi"], []
    )
    assert place.get_place()["description"] == "Beautiful apartment"

def test_create_place_missing_required_field():
    host = User("host2@example.com", "password", "Bob", "Builder")
    with pytest.raises(ValueError, match="Missing required field"):
        Places.create_place(
            "Nice place", None, "San Francisco", 37.7749, -122.4194, host,
            2, 1, 100, 4, ["WiFi"], []
        )

def test_create_place_invalid_field_type():
    host = User("host3@example.com", "password", "Charlie", "Brown")
    with pytest.raises(TypeError):
        # Passing a string instead of a User object for the host
        Places.create_place(
            "Another place", "456 Main St", "San Francisco", 37.7749, -122.4194, "NotAUser",
            2, 1, 100, 4, ["WiFi"], []
        )

if __name__ == "__main__":
    pytest.main()
