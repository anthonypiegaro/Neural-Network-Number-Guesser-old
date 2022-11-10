import numpy as np
import random
import tensorflow as tf

from flask import Flask, render_template, request, jsonify, make_response
from keras.models import Sequential, model_from_json
from keras.layers import Conv2D, Dense, Flatten, MaxPooling2D
from keras.optimizers import SGD
from keras.utils import to_categorical
from keras.datasets import mnist

# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
# load weights into new model
model.load_weights("model.h5")
print("Loaded model from disk")

app = Flask(__name__)

@app.route("/")
def hello_world():
     return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict_number():
    data = request.get_json()

    array = np.array(data["data"])

    digit = np.argmax(model.predict(array.reshape((1, 28, 28, 1)))[0], axis=-1)

    res = make_response(jsonify({"message": str(digit)}), 200)

    return res