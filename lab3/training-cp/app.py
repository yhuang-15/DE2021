import os

import pandas as pd
import requests
from flask import Flask, Response

from resources import model_trainer

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/training-cp/model', methods=['POST'])
def train_models():
    db_api = os.environ['TRAININGDB_API']
    # Make a GET request to training db service to retrieve the training data/features.
    r = requests.get(db_api)
    j = r.json()
    df = pd.DataFrame.from_dict(j)
    js = model_trainer.train(df.values)
    from flask import jsonify
    resp = Response(jsonify(js), status=200, mimetype='application/json')
    return resp


app.run(host='0.0.0.0', port=5000)
