# mainplaces.py
from user import User
from places import Places

# Example user
host = User("example@example.com", "abc123", "John", "Smith")

# Create a place
place1 = Places.create_place(
    "Cozy Apartment", "123 Main St", "New York", 40.7128, -74.0060, host, 
    2, 1, 150, 4, ["WiFi", "Kitchen"], ["Great place!", "Very clean"]
)
print(place1.get_place())

# Output the unique place ID
print(f"Place ID for the cozy apartment: {place1.get_place()['placeid']}")

# Create another place
place2 = Places.create_place(
    "Modern Condo", "456 Elm St", "San Francisco", 37.7749, -122.4194, host,
    3, 2, 250, 6, ["Pool", "Gym"], ["Awesome stay!", "Highly recommend"]
)
print(place2.get_place())
print(f"Place ID for the modern condo: {place2.get_place()['placeid']}")

# Get all place IDs
print("All place IDs:", list(Places.places_by_id.keys()))

