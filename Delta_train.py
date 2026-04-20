from ultralytics import YOLO
DeltaPrime = YOLO("yolov8n.pt")
Deltaprime.train(data = "VisDrone.yaml", epochs = 70)
