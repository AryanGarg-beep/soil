import serial
import time
import matplotlib.pyplot as plt
from collections import deque

# Set up the serial connection (adjust 'COM3' and baudrate as needed)
ser = serial.Serial('/dev/ttyUSB0', 11500)  # Use the correct port for your Arduino
time.sleep(2)  # Give the connection a second to settle

# Create lists to store sensor data and ppm values
sensor_data = deque(maxlen=100)  # Keep the last 100 readings
ppm_data = deque(maxlen=100)      # Keep the last 100 readings

plt.ion()  # Enable interactive mode
fig, axs = plt.subplots(2, 1, figsize=(10, 5))

# Set titles and labels for the plots
axs[0].set_title('Sensor Data')
axs[0].set_ylabel('Sensor Data (Analog Value)')
axs[1].set_title('Gas Concentration in ppm')
axs[1].set_ylabel('Concentration (ppm)')
axs[1].set_xlabel('Samples')

try:
    while True:
        if ser.in_waiting > 0:  # Check if data is available
            line = ser.readline().decode('utf-8').rstrip()  # Read a line from serial
            data = line.split(',')  # Split the line into sensor data and concentration
            
            # Ensure we have two values
            if len(data) == 2:
                sensor_value = float(data[0])  # Convert sensor data to float
                ppm_value = float(data[1])      # Convert ppm value to float

                # Append data to the deque
                sensor_data.append(sensor_value)
                ppm_data.append(ppm_value)

                # Clear the current plots
                axs[0].cla()
                axs[1].cla()

                # Plot sensor data
                axs[0].plot(sensor_data, color='blue')
                axs[0].set_title('Sensor Data')
                axs[0].set_ylabel('Sensor Data (Analog Value)')

                # Plot ppm concentration
                axs[1].plot(ppm_data, color='red')
                axs[1].set_title('Gas Concentration in ppm')
                axs[1].set_ylabel('Concentration (ppm)')
                axs[1].set_xlabel('Samples')

                # Refresh the plots
                plt.pause(0.1)  # Short pause to update the plot
except KeyboardInterrupt:
    print("Logging stopped.")
finally:
    ser.close()  # Close the serial connection
