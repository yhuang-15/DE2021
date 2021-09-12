import pandas as pd
from flask import Flask, json, request, Response, jsonify

from resources import predictor

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/prediction-cp/results', methods=['POST'])
def predict_perf():
    # receive the prediction request data as the message body
    content = request.get_json()
    df = pd.read_json(json.dumps(content), orient='records')
    js = predictor.predict(df)
    resp = Response(jsonify(js), status=200, mimetype='application/json')
    return resp


app.run(host='0.0.0.0', port=5000)
