import logging

import keras
from keras.api.datasets import mnist
from keras.api.utils import to_categorical

from utils.timer import Timer
from mlp import train_model, height, width, depth, num_classes

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(x_train.shape[0], height, width, depth)
x_train = x_train.astype('float32')
x_train /= 255

x_test = x_test.reshape(x_test.shape[0], height, width, depth)
x_test = x_test.astype('float32')
x_test /= 255

y_train = to_categorical(y_train, num_classes=num_classes)
y_test = to_categorical(y_test, num_classes=num_classes)

batch_size = 32
num_epochs = 100


def create_cnn_model():
    model = keras.Sequential()
    model.add(keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(width, height, depth)))
    model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(128, activation='relu'))
    model.add(keras.layers.Dropout(0.3))
    model.add(keras.layers.Dense(num_classes, activation='softmax'))

    return model


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    model = create_cnn_model()
    with Timer():
        train_model(model, x_train, y_train, batch_size, num_epochs, x_test, y_test, name='cnn')
