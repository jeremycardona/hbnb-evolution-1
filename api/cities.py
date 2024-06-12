#!/usr/bin/python3
"""Module for city and country api"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Blueprint, request, jsonify
from models.country import Country
from models.city import City
from persistence.data_manager import DataManager

cities = Blueprint('cities', __name__)
# Initialize the DataManager
data_manager = DataManager()

# Pre-load countries based on ISO 3166-1 standard (for simplicity, a subset)
preloaded_countries = [
    #{"countryname": "United States", "code": "US"},
    #{"countryname": "United Kingdom", "code": "GB"},
    #{"countryname": "France", "code": "FR"},
    #{"countryname": "Puerto Rico", "code": "PR"},
    #{"countryname": "Mexico", "code": "MX"},
    #{"countryname": "Dominican Republic", "code": "RD"}
]

# Save pre-loaded countries using DataManager
for country_data in preloaded_countries:
    country = Country(**country_data)
    data_manager.save(country)


@cities.route('/countries', methods=['GET'])
def get_countries():
    countries = data_manager.get_all('Country')
    return jsonify(countries)


@cities.route('/countries/<country_code>', methods=['GET'])
def get_country(country_code):
    country = data_manager.get(country_code, 'Country')
    if country:
        return jsonify(country)
    return jsonify({"error": "Country not found"}), 404


@cities.route('/countries/<country_code>/cities', methods=['GET'])
def get_cities_by_country(country_code):
    country = data_manager.get(country_code, 'Country')
    if country:
        cities = [city for city in data_manager.get_all('City') if city['country']['code'] == country_code]
        return jsonify(cities)
    return jsonify({"error": "Country not found"}), 404


@cities.route('/cities', methods=['POST'])
def create_city():
    data = request.get_json()
    cityname = data.get('cityname')
    country_code = data.get('country_code')

    country = data_manager.get(country_code, 'Country')
    if not country:
        return jsonify({"error": "Country not found"}), 404

    country_instance = Country(country['name'], country['code'])
    new_city = City.create(cityname, country_instance)
    data_manager.save(new_city)
    return jsonify(new_city.get()), 201


@cities.route('/cities', methods=['GET'])
def get_all_cities():
    cities = data_manager.get_all('City')
    return jsonify(cities)


@cities.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    city = data_manager.get(city_id, 'City')
    if city:
        return jsonify(city)
    return jsonify({"error": "City not found"}), 404


@cities.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    city_data = data_manager.get(city_id, 'City')
    if not city_data:
        return jsonify({"error": "City not found"}), 404

    data = request.get_json()
    cityname = data.get('cityname')
    country_code = data.get('country_code')

    country = data_manager.get(country_code, 'Country')
    if not country:
        return jsonify({"error": "Country not found"}), 404

    country_instance = Country(country['name'], country['code'])
    city = City(city_data['cityname'], country_instance)
    city.update(cityname, country_instance)
    data_manager.update(city)
    return jsonify(city.get())


@cities.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    city_data = data_manager.get(city_id, 'City')
    if city_data:
        data_manager.delete(city_id, 'City')
        return jsonify({"message": "City deleted successfully"})
    return jsonify({"error": "City not found"}), 404

