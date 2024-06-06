import pytest
from models.places import Places
from models.user import User

def test_delete_place():
    # Create a host user
    host = User("host@example.com", "password", "Alice", "Wonder")
    
    # Create a place
    place = Places.create_place(
        "Beautiful apartment", "123 Main St", "New York", 40.7128, -74.0060, host, 
        2, 1, 150, 4, ["WiFi"], ["Great place!"]
    )
    
    # Ensure the place is in the host's places list
    assert place in host.places
    
    # Delete the place
    place.delete_place()
    
    # Verify the place is removed from Places.places_by_id
    assert place.get_place()['placeid'] not in Places.places_by_id
    
    # Verify the place is removed from the host's places list
    assert place not in host.places
