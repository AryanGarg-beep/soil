const int bulb1 = 13; 
const int bulb2 = 12; 
const int bulb3 = 11;
const int bulb4 = 10;

const long interval1 = 2000;    
const long interval2 = 3000;
const long interval3 = 4000;
const long interval4 = 5000;
const long blinktime = 100; 


unsigned long lastMillis1 = 0;
unsigned long lastMillis2 = 0;
unsigned long lastMillis3 = 0;
unsigned long lastMillis4 = 0;


int bulb1State = LOW;
int bulb2State = LOW;
int bulb3State = LOW;
int bulb4State = LOW;

void setup() {
  
  pinMode(bulb1, OUTPUT);
  pinMode(bulb2, OUTPUT);
  pinMode(bulb3, OUTPUT);
  pinMode(bulb4, OUTPUT);
}

void loop() {
  unsigned long currentMillis = millis();

  
  if (bulb1State == LOW && (currentMillis - lastMillis1 >= interval1)) {
    bulb1State = HIGH;  
    lastMillis1 = currentMillis; 
    digitalWrite(bulb1, bulb1State);
  } else if (bulb1State == HIGH && (currentMillis - lastMillis1 >= blinktime)) {
    bulb1State = LOW;   
    digitalWrite(bulb1, bulb1State);
  }

  
  if (bulb2State == LOW && (currentMillis - lastMillis2 >= interval2)) {
    bulb2State = HIGH;  
    lastMillis2 = currentMillis; 
    digitalWrite(bulb2, bulb2State);
  } else if (bulb2State == HIGH && (currentMillis - lastMillis2 >= blinktime)) {
    bulb2State = LOW;   
    digitalWrite(bulb2, bulb2State);
  }
  
  if (bulb3State == LOW && (currentMillis - lastMillis3 >= interval3)) {
    bulb3State = HIGH;
    lastMillis3 = currentMillis;
    digitalWrite(bulb3, bulb3State);
  }else if(bulb3State == HIGH && (currentMillis - lastMillis3 >= blinktime)){
    bulb3State = LOW;
    digitalWrite(bulb3, bulb3State);
  }
  
  if (bulb4State == LOW && (currentMillis - lastMillis4 >= interval4)) {
    bulb4State = HIGH;
    lastMillis4 = currentMillis;
    digitalWrite(bulb4, bulb4State);
  }else if(bulb4State == HIGH && (currentMillis - lastMillis4 >= blinktime)){
    bulb4State = LOW;
    digitalWrite(bulb4, bulb4State);
  }
  
  
}

    


    
  