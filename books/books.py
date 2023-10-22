from flask import Flask, request, render_template, Blueprint

books_bp = Blueprint('books_bp', __name__,
    template_folder='templates',
    static_folder='static', static_url_path='assets')

# In-memory data for demonstration
available_flights = [
    {"flight_id": 1, "airline": "Sample Airlines", "destination": "New York", "price": 300},
    {"flight_id": 2, "airline": "Travel Airways", "destination": "Los Angeles", "price": 400},
]

available_hotels = [
    {"hotel_id": 1, "name": "Sample Hotel", "location": "New York", "price_per_night": 150},
    {"hotel_id": 2, "name": "Hotel Paradise", "location": "Los Angeles", "price_per_night": 200},
]


@books_bp.route('/flights')
def list_flights():
    return render_template('flights.html', flights=available_flights)

@books_bp.route('/hotels')
def list_hotels():
    return render_template('hotels.html', hotels=available_hotels)

@books_bp.route('/book/flight/<int:flight_id>')
def book_flight(flight_id):
    flight = next((f for f in available_flights if f["flight_id"] == flight_id), None)
    if not flight:
        return 'Flight not found', 404

    return f'Booking flight with {flight["airline"]} to {flight["destination"]} for ${flight["price"]}. Payment processing would go here.'

@books_bp.route('/book/hotel/<int:hotel_id>')
def book_hotel(hotel_id):
    hotel = next((h for h in available_hotels if h["hotel_id"] == hotel_id), None)
    if not hotel:
        return 'Hotel not found', 404

    return f'Booking a room at {hotel["name"]} in {hotel["location"]} for ${hotel["price_per_night"]} per night. Payment processing would go here.'