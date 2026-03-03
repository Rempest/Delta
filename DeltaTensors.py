import numpy as np
class Delta_arrays:
  def DeltaTen(self):
    sensor_data = np.array(2.5, 2.9, 3.0, 1.9, 2.7)
    min_sensor_data = np.min(sensor_data)
    if np.any(sensor_data = 1):
      print("STOP!")
    best_sensor_data = np.argmax(sensor_data)
    way = ["Left", "Left-front", "Straight", "Right-front", "Right"]
    print("The best way it is:", way[best_sensor_data])
    
    
