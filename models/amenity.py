#!/usr/bin/python3
"""Module for amenity class"""
from datetime import datetime
import uuid

class Amenity():
    """Methods for amenity"""

    def __init__(self, feature):
        self.__amenityid = uuid.uuid4()
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
        created_at_str = self.__created_at.strftime("%Y-%m-%d %H:%M:%S:%f")
        updated_at_str = self.__updated_at.strftime("%Y-%m-%d %H:%M:%S:%f")
        return {
            "amenityid": str(self.__amenityid),
            "features": self.feature[:],
            "created_at": created_at_str,
            "updated_at": updated_at_str
        }
    def delete_amenity(self):
        del self

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
