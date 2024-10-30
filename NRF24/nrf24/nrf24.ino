#include <SPI.h>
#include <RF24.h>

// nRF24L01 pins
#define CE_PIN 9
#define CSN_PIN 10

// Initialize the radio object
RF24 radio(CE_PIN, CSN_PIN);

// Define address for communication
const byte address[6] = "00001";

void setup() {
    Serial.begin(9600);
    radio.begin();
    radio.openReadingPipe(0, address); // Set the same address for both devices
    radio.setPALevel(RF24_PA_LOW);     // Power level to low
    radio.startListening();
}

void loop() {
    if (radio.available()) {
        char text[32] = {0};
        radio.read(&text, sizeof(text));
        
        Serial.print("Received: ");
        Serial.println(text);
        
        // Sending acknowledgment
        radio.stopListening();                // Stop listening to send response
        radio.write("Ack: ", strlen("Ack: ")); // Respond with acknowledgment
        radio.startListening();                // Switch back to listening mode
    }
}
