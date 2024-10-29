#include <DHT.h>

#define DHTPIN 2     // Pin to which DHT11 is connected
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  // Wait a few seconds between measurements.
  delay(2000);

  // Reading temperature or humidity takes about 250 milliseconds
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  // Check if any reads failed
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Send JSON formatted data
  Serial.print("{\"temperature\":");
  Serial.print(temperature);
  Serial.print(", \"humidity\":");
  Serial.print(humidity);
  Serial.println("}");
}
