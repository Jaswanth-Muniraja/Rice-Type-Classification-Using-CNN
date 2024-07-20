import tensorflow as tf
import tensorflow_hub as hub 
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import os
from flask import Flask, request, render_template

import cv2

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == "POST":
        f = request.files['image']
        basepath = os.path.dirname(__file__)  # getting the current path i.e where app.py is present
        filepath = os.path.join(basepath, 'uploads', f.filename)  # path to save the file
        f.save(filepath)

        # Load and preprocess the image
        img = cv2.imread(filepath)
        img = cv2.resize(img, (224, 224))
        img = np.array(img)
        img = img / 255.0
        img = np.expand_dims(img, axis=0)

        # Load the pre-trained model
        model = tf.keras.models.load_model('rice.h5', custom_objects={'KerasLayer': hub.KerasLayer})

        # Add the code from the previous response
        # Load the TensorFlow Hub module
        module_url = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4"
        feature_extractor = tf.keras.Sequential([
            hub.KerasLayer(module_url, input_shape=(224, 224, 3), trainable=False)
        ])

        # Build the final model
        model = tf.keras.Sequential([
            feature_extractor,
            tf.keras.layers.Dense(num_classes, activation='softmax')
        ])

        # Predict
        pred = model.predict(img)
        pred = pred.argmax()

        labels = ['Arborio', 'Basmati', 'Ipsala', 'Jasmine', 'Karacadag']
        prediction = labels[pred]

        return render_template('index.html', prediction=prediction)

if __name__ == "__main__":
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)