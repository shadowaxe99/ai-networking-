
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder

class AIAgent:
    def __init__(self):
        self.model = keras.models.Sequential()
        self.encoder = LabelEncoder()

    def train(self, X, y):
        X = self.encoder.fit_transform(X)
        y = self.encoder.fit_transform(y)
        self.model.add(keras.layers.Dense(64, activation='relu', input_shape=(X.shape[1],)))
        self.model.add(keras.layers.Dense(64, activation='relu'))
        self.model.add(keras.layers.Dense(1, activation='sigmoid'))
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        self.model.fit(X, y, epochs=10, batch_size=32)

    def predict(self, X):
        X = self.encoder.transform(X)
        return self.model.predict(X)
