from imports import *
import createDataset as createDataset

import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Conv1D
from tensorflow.keras.layers import MaxPooling1D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import InputLayer

# Multi-head neural network optimizer
# to predict the Modified-SEIR model parameters
def createModel(realDailyDeaths, predictedDailyDeaths, theta):
    model = Sequential()

    # TODO: Create model layers

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['acc'])

    return model