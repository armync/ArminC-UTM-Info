void setup() {
  Serial.begin(9600);
}

void loop() {
  const float BETA = 3950;
  int analogValue = analogRead(A0);
  float celsius = 1 / (log(1 / (1023. / analogValue - 1)) / BETA + 1.0 / 298.15) - 273.15;

  Serial.print("Temperature is ");
  Serial.println(celsius);
  
  delay(1000);
}
