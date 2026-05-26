from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.train(data="VisDrone.yaml", epochs=70)
