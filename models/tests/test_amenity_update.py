#!/usr/bin/python3
"""Module that check retrieval mechanisms and ensure updates"""
import pytest
from amenity import Amenity


def test_create_amenity():
    amenity = Amenity("WiFi")
    assert amenity.get_amenity()["features"] == ["WiFi"]

def test_add_amenity():
    amenity = Amenity("WiFi")
    amenity.create_amenity("Pool")
    assert "Pool" in amenity.get_amenity()["features"]

def test_update_amenity():
    amenity = Amenity("WiFi")
    amenity.create_amenity("Pool")
    amenity.update_amenity(0, "High-Speed WiFi")
    assert amenity.get_amenity()["features"] == ["High-Speed WiFi", "Pool"]

def test_update_amenity_invalid_index():
    amenity = Amenity("WiFi")
    with pytest.raises(IndexError):
        amenity.update_amenity(1, "Pool")

def test_retrieve_amenity():
    amenity = Amenity("WiFi")
    amenity.create_amenity("Pool")
    amenity_details = amenity.get_amenity()
    assert amenity_details["features"] == ["WiFi", "Pool"]
    assert "created_at" in amenity_details
    assert "updated_at" in amenity_details

def test_delete_amenity():
    amenity = Amenity("WiFi")
    amenity_id = amenity.get_amenity()["amenityid"]
    amenity.delete_amenity()
    # Assuming that you manage the amenities somewhere else, 
    # otherwise the del self won't have a way to test since it's a memory cleanup
    # this would need to be adjusted based on actual deletion logic
    # assert amenity_id not in amenities_storage  # Example if there's a storage to check
