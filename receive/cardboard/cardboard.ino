#include <Servo.h>

Servo cardServo;
const int card_SERVO_PIN = 9;
const int CLOSED_POSITION = 0;
const int OPEN_POSITION = 90;
const int SERVO_DELAY = 10000;

String inputString = "";
bool stringComplete = false;

void setup() {
    Serial.begin(9600);
    cardServo.attach(card_SERVO_PIN);
    cardServo.write(CLOSED_POSITION);
    Serial.println("card sorter ready!");
}

void activateServo() {
    cardServo.write(OPEN_POSITION);
    delay(SERVO_DELAY);
    cardServo.write(CLOSED_POSITION);
    Serial.println("card bin sorted!");
}

void loop() {
    if (stringComplete) {
        inputString.trim();
        if (inputString.equals("cardboard")) {
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
