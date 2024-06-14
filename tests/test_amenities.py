import unittest
import json
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask
from flask.testing import FlaskClient
from api.amenities import amenities
from persistence.data_manager import DataManager
from models.amenity import Amenity

class AmenityAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(amenities)
        self.client = self.app.test_client()
        self.client.testing = True


    def test_health_check(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Amenity Management API is running!")

    def test_create_amenity(self):
        response = self.client.post('/amenities', data=json.dumps({'name': 'WiFi'}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data.decode())
        self.assertIn('id', data)
        self.assertEqual(['WiFi'], data['features'] )

    def test_create_amenity_invalid_input(self):
        response = self.client.post('/amenities', data=json.dumps({'invalid': 'input'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data.decode())
        self.assertEqual(data['error'], 'Invalid input')


    def test_delete_amenity_not_found(self):
        response = self.client.delete('/amenities/nonexistent_id')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data.decode())
        self.assertEqual(data['error'], 'Amenity not found')


if __name__ == '__main__':
    unittest.main()
