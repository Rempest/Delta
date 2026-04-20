from ultralytics import YOLO
DeltaPrime = YOLO("yolovn.pt")
Deltaprime.train(data = "VisDrone.yaml", epoch = 70)
