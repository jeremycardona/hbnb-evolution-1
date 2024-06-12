#!/usr/bin/python3
"""Module for amenities api"""
from flask import Blueprint, request, jsonify
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from persistence.data_manager import DataManager
from models.amenity import Amenity


# Create a Blueprint instance
amenities = Blueprint('amenities', __name__)

data_manager = DataManager()

# Health check endpoint
@amenities.route('/')
def index():
    return "Amenity Management API is running!"

# POST /amenities: Create a new amenity
@amenities.route('/amenities', methods=['POST'])
def create_amenity():
    if not request.json or 'name' not in request.json:
        return jsonify({'error': 'Invalid input'}), 400
    name = request.json['name']
    amenity = Amenity(name)
    data_manager.save(amenity)
    return jsonify(amenity.get()), 201

# GET /amenities: Retrieve a list of all amenities
@amenities.route('/amenities', methods=['GET'])
def get_amenities():
    amenities = data_manager.get_all('Amenity')
    return jsonify(amenities), 200

# GET /amenities/<amenity_id>: Retrieve detailed information about a specific amenity
@amenities.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = data_manager.get(amenity_id, 'Amenity')
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404
    return jsonify(amenity), 200

# PUT /amenities/<amenity_id>: Update an existing amenity’s information
@amenities.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    if not request.json or 'name' not in request.json:
        return jsonify({'error': 'Invalid input'}), 400
    amenity_data = data_manager.get(amenity_id, 'Amenity')
    if not amenity_data:
        return jsonify({'error': 'Amenity not found'}), 404
    amenity = Amenity(amenity_data['features'][0])
    amenity.__dict__.update(amenity_data)
    amenity.update(0, request.json['name'])
    data_manager.update(amenity)
    return jsonify(amenity.get()), 200

# DELETE /amenities/<amenity_id>: Delete a specific amenity
@amenities.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    try:
        data_manager.delete(amenity_id, 'Amenity')
        return jsonify({'result': 'Amenity deleted'}), 200
    except KeyError:
        return jsonify({'error': 'Amenity not found'}), 404
    