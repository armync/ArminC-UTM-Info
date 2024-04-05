#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <AccelStepper.h>

#define MOTOR_DIR_PIN 8
#define MOTOR_STEP_PIN 9
#define ANALOG_INPUT_1 A0
#define ANALOG_INPUT_2 A1
#define MOTOR_STEPS_PER_REV 200

AccelStepper motorControl(AccelStepper::FULL4WIRE, MOTOR_STEP_PIN, MOTOR_DIR_PIN);
LiquidCrystal_I2C displayUnit(0x27, 20, 4);

int userInput1;
int userInput2;
int rotation1;
int rotation2;
int diff;

const int motorAcceleration = 65;
const int motorMaxSpeed = 4000;

void setup() {
  Serial.begin(9600);
  motorControl.setMaxSpeed(motorMaxSpeed);
  motorControl.setAcceleration(motorAcceleration);
  displayUnit.init();
  displayUnit.backlight();
}

void loop() {
  controlRotation();

  displayUnit.clear();
  displayUnit.setCursor(0, 0);
  displayUnit.print("Slide 1: ");
  displayUnit.print(rotation1);
  displayUnit.setCursor(0, 1);
  displayUnit.print("Slide 2: ");
  displayUnit.print(rotation2);
  displayUnit.setCursor(0, 2);
  displayUnit.print("Diff: ");
  displayUnit.print(diff);

  delay(100);
}

void controlRotation() {
  userInput1 = analogRead(ANALOG_INPUT_1);
  userInput2 = analogRead(ANALOG_INPUT_2);
  rotation1 = map(userInput1, 0, 1023, 0, 180);
  rotation2 = map(userInput2, 0, 1023, 0, 180);

  if (rotation1 >= rotation2) {
    diff = rotation1 - rotation2;
  } else {
    diff = rotation2 - rotation1;
  }

  if (rotation2 >= rotation1 && rotation2 <= (rotation1 + 10)) {
    diff = 0;
    motorControl.setSpeed(0);
  } else {
    int targetPosition = rotation1 * (MOTOR_STEPS_PER_REV / 180);
    motorControl.moveTo(targetPosition);
  }

  motorControl.run();
}