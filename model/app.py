from flask import Flask, request, jsonify
import pickle
import numpy as np

from flask_cors import CORS  

app = Flask(__name__)
CORS(app)  


with open('model.pkl', 'rb') as file:
    regressor = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    square_footage = np.array([[data['square_footage']]])
    predicted_price = regressor.predict(square_footage)[0]
    return jsonify({'predicted_price': f"₹{(predicted_price*23.8):,.2f}"})

if __name__ == '__main__':
    app.run(debug=True)
