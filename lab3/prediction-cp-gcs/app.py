import pandas as pd
from flask import Flask, json, request

from resources.predictor import DiabetesPredictor

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/diabetes_predictor', methods=['PUT'])
def refresh_model():
    return dp.download_model()


@app.route('/prediction-cp/results', methods=['POST'])
def predict():
    # receive the prediction request data as the message body
    content = request.get_json()
    df = pd.read_json(json.dumps(content), orient='records')
    return dp.predict(df)


dp = DiabetesPredictor()

app.run(host='0.0.0.0', port=5000)
