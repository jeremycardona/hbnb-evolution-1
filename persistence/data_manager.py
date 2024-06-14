#!/usr/bin/python3
"""Module for data manager class"""

from persistence.persistance_manager import IPersistenceManager
import json
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.user import User
from models.places import Places
from models.amenity import Amenity
from models.city import City
from models.country import Country
from models.reviews import Reviews

class DataManager(IPersistenceManager):
    """Methods for data manager"""

    def __init__(self, storage_directory='storage'):
        self.storage_directory = storage_directory
        os.makedirs(self.storage_directory, exist_ok=True)

    def _get_file_path(self, entity_type):
        return os.path.join(self.storage_directory, f'{entity_type}.json')

    def _read_storage(self, entity_type):
        file_path = self._get_file_path(entity_type)
        try:
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    data = json.load(file)
                    return data
            else:
                return {}
        except Exception as e:
            print(f"Error reading storage file '{file_path}': {e}")
            return {}

    def _write_storage(self, entity_type, data):
        file_path = self._get_file_path(entity_type)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def _convert_to_serializable(self, data):
        if isinstance(data, User):
            return data.get()
        elif isinstance(data, Places):
            return data.get()
        elif isinstance(data, Amenity):
            return data.get()
        elif isinstance(data, City):
            return data.get()
        elif isinstance(data, Country):
            return data.get()
        elif isinstance(data, Reviews):
            return data.get()
        else:
            raise TypeError(f"Unsupported type for serialization: {type(data)}")

    def save(self, entity):
        entity_type = type(entity).__name__
        entity_id = entity.get().get('id', None) or entity.get().get('code')
        print(f"Saving entity: {entity_id} of type {entity_type}")
        storage_data = self._read_storage(entity_type)
        
        # Debug print to ensure storage_data is a dictionary
        print(f"Read storage data: {storage_data}")
        
        serialized_entity = self._convert_to_serializable(entity)
        
        if serialized_entity is None:
            raise ValueError(f"Serialization failed for entity of type {entity_type} with ID {entity_id}")

        print(f"Serialized entity: {serialized_entity}")
        storage_data[entity_id] = serialized_entity
        print(f"Storage data after save: {storage_data}")
        self._write_storage(entity_type, storage_data)

    def get(self, entity_id, entity_type):
        entity_id = str(entity_id)
        storage_data = self._read_storage(entity_type)
        return storage_data.get(entity_id)

    def update(self, entity):
        entity_type = type(entity).__name__  # Get the type (class name) of the entity
        entity_id = entity.get('id', None)  # Get the ID of the entity
        
        # Read the current storage data for the entity type
        storage_data = self._read_storage(entity_type)
        
        # Check if the entity ID exists in the storage data
        if entity_id in storage_data:
            # Update the storage data with the new entity properties
            storage_data[entity_id] = self._convert_to_serializable(entity)
            
            # Write the updated storage data back to the storage file
            self._write_storage(entity_type, storage_data)
        else:
            # Raise an exception if the entity ID is not found in the storage
            raise KeyError(f"Entity with ID {entity_id} not found in {entity_type} storage.")

    def delete(self, entity_id, entity_type):
        entity_id = str(entity_id)
        storage_data = self._read_storage(entity_type)
        if entity_id in storage_data:
            del storage_data[entity_id]
            self._write_storage(entity_type, storage_data)
        else:
            raise KeyError(f"Entity with ID {entity_id} not found in {entity_type} storage.")
    
    def get_all(self, entity_type):
        storage_data = self._read_storage(entity_type)
        return list(storage_data.values())
