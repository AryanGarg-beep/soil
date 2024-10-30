import serial
import time

# Set up the serial connection (adjust 'COM3' or '/dev/ttyUSB0' as needed)
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Adjust for your actual port

try:
    while True:
        # Send a message
        message = "Hello, Arduino"
        ser.write(message.encode('utf-8'))
        print(f"Sent: {message}")
        
        # Wait for response
        time.sleep(1)
        
        # Read response from Arduino
        if ser.in_waiting > 0:
            response = ser.readline().decode('utf-8').strip()
            print(f"Arduino responded: {response}")
            
        time.sleep(1)  # Add delay to control message frequency

except KeyboardInterrupt:
    print("Program interrupted")

finally:
    ser.close()
