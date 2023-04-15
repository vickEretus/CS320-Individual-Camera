#include <Servo.h>


Servo servo1;  // create servo object to control a servo

Servo servo2; 
// twelve servo objects can be created on most boards
char serial;

int pos = 0;    // variable to store the servo position

struct Data {
  float value;
};

void setup() {

  // servo2.attach(10);  // attaches the servo on pin 9 to the servo object
  // servo1.attach(8); 

  // servo2.write(90);
  // servo1.write(90);
  
  Serial.begin(9600);
  //Serial.setTimeout(1);
}


void loop() {
  //sends  difference of x and y values between the center of the area 
  //and what cv is thinking is a face 
  if (Serial.available() > 0) { //= sizeof(Data)
    //Data data;
    serial = Serial.read();
    //Serial.readBytes((char*)&data, sizeof(Data));
    Serial.println(serial, HEX);
  }


  // for (pos = 0; pos <= 180; pos += 2.5) { // goes from 0 degrees to 180 degrees
    

  //   servo1.write(pos);            // tell servo to go to position in variable 'pos'
  //   servo2.write(pos);
  //   delay(15);                       // waits 15ms for the servo to reach the position

  // }

  // for (pos = 180; pos >= 0; pos -= 2.5) { // goes from 180 degrees to 0 degrees
    

  //   servo1.write(pos);              // tell servo to go to position in variable 'pos'
  //   servo2.write(pos);              // tell servo to go to position in variable 'pos'

  //   delay(15);                       // waits 15ms for the servo to reach the position

  //}

}




