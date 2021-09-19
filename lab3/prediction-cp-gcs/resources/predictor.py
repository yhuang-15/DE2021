import os

from flask import jsonify
from google.cloud import storage
from keras.models import load_model


class DiabetesPredictor:
    def __init__(self):
        self.model = None

    # download the model
    def download_model(self):
        project_id = os.environ.get('PROJECT_ID', 'Specified environment variable is not set.')
        model_repo = os.environ.get('MODEL_REPO', 'Specified environment variable is not set.')
        client = storage.Client(project=project_id)
        bucket = client.get_bucket(model_repo)
        model_file_name = 'model.h5'
        blob = bucket.blob(model_file_name)
        blob.download_to_filename(model_file_name)
        self.model = load_model(model_file_name)

    # make prediction
    def predict(self, dataset):
        if self.model is None:
            self.download_model()
        val_set2 = dataset.copy()
        result = self.model.predict(dataset)
        y_classes = result.argmax(axis=-1)
        val_set2['class'] = y_classes.tolist()
        dic = val_set2.to_dict(orient='records')
        return jsonify(dic), 200
