
// use A0-plug to check the voltage. //
//
// parameters                        //

int analogPin   = 0;
int val         = 0;
int sampleRate  = 19200;
int interval_ms = 1000


void setup() {
   Serial.begin( sampleRate );
}

void loop() {
  val = analogRead( analogPin );
  Serial.println(val);
  delay( interval_ms );
}
