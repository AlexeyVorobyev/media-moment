from keras.api.models import Model

from mlp import x_test, y_test, create_model


def evaluate_model(model: Model, x_test, y_test):
    model.evaluate(x_test, y_test, verbose=1)


if __name__ == '__main__':

    weights = [
        "5-mlp-1-512.weights.h5",
        "5-mlp-2-512.weights.h5",
        "5-mlp-5-512.weights.h5",
        "5-mlp-20-512.weights.h5",
        "5-mlp-50-512.weights.h5",
        "5-mlp-100-512.weights.h5",
        "5-mlp-500-512.weights.h5"
    ]

    for weight in weights:
        model = create_model()
        model.load_weights(weight)
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        evaluate_model(model, x_test, y_test)
