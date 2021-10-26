import json
import pickle
import numpy as np

locations = None
data_column = None
model = None


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


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st block jayanagar', 1000, 3, 3))
    print(get_estimated_price('1st phase jp nagar', 1000, 3, 3))
