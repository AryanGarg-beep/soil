from RF24 import RF24, RF24_PA_LOW
import time

# Configure the radio and GPIO
radio = RF24(22, 0)  # CE on GPIO 22, CSN on SPI CE0 (GPIO 8)

# Set up the address for the transmitter and receiver
address = b"1Node"
radio.openWritingPipe(address)
radio.setPALevel(RF24_PA_LOW)  # Set power level

# Function to send a message
def send_message(message):
    radio.write(message.encode('utf-8'))

# Initialize radio
radio.stopListening()

# Main loop to send data
try:
    while True:
        send_message("Hello from Raspberry Pi!")
        print("Message sent")
        time.sleep(1)
except KeyboardInterrupt:
    print("Transmission stopped")
