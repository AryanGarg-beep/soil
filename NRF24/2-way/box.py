from RF24 import RF24, RF24_PA_LOW
import time

# Initialize radio on CE (GPIO 22) and CSN (SPI CE0 - GPIO 8)
radio = RF24(22, 0)

# Addresses for each device
address_tx = b"2Node"  # Transmit address
address_rx = b"1Node"  # Receive address

# Setup radio configurations
radio.openWritingPipe(address_tx)    # Open the transmit address
radio.openReadingPipe(1, address_rx) # Open the receive address
radio.setPALevel(RF24_PA_LOW)

# Switch to listening mode
radio.startListening()

while True:
    if radio.available():
        # Receive message
        received_message = radio.read(32).decode('utf-8')
        print("Device 2 received:", received_message)

        # Stop listening, send response, then return to listening
        radio.stopListening()
        response = "Acknowledged by Device 2"
        radio.write(response.encode('utf-8'))
        print("Device 2 sent:", response)
        radio.startListening()
    
    time.sleep(1)
