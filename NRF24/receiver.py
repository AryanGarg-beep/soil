from RF24 import RF24, RF24_PA_LOW
import time

# Configure the radio and GPIO
radio = RF24(22, 0)  # CE on GPIO 22, CSN on SPI CE0 (GPIO 8)

# Set up the address for the transmitter and receiver
address = b"1Node"
radio.openReadingPipe(1, address)
radio.setPALevel(RF24_PA_LOW)  # Set power level

# Initialize radio to start listening
radio.startListening()

# Main loop to receive data
try:
    while True:
        if radio.available():
            received_message = radio.read(32).decode('utf-8')
            print("Received message:", received_message)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Reception stopped")
