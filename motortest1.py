import time
from unittest.mock import MagicMock

# Simulate serial.Serial class with a mock
serial = MagicMock()

# Mock serial.Serial object to capture and print sent data
class MockSerial:
    def __init__(self, port, baudrate, timeout):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.commands = []

    def write(self, data):
        # Simulate writing data to the serial port
        command = data[0]
        self.commands.append(command)
        bcommand = bin(command)
        print(f"Command is {bcommand}")
        if command == 64:
            print("Motor stopped.")
        elif 1<=command<64:
            print(f"Motor running forward at speed {command}({bcommand}).")
        else:
            print(f"Motor running backward at speed {command}({bcommand}).")
        
    def close(self):
        print("Serial connection closed.")

# Replace the serial.Serial class with MockSerial
serial.Serial = MockSerial

# Function to set motor speed based on user input
def set_motor_speed(motor, speed):
    """
    Sends a command to the simulated Sabertooth to control the motor speed.
    
    motor: 1 or 2 (for motor 1 or motor 2)
    speed: 0-127 for forward, 128-255 for reverse.
    Example: 64 is half-speed forward, 192 is half-speed backward.
    """
    if motor == 1:
        command = speed
    
    ser.write(bytes([command]))
    # Simulate sending a command to Sabertooth

# Simulated serial object
ser = serial.Serial('COM3', 9600, timeout=1)  # Simulated port

# Loop to take user input for motor speed
try:
    while True:
        user_input = input("Enter motor speed (1-63 is reverse, 65-127 is forward, or 'stop' to stop the motor, 'exit' to quit): ").strip()
        
        if user_input.lower() == 'exit':
            break  # Exit the program
        elif user_input.lower() == 'stop':
            set_motor_speed(1, 64)  # 128 stops the motor
        else:
            try:
                speed = int(user_input)
                if 1 <= speed <= 127:
                    if speed >= 0:
                        set_motor_speed(1, speed)  # Forward speed
                    else:
                        set_motor_speed(1, speed)  # Reverse speed
                else:
                    print("Please enter a speed between 1 and 127.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 127, or 'stop' to stop the motor.")
finally:
    set_motor_speed(1, 128)  # Stop the motor before exiting
    ser.close()              # Simulate closing the serial connection

