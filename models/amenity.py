#!/usr/bin/python3
"""Module for amenity class"""
from datetime import datetime


class Amenity():
    """Methods for amenity"""
    count = 0
    def __init__(self, feature):
        self.amenityid = Amenity.count
        self.feature = [feature]
        self.__created_at = datetime.now()
        self.__updated_at = datetime.now()
        Amenity.count += 1

    def create_amenity(self, feature):
        self.feature.append(feature)
        self.__updated_at = datetime.now()

    def update_amenity(self, index, feature):
        if (self.feature[index]):
            self.feature[index] = feature
            self.__updated_at = datetime.now()
        else:
            return None
        
    def get_amenity(self):
        return self.feature[:]
    
    def delete_amenity(self): 
        del self
        count -= 1
    def updated(self):
        return self.__updated_at
amen = Amenity("wifi")
amen.create_amenity("fridge")

print(amen.get_amenity())
print(amen.updated())