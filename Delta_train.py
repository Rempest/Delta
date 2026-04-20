from ultralytics import YOLO
DeltaPrime = YOLO("yolov8n.pt")
DeltaPrime.train(data = "VisDrone.yaml", epochs = 70)
