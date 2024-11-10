from flask import Flask, render_template, Response, jsonify
import cv2
import numpy as np
import time
import os

app = Flask(__name__)
cap = cv2.VideoCapture(0)  # Laptop webcam

def analyze_spectrum(frame):
    # Define a region of interest (ROI) for analysis (customize as needed)
    roi = frame[100:400, 200:600]
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    hue_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])  # Hue histogram

    # Map hues to wavelengths (rough estimate for visible light spectrum)
    wavelengths = np.linspace(400, 700, 180)  # From 400nm to 700nm
    intensities = hue_hist.flatten()  # Flatten histogram to use as intensity values
    return wavelengths.tolist(), intensities.tolist()

def generate_camera_feed():
    while True:
        success, frame = cap.read()
        if not success:
            break
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_camera_feed(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/spectrum_data')
def spectrum_data():
    success, frame = cap.read()
    if success:
        wavelengths, intensities = analyze_spectrum(frame)
        return jsonify({"wavelengths": wavelengths, "intensities": intensities})
    return jsonify({"error": "Failed to capture frame"}), 500

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
