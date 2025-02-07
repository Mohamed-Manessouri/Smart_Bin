#include <Servo.h>

Servo clothesServo;
const int clothes_SERVO_PIN = 9;
const int CLOSED_POSITION = 0;
const int OPEN_POSITION = 90;
const int SERVO_DELAY = 10000;

String inputString = "";
bool stringComplete = false;

void setup() {
    Serial.begin(9600);
    clothesServo.attach(clothes_SERVO_PIN);
    clothesServo.write(CLOSED_POSITION);
    Serial.println("clothes sorter ready!");
}

void activateServo() {
    clothesServo.write(OPEN_POSITION);
    delay(SERVO_DELAY);
    clothesServo.write(CLOSED_POSITION);
    Serial.println("clothes bin sorted!");
}

void loop() {
    if (stringComplete) {
        inputString.trim();
        if (inputString.equals("clothes")) {
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
