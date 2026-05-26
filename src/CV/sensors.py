import numpy as np
import cv2
import logging

logger = logging.getLogger(__name__)

class DeltaSensors:
    DIRECTIONS = ["Left", "Left-front", "Straight", "Right-front", "Right"]
    SAFE_DISTANCE = 1.0

    def DeltaTen(self, sensor_data: np.ndarray) -> str:
        if sensor_data is None or len(sensor_data) == 0:
            logger.error("Sensor data is empty or None")
            return "STOP!"

        if len(sensor_data) != len(self.DIRECTIONS):
            logger.error(f"Expected {len(self.DIRECTIONS)} sensors, got {len(sensor_data)}")
            return "STOP!"

        if not np.all(np.isfinite(sensor_data)):
            logger.warning("Sensor data contains NaN or Inf values")
            return "STOP!"

        min_distance = np.min(sensor_data)

        if min_distance <= self.SAFE_DISTANCE:
            logger.warning(f"Obstacle detected! Min distance: {min_distance:.2f}m")
            return "STOP!"

        best_direction_idx = np.argmax(sensor_data)
        direction = self.DIRECTIONS[best_direction_idx]

        logger.info(f"Best direction: {direction} (distance: {sensor_data[best_direction_idx]:.2f}m)")
        return direction
