#include <Servo.h>

Servo plasticServo;
const int PLASTIC_SERVO_PIN = 9;
const int CLOSED_POSITION = 0;
const int OPEN_POSITION = 90;
const int SERVO_DELAY = 10000;

String inputString = "";
bool stringComplete = false;

void setup() {
    Serial.begin(9600);
    plasticServo.attach(PLASTIC_SERVO_PIN);
    plasticServo.write(CLOSED_POSITION);
    Serial.println("Plastic sorter ready!");
}

void activateServo() {
    plasticServo.write(OPEN_POSITION);
    delay(SERVO_DELAY);
    plasticServo.write(CLOSED_POSITION);
    Serial.println("Plastic bin sorted!");
}

void loop() {
    if (stringComplete) {
        inputString.trim();
        if (inputString.equals("plastic")) {
            activateServo();
        }
        inputString = "";
        stringComplete = false;
    }

    while (Serial.available()) {
        char inChar = (char)Serial.read();
        if (inChar == '\n') {
            stringComplete = true;
        } else {
            inputString += inChar;
        }
    }
}
