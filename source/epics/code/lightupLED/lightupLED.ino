
// program to control LED's luminocity by PWM.

// parameters
int pin_LED     = 2;
int powerFactor = 0.0;
int serial_bps  = 19200;
int ASCII_H     = 72;
int ASCII_L     = 76;

void setup() {
  // put your setup code here, to run once:
  pinMode( pin_LED, OUTPUT );
  Serial.begin( serial_bps );
}

void loop() {
  // put your main code here, to run repeatedly:
  
  if ( Serial.available() > 0){
    char cRecv = Serial.read();

    if ( cRecv == ASCII_H ){
      digitalWrite( pin_LED, HIGH );
    }
    else if ( cRecv == ASCII_L ){
      digitalWrite( pin_LED, LOW  );
    }
  }
} 
