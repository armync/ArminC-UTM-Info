#include <Servo.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 20, 4);
Servo servos[6];
int potPins[6] = {A0, A1, A2, A3, A4, A5};
int servoPins[6] = {8, 9, 10, 11, 12, 13};

void setup() {
  lcd.init();
  lcd.backlight();

  for (int i = 0; i < 6; i++) {
    servos[i].attach(servoPins[i]);
  }
}

void loop() {
  int potValues[6];
  int servoAngles[6];

  for (int i = 0; i < 6; i++) {
    potValues[i] = analogRead(potPins[i]);
    servoAngles[i] = map(potValues[i], 0, 1023, 0, 180);
    servos[i].write(servoAngles[i]);
  }

  lcd.setCursor(0, 0);
  lcd.print("Potentiometer:");
  lcd.setCursor(0, 1);
  lcd.print("S B L T U R");

  lcd.setCursor(2, 3);
  for (int i = 0; i < 6; i++) {
    lcd.print(formatAngle(servoAngles[i]));
    if (i < 5) {
      lcd.print(" ");
    }
  }

  delay(15);
}

String formatAngle(int angle) {
  return String(angle);
}