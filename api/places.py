#!/usr/bin/python3
"""Module for places API"""
from flask import Blueprint, request, jsonify
import os
import sys
import uuid
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, jsonify, request
from models.places import Places
from models.user import User  # Assuming User class for host management
from persistence.data_manager import DataManager  # Assuming data_manager for data operations

places = Blueprint('places', __name__)
data_manager = DataManager()  # Initialize your data manager instance


@places.route('/places', methods=['POST'])
def create_place():
    data = request.json

    # Extract data from JSON payload
    description = data.get('description')
    address = data.get('address')
    city_id = data.get('city_id')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    host_id = data.get('host_id')
    number_of_rooms = data.get('number_of_rooms')
    bathrooms = data.get('number_of_bathrooms')
    price_per_night = data.get('price_per_night')
    max_guests = data.get('max_guests')
    amenity_ids = data.get('amenity_ids', [])
    reviews = data.get('reviews', [])

    # Fetch host data
    host_data = data_manager.get(host_id, 'User')
    if not host_data:
        return jsonify({'error': 'Host not found'}), 404

    # Fetch city data
    city_data = data_manager.get(city_id, 'City')
    if not city_data:
        return jsonify({'error': 'City not found'}), 404

    # Create a new place instance
    new_place = Places.create(
        description=description,
        address=address,
        city=city_id,
        latitude=latitude,
        longitude=longitude,
        host=User(
            email=host_data['email'],
            password=host_data['password'],
            firstname=host_data['firstname'],
            lastname=host_data['lastname']
        ),
        number_of_rooms=number_of_rooms,
        bathrooms=bathrooms,
        price_per_night=price_per_night,
        max_guests=max_guests,
        amenities=amenity_ids,  # Assuming amenity_ids are directly passed
        reviews=reviews
    )

    try:
        # Save the new place data
        data_manager.save(new_place)

        # Return a JSON response with the created place details
        return jsonify(new_place.get()), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@places.route('/places', methods=['GET'])
def get_all_places():
    all_places = [place.get() for place in Places.places_by_id.values()]
    return jsonify(all_places)

@places.route('/places/<string:place_id>', methods=['GET'])
def get_place(place_id):
    place = Places.places_by_id.get(uuid.UUID(place_id))
    if not place:
        return jsonify({'error': 'Place not found'}), 404
    return jsonify(place.get())

@places.route('/places/<string:place_id>', methods=['PUT'])
def update_place(place_id):
    data = request.json
    place = Places.places_by_id.get(uuid.UUID(place_id))
    if not place:
        return jsonify({'error': 'Place not found'}), 404

    # Validate and fetch city data
    city_id = data.get('city_id')
    city_data = data_manager.get(city_id, 'City')
    if not city_data:
        return jsonify({'error': 'City not found'}), 404

    # Validate latitude and longitude
    try:
        latitude = float(data.get('latitude', place.get()['latitude']))
        longitude = float(data.get('longitude', place.get()['longitude']))
        # Validate within appropriate ranges
        if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
            raise ValueError("Latitude must be between -90 and 90 degrees. Longitude must be between -180 and 180 degrees.")
    except ValueError:
        return jsonify({'error': 'Invalid latitude or longitude'}), 400

    # Validate amenity IDs
    amenity_ids = data.get('amenity_ids', [])
    invalid_amenities = [aid for aid in amenity_ids if not data_manager.get(aid, 'Amenity')]
    if invalid_amenities:
        return jsonify({'error': f'Amenities not found: {", ".join(invalid_amenities)}'}), 404

    try:
        place.update(
            description=data.get('description', place.description),
            address=data.get('address', place.address),
            city=city_id,
            latitude=latitude,
            longitude=longitude,
            host=None,  # Update host if necessary
            number_of_rooms=data.get('number_of_rooms', place.number_of_rooms),
            bathrooms=data.get('number_of_bathrooms', place.bathrooms),
            price_per_night=data.get('price_per_night', place.price_per_night),
            max_guests=data.get('max_guests', place.max_guests),
            amenities=amenity_ids,
            reviews=data.get('reviews', place.reviews)
        )
        data_manager.save(place.get(), 'Places')
        return jsonify(place.get())

    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@places.route('/places/<string:place_id>', methods=['DELETE'])
def delete_place(place_id):
    place = Places.places_by_id.get(uuid.UUID(place_id))
    if not place:
        return jsonify({'error': 'Place not found'}), 404

    try:
        place.delete()

        return jsonify({'message': 'Place deleted successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
