import Adafruit_DHT
import RPi.GPIO as GPIO
import json
from flask import Flask, jsonify, render_template
import time
import cv2

app = Flask(__name__)

# DHT11 Setup
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # GPIO pin connected to DHT11 data pin

# Gas Sensor Setup (digital threshold)
GAS_SENSOR_PIN = 17  # Connect digital pin of gas sensor to GPIO 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(GAS_SENSOR_PIN, GPIO.IN)

#camera
cap = cv2.VideoCapture(0)
last_frame = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/database')
def database():
    return render_template('database.html')  # Ensure you have this template

# Serve experiment page
@app.route('/experiment')
def experiment():
    return render_template('experiment.html')

@app.route('/humidity')
def humidity():
    return render_template('humidity.html')

@app.route('/gas')
def gas():
    return render_template('gas.html')

# Endpoint to retrieve sensor data
@app.route('/sensor-data')
def sensor_data():
    # Read DHT11 sensor data
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    # Read gas sensor digital threshold
    gas_detected = GPIO.input(GAS_SENSOR_PIN)

    if humidity is not None and temperature is not None:
        data = {
            'temperature': temperature,
            'humidity': humidity,
            'gas': "Detected" if gas_detected else "Not Detected"
        }
    else:
        data = {'error': 'Failed to read from DHT11 sensor'}

    return jsonify(data)

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def gen_frames():
    global last_frame
    while True:
        success, frame = cap.read()  # Read a frame from the camera
        if not success:
            break
        else:
            last_frame = frame  # Store the last frame for processing
            # Encode the frame in JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # Send frame in byte format


@app.route('/get_rgb/<int:x>/<int:y>')
def get_rgb(x, y):
    global last_frame
    if last_frame is not None:
        # Get the BGR values at the specified coordinates
        b, g, r = last_frame[y, x]
        # Convert to RGB format
        rgb = (r, g, b)
        return jsonify({'coordinates': (x, y), 'rgb': rgb})
    return jsonify({'error': 'No image available'}), 400


@app.route('/results')
def results():
    return render_template('results.html', data=sensor_values)

if __name__ == '__main__':
    try:
        app.run(debug=True, host='0.0.0.0')
    finally:
        GPIO.cleanup()
        cap.release()
