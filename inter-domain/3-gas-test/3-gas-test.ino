int sensorPin = A5;          
int sensorData;              
float R0 = 1000.0;           
float Rs;                   

//gas constants
float A_CO2 = 1.44; //1.44         
float B_CO2 = -1.2; // -1.2

float A_METHANE = 1.3;       
float B_METHANE = -1.5;

float A_HYDROGEN = 0.42;     
float B_HYDROGEN = -2.0;

float ppm_CO2;
float ppm_METHANE;
float ppm_HYDROGEN;

void setup() {
  Serial.begin(9600);   
  pinMode(sensorPin, INPUT);  
}

void loop() {
  sensorData = analogRead(sensorPin);
  
  // Calculate rs
  Rs = ((1023.0 / sensorData) - 1) * R0;
  
  // Convert Rs to ppm
  ppm_CO2 = A_CO2 * pow((Rs / R0), B_CO2) * 1000;
  ppm_METHANE = A_METHANE * pow((Rs / R0), B_METHANE) * 1000;
  ppm_HYDROGEN = A_HYDROGEN * pow((Rs / R0), B_HYDROGEN) * 1000;

  Serial.print((Rs / R0));   // Rs/R0
  Serial.print(",");
  Serial.print(ppm_CO2);     // CO2 ppm
  Serial.print(",");
  Serial.print(ppm_METHANE); // Methane ppm
  Serial.print(",");
  Serial.println(ppm_HYDROGEN); // Hydrogen ppm

  delay(100); 
}
