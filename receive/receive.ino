#include <string.h>

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String prediction = Serial.readStringUntil('\n');
    Serial.print("Predicted: ");
    Serial.println(prediction);
    delay(1000);
  }
}