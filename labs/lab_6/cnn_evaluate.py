from keras.api.models import Model

from cnn import x_test, y_test, create_cnn_model, Timer


def evaluate_model(model: Model, x_test, y_test):
    model.evaluate(x_test, y_test, verbose=1)


if __name__ == '__main__':

    weights = [
        "6-cnn-1-512.weights.h5",
        "6-cnn-2-512.weights.h5",
        "6-cnn-5-512.weights.h5",
        "6-cnn-20-512.weights.h5",
        "6-cnn-50-512.weights.h5",
        "6-cnn-100-512.weights.h5",
        # "5-cnn-500-512.weights.h5"
    ]

    for weight in weights:
        model = create_cnn_model()
        model.load_weights(weight)
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        with Timer():
            evaluate_model(model, x_test, y_test)
