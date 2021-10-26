from flask import Flask, request, jsonify, render_template
from flask_cors import cross_origin
import json
import pickle
import numpy as np

app = Flask(__name__)



locations = None
data_column = None
model = None

def load_saved_artifacts():
    print('Loading saved artifacts.......START')
    global locations
    global data_column
    global model

    with open('./artifacts/columns.json', 'r') as f:
        data_column = json.load(f)['data_columns']
        locations = data_column[3:]

    with open('./artifacts/bangalore_price_prediction.pickle', 'rb') as f:
        model = pickle.load(f)
    print('Loading saved artifacts.......DONE')

def get_estimated_price(location, sqft, bath, bhk):
    try:
        location_index = data_column.index(location.lower())
    except:
        location_index = -1

    x = np.zeros(len(data_column))  # It gives an nd array of all zeros
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if location_index >= 0:
        x[location_index] = 1

    return round(model.predict([x])[0], 2)


def get_location_names():
    load_saved_artifacts()
    return locations





@app.route("/")
@cross_origin()
def home():
    return render_template('index.html')


@app.route('/get_location_names', methods=['GET'])
def get_location_names1():
    response = jsonify({
        'locations': get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
 

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form.get('sqft'))
    location = request.form.get('loc')
    bhk = int(request.form.get('bhk'))
    bath = int(request.form.get('bath'))
    response = str(get_estimated_price(location, total_sqft, bath, bhk))
    #response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    #return render_template('index.html', prediction_value= str(response) + " Lakhs")




if __name__ == "__main__":
    print('Starting python flask server for home price prediction..')
    load_saved_artifacts()
    app.run(debug=True)
