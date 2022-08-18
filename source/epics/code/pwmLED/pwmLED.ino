
// arduino PWM output program //

int    pin_LED    = 5;
int    usb_bpm    = 19200;

void setup() {
  // put your setup code here, to run once:
  pinMode( pin_LED, OUTPUT );
  Serial.begin( usb_bpm );
}

void loop() {
  // put your main code here, to run repeatedly:
  
  if ( Serial.available() > 0 ){
    int iRecv = Serial.parseInt();
    if ( iRecv > 255 ){
      iRecv = 255;
    } else if ( iRecv < 0 ){
      iRecv = 0;
    }
    analogWrite( pin_LED, iRecv );
  }
}
