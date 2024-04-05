#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

const int dirPin = 8;
const int stepPin = 9;
const int speedPin = A0;
const int anglePin = A1;

int speed = 0;
int angle = 0;

void setup() {
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);

  lcd.init();
  lcd.backlight();
  lcd.clear();
}

void loop() {
  speed = map(analogRead(speedPin), 0, 1023, 1, 100); // 1 - 100 as speed
  angle = map(analogRead(anglePin), 0, 1023, 0, 360); // 0 - 360 as angle

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Speed: ");
  lcd.print(speed);
  lcd.print("%");

  lcd.setCursor(0, 1);
  lcd.print("Angle: ");
  lcd.print(angle);
  lcd.print("*");


  // angle
  int steps = map(angle, 0, 360, 0, 200); // 200 steps per rev
  rotate(steps, speed);
  delay(100);
}

void rotate(int steps, int speed) {
  int delayTime = map(speed, 1, 100, 5000, 50);

  if (steps > 0) {
    digitalWrite(dirPin, HIGH); // clockwise
  } else {
    digitalWrite(dirPin, LOW); // counter-clockwise
    steps = -steps; // convert to positive steps value
  }

  for (int i = 0; i < steps; i++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(delayTime);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(delayTime);
  }
}