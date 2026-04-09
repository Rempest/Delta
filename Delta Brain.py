from DeltaAnalyze import DeltaED
from DeltaTensors import DeltaSensors
class DeltaBrain:
  def __init__(self):
    self.brain = DeltaED()
    self.sensor = DeltaSensors()
  def run(self):
     print("Analyzing  photo..")
    vision_ok = self.brain.DeltaACT()
    if not vision_ok:
      print("The odject is failed...")
      return False
      print("checking sensors..")
     result = self.sensor.DeltaTen()
    if result == "STOP":
      print("Robot is stoped")
    else:
      print("Robot is working", result)
robot = DeltaBrain()
robot.run()

