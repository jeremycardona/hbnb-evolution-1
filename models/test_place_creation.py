import pytest
from user import User
from city import City
from places import Places

@pytest.fixture
def setup_user_and_city():
    # Create a user
    host = User.create_user("host@example.com", "password", "Alice", "Wonder")
    
    # Create a city
    city = City("San Francisco")
    
    yield host, city
    
    # Clean up after the test
    city.delete_city()
    host.delete_user()

def test_create_place_with_required_fields(setup_user_and_city):
    host, city = setup_user_and_city
    
    # Create a place with all required fields
    place = Places.create_place("Beautiful apartment", "123 Main St", city, 37.7749, -122.4194, host, 2, 1, 100, 4, ["WiFi"], [])
    
    # Verify creation
    place_info = place.get_place()
    assert place_info["description"] == "Beautiful apartment"
    assert place_info["address"] == "123 Main St"
    assert place_info["city"].name == "San Francisco"  # Check if the city name is correct
    assert place_info["latitude"] == 37.7749
    assert place_info["longitude"] == -122.4194
    assert place_info["host"]["email"] == "host@example.com"
    assert place_info["number_of_rooms"] == 2
    assert place_info["bathrooms"] == 1
    assert place_info["price_per_night"] == 100
    assert place_info["max_guests"] == 4
    assert place_info["amenities"] == ["WiFi"]
    assert place_info["reviews"] == []

def test_create_place_missing_required_field(setup_user_and_city):
    host, city = setup_user_and_city
    
    # Attempt to create a place with a missing required field (latitude)
    with pytest.raises(TypeError):
        Places.create_place("Beautiful apartment", "123 Main St", city, None, -122.4194, host, 2, 1, 100, 4, ["WiFi"], [])

def test_create_place_invalid_city(setup_user_and_city):
    host, _ = setup_user_and_city  # Use `_` to ignore the city for this test
    
    # Attempt to create a place with an invalid city (not a City object)
    with pytest.raises(ValueError):
        Places.create_place("Beautiful apartment", "123 Main St", "InvalidCity", 37.7749, -122.4194, host, 2, 1, 100, 4, ["WiFi"], [])

if __name__ == "__main__":
    pytest.main()
