import serial
import json
import time
import Adafruit_DHT
import RPi.GPIO as GPIO
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# DHT11 Setup
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # GPIO pin connected to DHT11 data pin

# Gas Sensor Setup (digital threshold)
GAS_SENSOR_PIN = 17  # Connect digital pin of gas sensor to GPIO 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(GAS_SENSOR_PIN, GPIO.IN)

# Serial connection setup

try:
    ser = serial.Serial('/dev/ttyUSB0', 9600)  # Update with your serial port if needed
except serial.SerialException as e:
    ser = None
    print(f"Error opening serial port: {e}")

# Store sensor values globally
sensor_values = []

# Serve the main page (index)
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

@app.route('/sensor-data')
def get_sensor_data():
    if ser and ser.in_waiting > 0:
        sensor_value = ser.readline().decode('utf-8').strip()  # Read data from Arduino
        
        # Ensure we get a well-formed JSON
        try:
            data = json.loads(sensor_value)  # Parse JSON
            temperature = data['temperature']  # Get temperature value
            humidity = data['humidity']        # Get humidity value
            sensor_values.append((temperature, humidity))  # Store the value
            return jsonify({'sensor_value': data})  # Return JSON response
        except json.JSONDecodeError:
            return jsonify({'error': 'Failed to decode JSON data'}), 400
        except KeyError:
            return jsonify({'error': 'Invalid data format'}), 400
    else:
        return jsonify({'error': 'No data available'}), 503

# Serve gas sensor page and read sensor data
@app.route('/gas')
def gas_test():
    return render_template('gas.html')

# Retrieve sensor data
@app.route('/sensor-data')
def get_sensor_data():
    if ser and ser.in_waiting > 0:
        sensor_value = ser.readline().decode('utf-8').strip()  # Read data from Arduino
        sensor_values.append(float(sensor_value))  # Store the value
        return jsonify({'sensor_value': sensor_value, 'sensor_values': sensor_values})
    else:
        return jsonify({'error': 'No data available'}), 503

# Serve the results page
@app.route('/results')
def results():
    return render_template('results.html', data=sensor_values)  # Pass data to results page

if __name__ == '__main__':
    app.run(debug=True)
