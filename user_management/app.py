from flask import Flask, request, jsonify, abort
from gevent.pywsgi import WSGIServer
from flask_restx import Api, Resource, fields
from datetime import datetime
import uuid

app = Flask(__name__)
api = Api(app)

# Pre-loaded country data based on ISO 3166-1 alpha-2
countries = {
    "US": {"name": "United States", "code": "US"},
    "CA": {"name": "Canada", "code": "CA"},
    "GB": {"name": "United Kingdom", "code": "GB"}
}

# Dummy data store for cities
cities = {}

# City Model
city_model = api.model('City', {
    'name': fields.String(required=True, description='City name'),
    'country_code': fields.String(required=True, description='ISO country code')
})

class City:
    def __init__(self, name, country_code):
        self.id = str(uuid.uuid4())
        self.name = name
        self.country_code = country_code
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Endpoints for Countries
@api.route('/countries')
class CountryList(Resource):
    def get(self):
        return jsonify(countries)

@api.route('/countries/<string:country_code>')
class Country(Resource):
    def get(self, country_code):
        country = countries.get(country_code.upper())
        if not country:
            abort(404, description="Country not found")
        return jsonify(country)

@api.route('/countries/<string:country_code>/cities')
class CountryCities(Resource):
    def get(self, country_code):
        country_code = country_code.upper()
        if country_code not in countries:
            abort(404, description="Country not found")
        country_cities = [city for city in cities.values() if city['country_code'] == country_code]
        return jsonify(country_cities)

# Endpoints for Cities
@api.route('/cities')
class CityList(Resource):
    @api.expect(city_model)
    def post(self):
        data = request.json
        name = data.get('name')
        country_code = data.get('country_code').upper()

        if country_code not in countries:
            abort(400, description="Invalid country code")
        
        if any(city['name'] == name and city['country_code'] == country_code for city in cities.values()):
            abort(409, description="City name already exists in this country")

        city = City(name, country_code)
        cities[city.id] = city.__dict__
        return jsonify(city.__dict__), 201

    def get(self):
        return jsonify(list(cities.values()))

@api.route('/cities/<string:city_id>')
class CityResource(Resource):
    def get(self, city_id):
        city = cities.get(city_id)
        if not city:
            abort(404, description="City not found")
        return jsonify(city)

    @api.expect(city_model)
    def put(self, city_id):
        city = cities.get(city_id)
        if not city:
            abort(404, description="City not found")

        data = request.json
        name = data.get('name')
        country_code = data.get('country_code').upper()

        if country_code not in countries:
            abort(400, description="Invalid country code")

        if any(c['name'] == name and c['country_code'] == country_code and c['id'] != city_id for c in cities.values()):
            abort(409, description="City name already exists in this country")

        city['name'] = name
        city['country_code'] = country_code
        city['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return jsonify(city)

    def delete(self, city_id):
        if city_id not in cities:
            abort(404, description="City not found")
        del cities[city_id]
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)

