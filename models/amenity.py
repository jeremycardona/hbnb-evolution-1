#!/usr/bin/python3
"""Module for amenity class"""
from datetime import datetime

class Amenity():
    """Methods for amenity"""
    count = 0

    def __init__(self, feature):
        Amenity.count += 1  # Increment count only on instantiation
        self.amenityid = Amenity.count
        self.feature = [feature]
        self.__created_at = datetime.now()
        self.__updated_at = datetime.now()

    def create_amenity(self, feature):
        self.feature.append(feature)
        self.__updated_at = datetime.now()

    def update_amenity(self, index, feature):
        if index < len(self.feature):
            self.feature[index] = feature
            self.__updated_at = datetime.now()
        else:
            raise IndexError("Index out of range")

    def get_amenity(self):
        return {
            "id": self.amenityid,
            "features": self.feature[:],
            "created_at": self.__created_at,
            "updated_at": self.__updated_at
        }
    def delete_amenity(self):
        del self
        Amenity.count -= 1

    def updated(self):
        return self.__updated_at

# Example usage:
amen = Amenity("wifi")
amen.create_amenity("fridge")
print(amen.get_amenity())

# another instance
amen2 = Amenity("Sofa")
amen2.create_amenity("stove")
amen2.create_amenity("microwave")
print(amen2.get_amenity())
print("amenities for amen2 are: ", amen2.get_amenity()['features'])
