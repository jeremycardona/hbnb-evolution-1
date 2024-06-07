#!/usr/bin/python3
"""Module for testing data manager"""
import unittest
from unittest.mock import Mock, patch
import json
import os
import shutil
from persistence.data_manager import DataManager
from models.user import User
from models.places import Places
from models.amenity import Amenity
from models.city import City
from models.country import Country
from models.reviews import Reviews


class TestDataManager(unittest.TestCase):

    def setUp(self):
        # Setup a temporary storage directory
        self.test_dir = 'test_storage'
        os.makedirs(self.test_dir, exist_ok=True)
        self.data_manager = DataManager(self.test_dir)

    def tearDown(self):
        # Cleanup the temporary storage directory
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_save_user(self):
        user = Mock(spec=User)
        user.get.return_value = {
            'id': 'user123',
            'email': 'test@example.com',
            'password': 'password',
            'firstname': 'John',
            'lastname': 'Doe',
            'created_at': '2024-06-07 15:12:36:907595',
            'updated_at': '2024-06-07 15:12:36:907595'
        }

        self.data_manager.save(user)
        with open(os.path.join(self.test_dir, 'User.json'), 'r') as file:
            data = json.load(file)
        
        self.assertIn('user123', data)
        self.assertEqual(data['user123']['email'], 'test@example.com')

    def test_get_user(self):
        user = Mock(spec=User)
        user.get.return_value = {
            'id': 'user123',
            'email': 'test@example.com',
            'password': 'password',
            'firstname': 'John',
            'lastname': 'Doe',
            'created_at': '2024-06-07 15:12:36:907595',
            'updated_at': '2024-06-07 15:12:36:907595'
        }

        self.data_manager.save(user)
        retrieved_user = self.data_manager.get('user123', 'User')
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user['email'], 'test@example.com')

    def test_update_user(self):
        user = Mock(spec=User)
        user.get.return_value = {
            'id': 'user123',
            'email': 'test@example.com',
            'password': 'password',
            'firstname': 'John',
            'lastname': 'Doe',
            'created_at': '2024-06-07 15:12:36:907595',
            'updated_at': '2024-06-07 15:12:36:907595'
        }

        self.data_manager.save(user)

        updated_user = Mock(spec=User)
        updated_user.get.return_value = {
            'id': 'user123',
            'email': 'updated@example.com',
            'password': 'newpassword',
            'firstname': 'Jane',
            'lastname': 'Smith',
            'created_at': '2024-06-07 15:12:36:907595',
            'updated_at': '2024-06-07 16:00:00:000000'
        }

        self.data_manager.update(updated_user)
        retrieved_user = self.data_manager.get('user123', 'User')
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user['email'], 'updated@example.com')
        self.assertEqual(retrieved_user['firstname'], 'Jane')

    def test_delete_user(self):
        user = Mock(spec=User)
        user.get.return_value = {
            'id': 'user123',
            'email': 'test@example.com',
            'password': 'password',
            'firstname': 'John',
            'lastname': 'Doe',
            'created_at': '2024-06-07 15:12:36:907595',
            'updated_at': '2024-06-07 15:12:36:907595'
        }

        self.data_manager.save(user)
        self.data_manager.delete('user123', 'User')
        retrieved_user = self.data_manager.get('user123', 'User')
        self.assertIsNone(retrieved_user)

    def test_non_existent_entity(self):
        retrieved_user = self.data_manager.get('nonexistent', 'User')
        self.assertIsNone(retrieved_user)

    def test_save_place(self):
        place = Mock(spec=Places)
        place.get.return_value = {
            'id': 'place123',
            'name': 'Test Place',
            'address': '123 Test St',
            'city': 'Test City',
            'latitude': 0.0,
            'longitude': 0.0,
            'user_id': 'user123',
            'rooms': 1,
            'bathrooms': 1,
            'price_by_night': 100,
            'max_guest': 2,
            'amenities': [],
            'reviews': []
        }

        self.data_manager.save(place)
        with open(os.path.join(self.test_dir, 'Places.json'), 'r') as file:
            data = json.load(file)
        
        self.assertIn('place123', data)
        self.assertEqual(data['place123']['name'], 'Test Place')

    def test_get_place(self):
        place = Mock(spec=Places)
        place.get.return_value = {
            'id': 'place123',
            'name': 'Test Place',
            'address': '123 Test St',
            'city': 'Test City',
            'latitude': 0.0,
            'longitude': 0.0,
            'user_id': 'user123',
            'rooms': 1,
            'bathrooms': 1,
            'price_by_night': 100,
            'max_guest': 2,
            'amenities': [],
            'reviews': []
        }

        self.data_manager.save(place)
        retrieved_place = self.data_manager.get('place123', 'Places')
        self.assertIsNotNone(retrieved_place)
        self.assertEqual(retrieved_place['name'], 'Test Place')

    def test_update_place(self):
        place = Mock(spec=Places)
        place.get.return_value = {
            'id': 'place123',
            'name': 'Test Place',
            'address': '123 Test St',
            'city': 'Test City',
            'latitude': 0.0,
            'longitude': 0.0,
            'user_id': 'user123',
            'rooms': 1,
            'bathrooms': 1,
            'price_by_night': 100,
            'max_guest': 2,
            'amenities': [],
            'reviews': []
        }

        self.data_manager.save(place)

        updated_place = Mock(spec=Places)
        updated_place.get.return_value = {
            'id': 'place123',
            'name': 'Updated Place',
            'address': '123 Test St',
            'city': 'Updated City',
            'latitude': 1.0,
            'longitude': 1.0,
            'user_id': 'user123',
            'rooms': 2,
            'bathrooms': 2,
            'price_by_night': 150,
            'max_guest': 4,
            'amenities': [],
            'reviews': []
        }

        self.data_manager.update(updated_place)
        retrieved_place = self.data_manager.get('place123', 'Places')
        self.assertIsNotNone(retrieved_place)
        self.assertEqual(retrieved_place['name'], 'Updated Place')
        self.assertEqual(retrieved_place['city'], 'Updated City')

    def test_delete_place(self):
        place = Mock(spec=Places)
        place.get.return_value = {
            'id': 'place123',
            'name': 'Test Place',
            'address': '123 Test St',
            'city': 'Test City',
            'latitude': 0.0,
            'longitude': 0.0,
            'user_id': 'user123',
            'rooms': 1,
            'bathrooms': 1,
            'price_by_night': 100,
            'max_guest': 2,
            'amenities': [],
            'reviews': []
        }

        self.data_manager.save(place)
        self.data_manager.delete('place123', 'Places')
        retrieved_place = self.data_manager.get('place123', 'Places')
        self.assertIsNone(retrieved_place)

if __name__ == '__main__':
    unittest.main()
