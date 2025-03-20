
#include "DHT.h"
#include <DS3231.h>
#include <time.h>

DS3231 myRTC;
bool h12;
bool hPM;
bool mode = false;

#define DHTPIN 11               // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11          // DHT 11
DHT dht(DHTPIN, DHTTYPE); 

int UCL = 65;
int LCL = 58;
int MOSFET = 3;
int Nightlight = 7;
int Daylight = 9;
int Humidifier = 5;

void setup() {
  Wire.begin();
  myRTC.setClockMode(mode);
  Serial.begin(9600);
  pinMode(MOSFET, OUTPUT); 
  pinMode(Nightlight, OUTPUT);
  pinMode(Daylight, OUTPUT);
  pinMode(Humidifier, OUTPUT);
  dht.begin();
  
}
///
void loop() {
  
  // Wait a few seconds between measurements.
  delay(1000);
  
  //gets seconds, minutes, and hour
  int second = myRTC.getSecond();
  int min = myRTC.getMinute();
  int hour = myRTC.getHour(h12, hPM);

  //checks if the hour is 18 (6PM)
  //if it is, turns on the nightlight
  //otherwise, turns on the daylight
   if (hour >= 19 || hour <= 7){
    digitalWrite(Nightlight, HIGH);
    digitalWrite(Daylight, LOW);
   }
   else{
    digitalWrite(Daylight, HIGH);
    digitalWrite(Nightlight, LOW);
   }
   
  //get temperature and humidity values
  int h = dht.readHumidity();
  int f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(f)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;  
  }

  //checks if the humidity goes above the upper limit
  //if so, then it turns off the fan and humidifier
  
  if (h>UCL){
    digitalWrite(MOSFET, LOW);            //turns off fan (MOSFET)
    digitalWrite(Humidifier, LOW);        //turns off humidifier
  }

 //checks if the humidity goes under the lower limit
 //if so, then it turns on the fan and humidifier 
 
  if (h<LCL){
    digitalWrite(MOSFET, HIGH);            //turns on fan (MOSFET)
    digitalWrite(Humidifier, HIGH);       //turns on humidifier
    }
   
  Serial.print(h);
  Serial.print(" ");
  Serial.println(f);
  Serial.print(" ");
}
