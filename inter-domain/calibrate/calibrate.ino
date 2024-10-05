// Define pins and constants
const int sensorPin = A0;  // Analog pin where the MQ8 sensor is connected
const float V_supply = 5.0; // Supply voltage to the MQ8 sensor (5V)
const float R_L = 10000.0;  // Load resistance in ohms (10kΩ)

// Function to read and convert the ADC value to voltage
float readSensorVoltage() {
  int sensorValue = analogRead(sensorPin);  // Read the analog value (ADC value)
  float voltage = (sensorValue / 4095.0) * 3.3;  // Convert to voltage (for 12-bit ADC, 3.3V reference)
  return voltage;
}

// Function to calculate the sensor resistance (Rs)
float calculateSensorResistance(float voltage) {
  // Rs = R_L * (V_supply - V_out) / V_out
  float Rs = R_L * (V_supply - voltage) / voltage;
  return Rs;
}

void setup() {
  Serial.begin(9600);  // Start serial communication
  delay(2000);  // Allow some time for the serial monitor to open
}

void loop() {
  // Step 1: Read sensor voltage
  float sensorVoltage = readSensorVoltage();

  // Step 2: Calculate sensor resistance (Rs)
  float Rs = calculateSensorResistance(sensorVoltage);

  // Output the results to the Serial Monitor
  Serial.print("Sensor Voltage (V): ");
  Serial.print(sensorVoltage);
  Serial.print("\tSensor Resistance (Rs): ");
  Serial.print(Rs);
  Serial.println(" ohms");

  // Step 3: Use Rs to calculate R0 in clean air (Record Rs as R0 during calibration)
  // In clean air, the calculated Rs can be considered as R0 for further measurements
  // Record the output Rs when the sensor is in clean air to use as R0

  delay(1000);  // Delay 1 second between readings
}
