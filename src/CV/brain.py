import cv2
import logging
import numpy as np
import asyncio

from CV.YOLO import Delta_YOLO
from CV.YOLO_analyze import DeltaAnalyze
from CV.decision import DeltaDecision
from CV.sensors import DeltaSensors

logger = logging.getLogger(__name__)


class DeltaBrain:

    def __init__(self, model_path: str = "yolov8n.pt", frame_width: int = 640):
        self.yolo = Delta_YOLO(model_path=model_path)
        self.analyze = DeltaAnalyze(frame_width=frame_width)
        self.decision = DeltaDecision(frame_width=frame_width)
        self.sensors = DeltaSensors()

        self._running = False
        self._last_decision = "SEARCH"
        self._last_sensor_state = "OK"

        logger.info("DeltaBrain initialized.")

    def _get_sensor_data(self) -> np.ndarray:
        # TODO: replace with real Gazebo/PX4 SITL data via MAVSDK
        # Format: [Left, Left-front, Straight, Right-front, Right] in meters
        return np.array([3.0, 3.5, 5.0, 3.5, 3.0])

    def _process_frame(self, frame: np.ndarray) -> tuple[np.ndarray, str, str]:
        detections = self.yolo.get_detection(frame)

        target = self.analyze.select_target(detections)
        scene_data = self.analyze.get_scene_data(target)

        decision = self.decision.decide(scene_data)

        sensor_data = self._get_sensor_data()
        sensor_state = self.sensors.DeltaTen(sensor_data)

        if sensor_state == "STOP!":
            decision = "STOP"

        self._last_decision = decision
        self._last_sensor_state = sensor_state

        frame = self.yolo.draw(frame, detections, target)
        frame = self._draw_overlay(frame, decision, sensor_state, scene_data)

        return frame, decision, sensor_state

    def _draw_overlay(
        self,
        frame: np.ndarray,
        decision: str,
        sensor_state: str,
        scene_data: dict | None
    ) -> np.ndarray:
        color = (0, 255, 0) if decision not in ("STOP", "SEARCH") else (0, 0, 255)

        cv2.putText(
            frame,
            f"Decision: {decision}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7, color, 2
        )

        cv2.putText(
            frame,
            f"Sensor: {sensor_state}",
            (10, 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6, (200, 200, 200), 1
        )

        if scene_data:
            cx = scene_data.get("cx", "-")
            cy = scene_data.get("cy", "-")
            conf = scene_data.get("conf", 0)
            cv2.putText(
                frame,
                f"Target: cx={cx} cy={cy} conf={conf:.2f}",
                (10, 90),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (180, 180, 255), 1
            )

        return frame

    def run(self, source: int | str = 0, show: bool = True) -> None:
        cap = cv2.VideoCapture(source)

        if not cap.isOpened():
            logger.error(f"Failed to open video source: {source}")
            return

        self._running = True
        logger.info(f"DeltaBrain started. Source: {source}")

        try:
            while self._running:
                ret, frame = cap.read()
                if not ret:
                    logger.warning("Frame capture failed, stopping.")
                    break

                frame, decision, sensor_state = self._process_frame(frame)
                logger.info(f"Decision: {decision} | Sensor: {sensor_state}")

                if show:
                    cv2.imshow("Delta Brain", frame)
                    if cv2.waitKey(1) & 0xFF == 27:
                        logger.info("ESC pressed, stopping.")
                        break

        except KeyboardInterrupt:
            logger.info("Interrupted by user.")

        finally:
            self._running = False
            cap.release()
            if show:
                cv2.destroyAllWindows()
            logger.info("DeltaBrain stopped.")

    async def run_async(self, source: int | str = 0, show: bool = False) -> None:
        cap = cv2.VideoCapture(source)

        if not cap.isOpened():
            logger.error(f"Failed to open video source: {source}")
            return

        self._running = True
        logger.info(f"DeltaBrain async started. Source: {source}")

        try:
            while self._running:
                ret, frame = await asyncio.get_event_loop().run_in_executor(
                    None, cap.read
                )

                if not ret:
                    logger.warning("Frame capture failed, stopping.")
                    break

                frame, decision, sensor_state = await asyncio.get_event_loop().run_in_executor(
                    None, self._process_frame, frame
                )

                logger.info(f"[ASYNC] Decision: {decision} | Sensor: {sensor_state}")

                if show:
                    cv2.imshow("Delta Brain", frame)
                    if cv2.waitKey(1) & 0xFF == 27:
                        break

                await asyncio.sleep(0)

        except asyncio.CancelledError:
            logger.info("DeltaBrain async task cancelled.")

        finally:
            self._running = False
            cap.release()
            if show:
                cv2.destroyAllWindows()
            logger.info("DeltaBrain async stopped.")

    def stop(self) -> None:
        self._running = False
        logger.info("DeltaBrain stop requested.")

    @property
    def last_decision(self) -> str:
        return self._last_decision

    @property
    def last_sensor_state(self) -> str:
        return self._last_sensor_state
