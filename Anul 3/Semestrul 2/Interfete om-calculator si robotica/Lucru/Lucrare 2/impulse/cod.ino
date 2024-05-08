#include <Stepper.h>
#include <LiquidCrystal_I2C.h>

const int stepperPins[6][2] = {{3, 4}, {5, 6}, {7, 8}, {9, 10}, {11, 12}, {13, 14}};

const int potPins[6] = {A0, A1, A2, A3, A4, A5};

Stepper steppers[6] = {Stepper(200, stepperPins[0][0], stepperPins[0][1]),
                       Stepper(200, stepperPins[1][0], stepperPins[1][1]),
                       Stepper(200, stepperPins[2][0], stepperPins[2][1]),
                       Stepper(200, stepperPins[3][0], stepperPins[3][1]),
                       Stepper(200, stepperPins[4][0], stepperPins[4][1]),
                       Stepper(200, stepperPins[5][0], stepperPins[5][1])};

LiquidCrystal_I2C lcd(0x27, 20, 4);

int stepperPositions[6] = {0, 0, 0, 0, 0, 0};

void setup() {
  lcd.init();
  lcd.backlight();

  lcd.setCursor(0, 0);
  lcd.print("Potentiometer:");
  lcd.setCursor(0, 3);
  lcd.print("S B L T U R");
}

void loop() {
  int potValues[6];
  for (int i = 0; i < 6; i++) {
    potValues[i] = analogRead(potPins[i]);
  }

  lcd.setCursor(0, 2);
  for (int i = 0; i < 6; i++) {
    lcd.print(potValues[i]);
    lcd.print(" ");
  }

  for (int i = 0; i < 6; i++) {
    int angle = map(potValues[i], 0, 1023, 0, 360);
    int targetPosition = (angle * 200) / 360;
    int steps = targetPosition - stepperPositions[i];
    steppers[i].step(steps);
    stepperPositions[i] = targetPosition;
  }

  delay(100);
}