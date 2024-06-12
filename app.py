#!/usr/bin/python3
"""Main application entry point"""
from flask import Flask
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from api.amenities import amenities
from api.users import users
from api.cities import cities
from api.places import places
from api.reviews import reviews
from persistence.data_manager import DataManager

def main():
    app = Flask(__name__)

    # Initialize DataManager
    data_manager = DataManager()

    # Register blueprints for different APIs
    app.register_blueprint(amenities)
    app.register_blueprint(cities)
    app.register_blueprint(places)
    app.register_blueprint(reviews)
    app.register_blueprint(users)

    return app

if __name__ == '__main__':
    app = main()
    app.run(debug=True)
