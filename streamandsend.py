import serial
import cv2
import torch
import time
from PIL import Image
from predict.predict import predict_image
from modelArchitecture import ResNet
from dataset.data_prepation import transformations

class MultiArduinoController:
    def __init__(self, ports, baud_rate=9600, model_path='modelparam.pth', detection_interval=5):
        self.serial_connections = {
            "plastic": serial.Serial(ports["plastic"], baud_rate, timeout=1),
            "cardboard": serial.Serial(ports["cardboard"], baud_rate, timeout=1),
            "clothes": serial.Serial(ports["clothes"], baud_rate, timeout=1),
        }

        self.model = ResNet()
        self.model.load_state_dict(torch.load(model_path, weights_only=True))
        self.model.eval()

        self.detection_interval = detection_interval
        self.last_detection_time = 0

    def send_to_arduino(self, label):
        if label in self.serial_connections:
            print(f"Sending '{label}' to Arduino...")
            self.serial_connections[label].write((label + "\n").encode())
        else:
            print(f"Label '{label}' is invalid or not connected to any Arduino.")

    def process_frame(self, frame):
        pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        processed_image = transformations(pil_image)

        prediction = predict_image(processed_image, self.model)
        cv2.putText(frame, f'Predicted: {prediction}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        return frame, prediction

    def run(self):
        cap = cv2.VideoCapture(0)  
        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                processed_frame, prediction = self.process_frame(frame)

                current_time = time.time()
                if current_time - self.last_detection_time > self.detection_interval:
                    self.send_to_arduino(prediction)
                    self.last_detection_time = current_time

                cv2.imshow('Object Classification', processed_frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        finally:
            cap.release()
            cv2.destroyAllWindows()
            for connection in self.serial_connections.values():
                connection.close()

if __name__ == '__main__':
    ports = {
        "plastic": "COM7",  
        "cardboard": "COM5",
        "clothes": "COM8",
    }
    controller = MultiArduinoController(ports)
    controller.run()
