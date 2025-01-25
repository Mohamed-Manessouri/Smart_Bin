import serial
import cv2
import torch
from PIL import Image

from predict.predict import predict_image
from modelArchitecture import ResNet
from dataset.data_prepation import transformations

ser = serial.Serial('COM6', 9600, timeout=1)  

model = ResNet()
model.load_state_dict(torch.load('modelparam.pth', weights_only=True))
model.eval()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    processed_image = transformations(pil_image)

    prediction = predict_image(processed_image, model)

    cv2.putText(frame, f'Predicted: {prediction}', 
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                1, (0, 255, 0), 2)

    ser.write((prediction + "\n").encode())  

    if ser.in_waiting > 0:  
        received_data = ser.readline().decode().strip()  
        print(f"Data received from Arduino: {received_data}")  

    cv2.imshow('Object Classification', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
ser.close()
