import cv2
import logging
import numpy as np

from Bridge.Delta_YOLO import Delta_YOLO
from Bridge.Delta_YOLO_analyze import DeltaAnalyze
from Bridge.Delta_decision import DeltaDecision
from Bridge.Delta_Sensors import DeltaSensors

logger = logging.getLogger(__name__)

class DeltaBrain:

    def __init__(self):
        self.yolo = Delta_YOLO()
        self.analyze = DeltaAnalyze()
        self.decision = DeltaDecision()
        self.sensors = DeltaSensors()

    def _get_sensor_data(self) -> np.ndarray:
        return np.array([3.0, 3.5, 5.0, 3.5, 3.0])

    def run(self, source=0):
        cap = cv2.VideoCapture(source)

        if not cap.isOpened():
            logger.error(f"Failed to open video source: {source}")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                logger.warning("Frame capture failed, exiting loop.")
                break

            detections = self.yolo.get_detection(frame)
            target = self.analyze.select_target(detections)
            scene_data = self.analyze.get_scene_data(target)
            decision = self.decision.decide(scene_data)

            sensor_data = self._get_sensor_data()
            sensor_state = self.sensors.DeltaTen(sensor_data)

            if sensor_state == "STOP!":
                decision = "STOP"

            logger.info(f"Decision: {decision} | Sensor: {sensor_state}")

            frame = self.yolo.draw(frame, detections, target)
            cv2.imshow("DeltaBrain", frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break

        cap.release()
        cv2.destroyAllWindows()