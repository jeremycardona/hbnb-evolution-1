#!/usr/bin/python3
"""Module for users api"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Blueprint, request, jsonify
from persistence.data_manager import DataManager
from models.user import User

users = Blueprint('users', __name__)
data_manager = DataManager()

# POST /users: Create a new user
@users.route('/users', methods=['POST'])
def create_user():
    data = request.json
    try:
        user = User.create(data['email'], data['password'], data['firstname'], data['lastname'])
        data_manager.save(user)
        return jsonify(user.get()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

# GET /users: Retrieve a list of all users
@users.route('/users', methods=['GET'])
def get_users():
    users = data_manager.get_all('User')
    return jsonify(users), 200

# GET /users/<user_id>: Retrieve details of a specific user
@users.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = data_manager.get(user_id, 'User')
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

# PUT /users/<user_id>: Update an existing user
@users.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    pass
# DELETE /users/<user_id>: Delete a user
@users.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    pass
