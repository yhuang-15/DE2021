# MLP for Pima Indians Dataset saved to single file
# see https://machinelearningmastery.com/save-load-keras-deep-learning-models/
import logging
import os

from flask import jsonify
from google.cloud import storage
from keras.layers import Dense
from keras.models import Sequential


def train(dataset):
    # split into input (X) and output (Y) variables
    X = dataset[:, 0:8]
    Y = dataset[:, 8]
    # define model
    model = Sequential()
    model.add(Dense(12, input_dim=8, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    # compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # Fit the model
    model.fit(X, Y, epochs=150, batch_size=10, verbose=0)
    # evaluate the model
    scores = model.evaluate(X, Y, verbose=0)
    print(model.metrics_names)
    text_out = {
        "accuracy:": scores[1],
        "loss": scores[0],
    }
    # Saving model in a given location provided as an env. variable
    project_id = os.environ.get('PROJECT_ID', 'Specified environment variable is not set.')
    model_repo = os.environ.get('MODEL_REPO', 'Specified environment variable is not set.')
    if model_repo:
        # Save the model localy
        model.save('local_model.h5')
        # Save to GCS as model.h5
        client = storage.Client(project=project_id)
        bucket = client.get_bucket(model_repo)
        blob = bucket.blob('model.h5')
        # Upload the locally saved model
        blob.upload_from_filename('local_model.h5')
        # Clean up
        os.remove('local_model.h5')
        logging.info("Saved the model to GCP bucket : " + model_repo)
        return jsonify(text_out), 200
    else:
        model.save("model.h5")
        return jsonify({'message': 'The model was saved locally.'}), 200
