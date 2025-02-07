# Smart Bin Project
* 🗑️ Overview
The Smart Bin Project is an AI-powered waste management system that automates waste sorting into three categories:

Clothes
Plastic
Cardboard
Each bin opens automatically when the AI model identifies the specific waste type, making recycling and waste management smarter and more efficient.

* ✨ Features
AI classification trained on three classes: Clothes, Plastic, and Cardboard.
Automated bin operation with Arduino Uno and servo motors.
Hands-free waste sorting using serial communication between the AI model and Arduino boards.
* 🛠️ How It Works
1. AI Classification
The AI model processes an image or video feed to classify the object as either Clothes, Plastic, or Cardboard.
The classification result (e.g., plastic, cardboard) is sent to the corresponding Arduino Uno via serial communication.
2. Arduino Control
Each Arduino controls a servo motor attached to its bin.
When a classification message is received, the Arduino:
Rotates the servo motor to open the bin.
Waits for 10 seconds to allow the waste to be deposited.
Rotates the servo motor back to close the bin.
* ⚙️ Setup
Hardware Requirements
3 bins (one for each waste category).
3 servo motors.
3 Arduino Uno boards.
Camera or device for object detection.
Computer to run the AI model.
Software Requirements
Arduino IDE.
Python (with libraries like TensorFlow, OpenCV, and PySerial).
