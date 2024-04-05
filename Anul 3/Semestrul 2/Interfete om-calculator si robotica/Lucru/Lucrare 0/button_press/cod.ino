// button_press
void setup() {
  pinMode(2,INPUT_PULLUP); // button, default=HIGH
  pinMode(13,OUTPUT); // LED
}

void loop() {
  if (digitalRead(2)==LOW) {
    digitalWrite(13,HIGH);
  } else {
    digitalWrite(13,LOW);
  }
  delay(10);
}
