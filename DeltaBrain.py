from DeltaAnalyze as DeltaACT
from DeltaTensors as DeltaSensors
class DeltaBrain(self):
  def __init__(self):
    self.brain = DeltaACT()
    self.sensor = DeltaSensors()
  def run(self)
    print("Analyzing  photo..")
    vision_ok = self.brain.DeltaACT()
    if not vision_ok:
      return False
  print("checking sensors..")
  result = self.sensor.DeltaSensors()
    if result == "STOP":
      print("Robot is stoped")
    else
      print("Robot is working", result)
robot = DeltaBrain()
robot.run()

