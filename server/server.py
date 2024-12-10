from flask import Flask, request, jsonify
from flask_cors import CORS
import util
app = Flask(__name__)
CORS(app)
util.load_saved_artifacts()

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add("Access-Control-Allow-Origin",'*')
    return response

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    total_sqrt = float(request.form['total_sqrt'])
    location = request.form['location']
    bhk = request.form['bhk']
    bath = request.form['bath']

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqrt,bhk,bath)
    })
    response.headers.add("Access-Control-Allow-Origin", '*')
    return  response
if __name__ == "__main__":
    print("staring server")
    app.run(debug=True)

