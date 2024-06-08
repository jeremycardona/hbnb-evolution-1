#!/usr/bin/python3
"""Module for city and country api"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, request, jsonify
from models.country import Country
from models.city import City


app = Flask(__name__)

# Pre-load countries based on ISO 3166-1 alpha-2 codification
preloaded_countries = [
    {"name": "United States", "code": "US"},
    {"name": "Canada", "code": "CA"},
    {"name": "Mexico", "code": "MX"},
    # Add more countries as needed
]

for country in preloaded_countries:
    Country.create(country["name"], country["code"])

@app.route('/countries', methods=['GET'])
def get_countries():
    countries = [country.get() for country in Country.countries_by_code.values()]
    return jsonify(countries), 200

@app.route('/countries/<country_code>', methods=['GET'])
def get_country(country_code):
    country = Country.countries_by_code.get(country_code.lower())
    if not country:
        return jsonify({"error": "Country not found"}), 404
    return jsonify(country.get()), 200

@app.route('/countries/<country_code>/cities', methods=['GET'])
def get_cities_by_country(country_code):
    country = Country.countries_by_code.get(country_code.lower())
    if not country:
        return jsonify({"error": "Country not found"}), 404
    cities = [city.get() for city in City.cities_by_id.values() if city.country.code.lower() == country_code.lower()]
    return jsonify(cities), 200

@app.route('/cities', methods=['POST'])
def create_city():
    data = request.get_json()
    cityname = data.get('cityname')
    country_code = data.get('country_code')
    country = Country.countries_by_code.get(country_code.lower())
    if not country:
        return jsonify({"error": "Country not found"}), 404
    city = City.create(cityname, country)
    return jsonify(city.get()), 201

@app.route('/cities', methods=['GET'])
def get_cities():
    cities = [city.get() for city in City.cities_by_id.values()]
    return jsonify(cities), 200

@app.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    city = City.cities_by_id.get(city_id)
    if not city:
        return jsonify({"error": "City not found"}), 404
    return jsonify(city.get()), 200

@app.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    data = request.get_json()
    city = City.cities_by_id.get(city_id)
    if not city:
        return jsonify({"error": "City not found"}), 404
    cityname = data.get('cityname')
    country_code = data.get('country_code')
    country = Country.countries_by_code.get(country_code.lower())
    if not country:
        return jsonify({"error": "Country not found"}), 404
    city.update(cityname, country)
    return jsonify(city.get()), 200

@app.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    city = City.cities_by_id.get(city_id)
    if not city:
        return jsonify({"error": "City not found"}), 404
    city.delete()
    return jsonify({"message": "City deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
