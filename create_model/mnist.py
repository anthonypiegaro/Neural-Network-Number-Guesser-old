import numpy as np
import pandas as pd
import random
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score

from keras.models import Sequential
from keras.layers import Conv2D, Dense, Flatten, MaxPooling2D
from keras.optimizers import SGD
from keras.utils import to_categorical
from keras.datasets import mnist


# Getting MNIST data
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Scaling the data, 0 to 1
X_train = (X_train - 0.0) / (255.0 - 0.0)
X_test = (X_test - 0.0) / (255.0 - 0.0)

# Transform data to add number of channels, in this case 1
X_train = X_train.reshape((X_train.shape + (1,)))
X_test = X_test.reshape((X_test.shape + (1,)))

# We are leaving our target data as they are, which are digits
# ranging from 0 to 9, thus we will use Sparse Categorical Cross-Entropy
# for the loss function

def plot_digit(image, digit, plt, i):
    plt.subplot(4, 5, i + 1)
    plt.imshow(image, cmap=plt.get_cmap('gray'))
    plt.title(f"Digit: {digit}")
    plt.xticks([])
    plt.yticks([])

# Building the model
model = Sequential([
    Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(100, activation="relu"),
    Dense(10, activation="softmax")
])

# Define how we will train the model
optimizer = SGD(learning_rate=0.01, momentum=0.9)
model.compile(
    optimizer=optimizer,
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)
model.summary()

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")

# # Checking on some test data
# plt.figure(figsize=(16, 10))
# for i in range(20):
#     image = random.choice(X_test).squeeze()
#     digit = np.argmax(model.predict(image.reshape((1, 28, 28, 1)))[0], axis=-1)
#     plot_digit(image, digit, plt, i)

# plt.show()

# # Testing on test data
# predictions = np.argmax(model.predict(X_test), axis=-1)
# accuracy_score(y_test, predictions)