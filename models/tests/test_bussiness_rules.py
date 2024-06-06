#!/usr/bin/python3
"""test bussiness logic"""
from places import Places
from user import User 
from reviews import Reviews
from amenity import Amenity
from city import City
from country import Country


def bussiness_rules():
        # Create User
        user1 = User.create_user("user1@example.com", "password123", "John", "Doe")
        assert user1.get_user()["email"] == "user1@example.com"

        # Email Uniqueness
        try:
            User.create_user("user1@example.com", "password456", "Jane", "Smith")
        except ValueError as e:
            assert str(e) == "Email already in use"

        # Update User
        user1.update_user("newemail@example.com", "newpassword", "John", "Doe")
        assert user1.get_user()["email"] == "newemail@example.com"

        # Delete User
        user1.delete_user()
        assert "newemail@example.com" not in User.get_emails()

        # Create Amenity
        amenity1 = Amenity("WiFi")
        assert "WiFi" in amenity1.get_amenity()["features"]

        # Update Amenity
        amenity1.update_amenity(0, "High-Speed WiFi")
        assert "High-Speed WiFi" in amenity1.get_amenity()["features"]

        # Delete Amenity
        amenity1.delete_amenity()

        # Create City
        city1 = City("New York")
        assert city1.get_city()["name"] == "New York"

        # Unique City Name
        try:
            City("New York")
        except ValueError as e:
            assert str(e) == "City 'New York' already exists"

        # Update City
        city1.update_name("Los Angeles")
        assert city1.get_city()["name"] == "Los Angeles"

        # Delete City
        city1.delete_city()

        # Create Country
        country1 = Country.create_country("USA")
        assert country1.get_country()["countryname"] == "USA"

        # Unique Country Name
        try:
            Country.create_country("USA")
        except ValueError as e:
            assert str(e) == "Country 'USA' already exists"

        # Update Country
        country1.update_country("United States")
        assert country1.get_country()["countryname"] == "United States"

        # Delete Country
        country1.delete_country()

        # Create Place
        city2 = City("San Francisco")
        host = User.create_user("host@example.com", "password", "Alice", "Wonder")
        place1 = Places.create_place("Beautiful apartment", "123 Main St", city2, 37.7749, -122.4194, host, 2, 1, 100, 4, ["WiFi"], [])
        assert place1.get_place()["description"] == "Beautiful apartment"

        # Update Place
        place1.update_place(description="Updated description")
        assert place1.get_place()["description"] == "Updated description"

        # Delete Place
        place1.delete_place()

        # Create Review
        review1 = Reviews.create_review("Great place!", 5)
        assert review1.get_review()["feedback"] == "Great place!"

        # Update Review
        review1.update_review("Amazing place!", 5)
        assert review1.get_review()["feedback"] == "Amazing place!"

        # Delete Review
        review1.delete_review()