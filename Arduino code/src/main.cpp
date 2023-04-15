#include <Arduino.h>
#include <Servo.h>
#include <ArduinoJson.h>

Servo servoX;
Servo servoY;
int x = 0;
int y = 0;

void setup() {
  Serial.begin(9600);
  servoX.attach(4);
  servoY.attach(2);

  servoX.write(100);
  servoY.write(90);
  //while (!Serial) continue;
}

void loop() {
  if (Serial.available()) {
    char c = Serial.read();
    
    
    if (c == 'X') {
      int x = Serial.parseInt();
      servoX.write(x);
        delay(15);   
    } else if (c == 'Y') {
      int y = Serial.parseInt();
      servoY.write(y);
        delay(15);   
    }
  }
}









    // char data = Serial.read();

    // if (data == 'X') {
    //   int x = Serial.parseInt();
    //  int areaX = map(x, 600, 0, 70, 179); 
    //   areaX = min(areaX, 179);
    //   areaX = max(areaX, 70);
    //   servoX.write(areaX);


    // } else if (data == 'Y') {
    //   int y = Serial.parseInt();
    //   int areaY = map(y, 450, 0, 179, 95); 

    //   areaY = min(areaY, 179);
    //   areaY = max(areaY, 95);
    //   servoY.write(areaY);
    // }
    // else{
  

    //   int pos = 0;    // variable to store the servo position
    //   for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    //     // in steps of 1 degree
    //     servoX.write(pos); 
    //     servoY.write(pos);             // tell servo to go to position in variable 'pos'
    //     delay(15);                       // waits 15ms for the servo to reach the position
    //   }
    //   for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    //      servoX.write(pos); 
    //     servoY.write(pos);              // tell servo to go to position in variable 'pos'
    //     delay(15);                       // waits 15ms for the servo to reach the position
    //   }









    // }



  


/*   if (Serial.available() >= 8) {
   
    Serial.readBytes(buffer, 8);


    if (Serial.read() == 'X')
    {
      x = Serial.parseInt();
        servoX.write(x);
    }
    if (Serial.read() == 'Y')
    {
      y = Serial.parseInt();
      servoY.write(y);
    }

  }*/

