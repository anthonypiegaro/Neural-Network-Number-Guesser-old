import numpy as np
import pandas as pd
import random
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score

from keras.models import Sequential, model_from_json
from keras.layers import Conv2D, Dense, Flatten, MaxPooling2D
from keras.optimizers import SGD
from keras.utils import to_categorical
from keras.datasets import mnist


# Getting MNIST data
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
# load weights into new model
model.load_weights("model.h5")
print("Loaded model from disk")



# predictions = np.argmax(model.predict(X_test), axis=-1)
# score = accuracy_score(y_test, predictions)
# print(score)