import os
import cv2
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

# Constants
NUM_CATEGORIES = 43
IMG_WIDTH = 30
IMG_HEIGHT = 30
EPOCHS = 10
TEST_SIZE = 0.4


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.
    Return tuple `(images, labels)`.
    `images` should be a list of all of the images in the data set,
    where each image is formatted as a numpy.ndarray with dimensions (IMG_WIDTH, IMG_HEIGHT, 3).
    `labels` should be a list of integer labels, representing the categories.
    """
    images = []
    labels = []

    # Loop through each category directory
    for label in range(NUM_CATEGORIES):
        label_dir = os.path.join(data_dir, str(label))
        for filename in os.listdir(label_dir):
            if filename.endswith(".ppm"):
                img_path = os.path.join(label_dir, filename)
                img = cv2.imread(img_path)
                img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
                images.append(img)
                labels.append(label)

    return images, labels


def get_model():
    """
    Returns a compiled convolutional neural network model.
    Input shape: (IMG_WIDTH, IMG_HEIGHT, 3)
    Output layer: NUM_CATEGORIES units, softmax activation.
    """
    model = tf.keras.models.Sequential([
        # Convolutional layer
        tf.keras.layers.Conv2D(
            32, (3, 3), activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
        ),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

        # Second convolutional layer
        tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

        # Flatten and dense layers
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dropout(0.5),

        # Output layer
        tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
    ])

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )
    return model


def main():
    import sys
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Load data
    images, labels = load_data(sys.argv[1])
    images = np.array(images)
    labels = np.array(labels)

    # Split into training and testing
    x_train, x_test, y_train, y_test = train_test_split(
        images, labels, test_size=TEST_SIZE
    )

    # Get and train model
    model = get_model()
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate model
    model.evaluate(x_test, y_test, verbose=2)

    # Save model if specified
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}")


if __name__ == "__main__":
    main()
