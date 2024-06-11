#!/usr/bin/python3
"""Main application entry point"""
from flask import Flask, request, jsonify
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from persistence.data_manager import DataManager
import api.amenities
import api.cities
import api.places
import api.reviews
import api.users


def main():

    app = Flask(__name__)
    if __name__ == '__main__':
        app.run(debug=True)