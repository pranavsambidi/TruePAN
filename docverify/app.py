from flask import Flask, render_template, request, redirect, url_for, session
import shutil
import cv2
from ultralytics import YOLO
import easyocr
import tensorflow as tf
import numpy as np
import os
from keras.models import load_model
import keras.losses
import uuid

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Needed for session

custom_objects = {"BinaryCrossentropy": keras.losses.BinaryCrossentropy}
new_model = load_model("logoClassifier.h5", compile=False, custom_objects=custom_objects)
new_model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
model = YOLO("best.pt")

@app.route('/')
def index():
    result_message = session.pop('result_message', None)
    show_image = session.pop('show_image', False)
    cache_buster = str(uuid.uuid4())
    return render_template('index.html', result_message=result_message, show_image=show_image, cache_buster=cache_buster)

@app.route('/process_image', methods=['POST'])
def process_image():
    try:
        image_path = "static/image/user_upload.jpg"
        if os.path.exists(image_path):
            os.remove(image_path)

        upload_folder = "uploads"
        os.makedirs(upload_folder, exist_ok=True)
        upload_path = os.path.join(upload_folder, "user_upload.jpg")

        file = request.files["image"]
        file.save(upload_path)

        folder_path = "runs"
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)

        model.predict(upload_path, save=True, save_crop=True)

        reader = easyocr.Reader(lang_list=["en"])
        it_crop_path = r"runs/detect/predict/crops/IT/user_upload.jpg"
        recognized_text = "Text not recognized"
        if os.path.exists(it_crop_path):
            text = reader.readtext(it_crop_path)
            recognized_text = text[0][1] if text else "Text not recognized"

        logoID = -1
        logo_crop_path = r"runs/detect/predict/crops/Logo/user_upload.jpg"
        if os.path.exists(logo_crop_path):
            img = cv2.imread(logo_crop_path)
            resize = tf.image.resize(img, (256, 256))
            predict = new_model.predict(np.expand_dims(resize / 255, 0))
            logoID = -1 if predict > 0.5 else 1

        result_message = "Valid Document" if recognized_text == "INCOME TAX DEPARTMENT" and logoID == 1 else "Invalid Document"

        shutil.move(upload_path, "static/image/user_upload.jpg")

        # Save result to session and redirect
        session['result_message'] = result_message
        session['show_image'] = True

        return redirect(url_for('index'))

    except Exception as e:
        session['result_message'] = f"Error: {str(e)}"
        session['show_image'] = False
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7860, debug=True)

