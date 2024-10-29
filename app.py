import serial
import json
import time
from flask import Flask, jsonify, render_template
import cv2

app = Flask(__name__)

# Serial connection setup
try:
    ser = serial.Serial('/dev/ttyUSB0', 9600)  # Update with your serial port if needed
except serial.SerialException as e:
    ser = None
    print(f"Error opening serial port: {e}")

cap = cv2.VideoCapture()
# Store sensor values globally
sensor_values = []

def generate_frames():
    while True:
        success, frame = cap.read()  # Capture frame-by-frame
        if not success:
            break
        else:
            # Encode the frame in JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()  # Convert the frame to bytes

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # Yield the frame

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
#@app.route('/sensor-data')
#def get_sensor_data():
#    if ser and ser.in_waiting > 0:
#        sensor_value = ser.readline().decode('utf-8').strip()  # Read data from Arduino
#        sensor_values.append(float(sensor_value))  # Store the value
#        return jsonify({'sensor_value': sensor_value, 'sensor_values': sensor_values})
#    else:
#        return jsonify({'error': 'No data available'}), 503

@app.route('/camera')
def camera_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    #return render_template('camera_feed.html')


# Serve the results page
@app.route('/results')
def results():
    return render_template('results.html', data=sensor_values)  # Pass data to results page

if __name__ == '__main__':
    try:
        app.run(debug=True, host='0.0.0.0')
    finally:
        cap.release()  # Release the webcam when done
        if ser:
            ser.close()  # Close the serial connection if opened

    
