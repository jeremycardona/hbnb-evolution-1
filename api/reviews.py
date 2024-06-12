#!/usr/bin/python3
"""Module for Reviews API"""

from flask import Blueprint, jsonify, request
from datetime import datetime
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.user import User
from models.places import Places
from models.reviews import Reviews
from persistence.data_manager import DataManager

reviews = Blueprint('reviews',__name__)
data_manager = DataManager()  # Assuming DataManager handles data operations

# Endpoint: Create a new review for a specified place
@reviews.route('/places/<string:place_id>/reviews', methods=['POST'])
def create_review(place_id):
    data = request.json
    user_id = data.get('user_id')
    rating = data.get('rating')
    comment = data.get('comment')

    if not all([user_id, rating, comment]):
        return jsonify({'error': 'Missing required fields'}), 400

    # Fetch user data
    user_data = data_manager.get(user_id, 'User')
    if not user_data:
        return jsonify({'error': 'User not found'}), 404
    
    # Fetch place data
    place_data = data_manager.get(place_id, 'Places')
    if not place_data:
        return jsonify({'error': 'Place not found'}), 404

    try:
        # Create a new review instance
        new_review = Reviews(
            feedback=comment,
            ratings=rating,
            user=user_data,
            place=place_data
        )

        # Save the new review data
        data_manager.save(new_review)

        # Return a JSON response with the created review details
        return jsonify(new_review.get()), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Endpoint: Retrieve all reviews written by a specific user
@reviews.route('/users/<string:user_id>/reviews', methods=['GET'])
def get_user_reviews(user_id):
    user_reviews = [review for review in data_manager.get_all('Reviews') if review['user']['id'] == user_id]
    return jsonify(user_reviews), 200

# Endpoint: Retrieve all reviews for a specific place
@reviews.route('/places/<string:place_id>/reviews', methods=['GET'])
def get_place_reviews(place_id):
    place_reviews = [review for review in data_manager.get_all('Reviews') if review['place']['id'] == place_id]
    return jsonify(place_reviews), 200

# Endpoint: Retrieve detailed information about a specific review
@reviews.route('/reviews/<string:review_id>', methods=['GET'])
def get_review(review_id):
    review_data = data_manager.get(review_id, 'Reviews')
    if not review_data:
        return jsonify({'error': 'Review not found'}), 404

    return jsonify(review_data), 200

@reviews.route('/reviews/<string:review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.json
    rating = data.get('rating')
    comment = data.get('comment')

    if not all([rating, comment]):
        return jsonify({'error': 'Missing required fields'}), 400

    # Fetch existing review data
    existing_review_data = data_manager.get(review_id, 'Reviews')
    if not existing_review_data:
        return jsonify({'error': 'Review not found'}), 404
    
    try:
        # Fetch user and place data for the review
        user_id = existing_review_data['user']
        place_id = existing_review_data['place']
        
        existing_user_data = data_manager.get(user_id, 'User')
        existing_place_data = data_manager.get(place_id, 'Places')
        
        if not existing_user_data or not existing_place_data:
            return jsonify({'error': 'User or Place data not found or invalid'}), 400

        # Create User and Places objects
        existing_user = User(**existing_user_data)
        existing_place = Places(**existing_place_data)

        # Create Reviews object
        existing_review = Reviews(
            feedback=existing_review_data['feedback'],
            ratings=existing_review_data['ratings'],
            user=existing_user,
            place=existing_place
        )

        # Update the review instance
        existing_review.update(
            feedback=comment,
            ratings=rating
        )
        
        # Save the updated review data
        data_manager.update(existing_review)

        # Return a JSON response with the updated review details
        return jsonify(existing_review.get()), 200

    except KeyError as e:
        return jsonify({'error': f"KeyError: {str(e)}"}), 400
    except ValueError as e:
        return jsonify({'error': f"ValueError: {str(e)}"}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400



# Endpoint: Delete a specific review
@reviews.route('/reviews/<string:review_id>', methods=['DELETE'])
def delete_review(review_id):
    try:
        data_manager.delete(review_id, 'Reviews')
        return jsonify({'message': 'Review deleted successfully'}), 200
    
    except KeyError:
        return jsonify({'error': 'Review not found'}), 404
