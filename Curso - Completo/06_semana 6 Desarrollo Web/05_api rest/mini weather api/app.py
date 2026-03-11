from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'Your_secret_key'

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
db = SQLAlchemy(app)

# User Model
class City(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    temperature = db.Column(db.Integer, nullable=False)
    condition = db.Column(db.String(80), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "temperature": self.temperature,
            "condition": self.condition
        }

# Create Database Tables
with app.app_context():
    db.create_all()

# Get weather condition
def weather_condition(temp):
    if temp < 0:
        return "Snowy"
    elif temp < 10:
        return "Cold"
    elif temp < 20:
        return "Rainy or Cloudy"
    elif temp < 25:
        return "Cloudy"
    elif temp < 30:
        return "Sunny"
    elif temp < 35:
        return "Hot"
    else:
        return "Very Hot"

# Root Endpoint
@app.route('/')
def home():
    return jsonify({"message":"welcome to the Mini Weather API!"})

# Get Weather for all Cities
@app.route('/weather', methods=['GET'])
def get_all_weather():
    cities = City.query.all()
    return jsonify([city.to_dict() for city in cities])

# Get Weather for a specific city
@app.route('/weather/<city>', methods=['GET'])
def get_weather_by_city(city):
    city = City.query.filter_by(name=city.lower()).first()
    if city:
        return jsonify(city.to_dict())
    return jsonify({"error":"City not found"}), 404

# Add New weather data
@app.route('/weather', methods=['POST'])
def add_city_weather():
    data = request.json
    city = data.get('city','').lower()
    temperature = data.get('temperature')

    if not city or not temperature:
        return jsonify({"error":"Missing city or temperature"}), 400
    
    new_city = City(name=city,temperature=temperature,condition=weather_condition(temperature))
    try:
        db.session.add(new_city)
        db.session.commit()
        return jsonify({"message":f"weather for {city} added successfully"}), 201
    except:
        db.session.rollback()
        return jsonify({"error":"City already on database"}), 400

# Update citi weather
@app.route('/weather/<id>', methods=['PUT'])
def update_weather(id):

    city_db = City.query.filter_by(id=id).first()

    if not city_db:
        return jsonify({"error": "City not found"}), 404

    data = request.get_json()

    new_city_name = data.get("city", city_db.name).lower()

    # validar si la ciudad ya existe en otro registro
    existing_city = City.query.filter(
        City.name == new_city_name,
        City.id != id
    ).first()

    if existing_city:
        return jsonify({"error": "City already exists"}), 400

    city_db.name = new_city_name
    city_db.temperature = data.get("temperature", city_db.temperature)
    city_db.condition = weather_condition(city_db.temperature)

    db.session.commit()

    return jsonify(city_db.to_dict())

# Delete city Weather
@app.route('/weather/<id>', methods=['DELETE'])
def delete_city(id):

    city_db = City.query.filter_by(id=id).first()

    if not city_db:
        return jsonify({"error": "City not found"}), 404

    db.session.delete(city_db)
    db.session.commit()

    return jsonify({"message": "City deleted successfully"}),204

if __name__ == '__main__':
    app.run(debug=True)