const int pinSensor = 8; //pin number for PIR sensor

void setup() 
{
  pinMode(pinSensor, INPUT);
  Serial.begin(9600);
}

void loop() 
{
  int sensorValue = digitalRead(pinSensor); 

  if(sensorValue == 1)    //will send '1' or '2' value to Serial which will be read by the python script
    Serial.println('1');
  else
    Serial.println('2');

}
