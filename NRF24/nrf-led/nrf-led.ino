#include <SPI.h>
#include <RF24.h>

// nRF24L01 pins
#define CE_PIN 9
#define CSN_PIN 10

// LED pin
#define LED_PIN 7

// Initialize the radio object
RF24 radio(CE_PIN, CSN_PIN);

// Define address for communication
const byte address[6] = "00001";

void setup() {
    Serial.begin(9600);
    pinMode(LED_PIN, OUTPUT);   // Set LED pin as output
    digitalWrite(LED_PIN, LOW); // Start with LED off

    radio.begin();
    radio.openReadingPipe(0, address); // Set the same address for both devices
    radio.setPALevel(RF24_PA_LOW);     // Power level to low
    radio.startListening();
}

void loop() {
    if (radio.available()) {
        char text[32] = {0};
        radio.read(&text, sizeof(text));
        
        Serial.print("Received command: ");
        Serial.println(text);
        
        // Control LED based on received command
        if (strcmp(text, "ON") == 0) {
            digitalWrite(LED_PIN, HIGH); // Turn LED on
            Serial.println("LED turned ON");
        } else if (strcmp(text, "OFF") == 0) {
            digitalWrite(LED_PIN, LOW);  // Turn LED off
            Serial.println("LED turned OFF");
        }
    }
}
