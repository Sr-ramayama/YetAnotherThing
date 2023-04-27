from flask import Flask, jsonify, request

app = Flask(__name__)

places = [
    { 'Type': 'bar', 'Location': 'Calle Cum', 'Style': 'Indian' }
]


@app.route('/places')
def get_places():
    return jsonify(places)

@app.route('/places/eat')
def get_bares():
    response = {}
    for key,value in places.item():
        if value == 'bar':
            response.append({key:value})
    return response
@app.route('/places', methods=['POST'])
def add_places():
    places.append(request.get_json())
    return '', 204