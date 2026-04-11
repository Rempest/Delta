import numpy as np
import cv2
class DeltaSensors:
  def DeltaTen(self):
    #data of the sensors
    sensor_data = np.array([2.5, 2.9, 3.0, 1.9, 2.7])
    min_sensor_data = np.min(sensor_data)
    #the safe
    if min_sensor_data <= 1.0:
      print("STOP!")
      return "STOP!"
    best_sensor_data = np.argmax(sensor_data)
    way = ["Left", "Left-front", "Straight", "Right-front", "Right"]
    print("The best way it is:", way[best_sensor_data])
    return way[best_sensor_data]

    
