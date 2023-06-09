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
    response = [{}]
    for el in places:
        for key,value in el.items():
            if value.lower() == 'bar':
                response.append(el)
    response = list(filter(None,response))
    return jsonify(response)

@app.route('/places', methods=['POST'])
def add_places():
    places.append(request.get_json())
    return '', 204