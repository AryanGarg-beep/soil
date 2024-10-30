import serial
import time

# Set up the serial connection (adjust '/dev/ttyUSB0' or 'COM3' as needed)
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Adjust for your actual port

def send_command(command):
    if command in ["ON", "OFF"]:
        ser.write(command.encode('utf-8'))
        print(f"Sent: {command}")
    else:
        print("Invalid command. Use 'ON' or 'OFF'.")

try:
    while True:
        # Get command from user
        command = input("Enter command (ON/OFF): ").strip().upper()
        
        # Send command
        send_command(command)
        
        # Wait for a moment to ensure the command is processed
        time.sleep(1)

except KeyboardInterrupt:
    print("Program interrupted")

finally:
    ser.close()
