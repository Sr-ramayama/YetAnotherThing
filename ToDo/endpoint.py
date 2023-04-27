from flask import Flask, jsonify, request

app = Flask(__name__)

places = [
    { 'Type': 'bar', 'Location': 'Calle Cum', 'Style': 'Indian' }
]


@app.route('/places')
def get_places():
    return jsonify(places)


@app.route('/places', methods=['POST'])
def add_income():
    places.append(request.get_json())
    return '', 204