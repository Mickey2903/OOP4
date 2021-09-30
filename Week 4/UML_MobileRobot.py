from enum import Enum


#implement your classes here below. Implement them such that all the test cases below will succeed.
class RobotState(Enum):
    WAITING_FOR_TASK = 0
    DOING_TASK = 1
    TASK_FINISHED = 2
    TASK_STOPPED = 3
    EMERGENCY_STOP = 4

class MobileRobot:
    _wheels = []
    def __init__(self, name, serial_nr):
        self.name = name
        self._serialnumber = serial_nr
        self.state = RobotState.WAITING_FOR_TASK
    
    def assignWheel(self,type,diameter,location):
        self._wheels.append(Wheel(diameter,location))
        return "An " + type + " wheel with a diameter of " + str(diameter) + ", has been assigned to " + str(location.name)

    def performTask(self,task):
        self.state = RobotState.DOING_TASK
        #task

        self.state = RobotState.TASK_FINISHED
        return self.state

    def getTaskStatus(self):
        return self.state

    def stopTask(self):
        self.state = RobotState.TASK_STOPPED
        return self.state

    def emergencyStop(self):
        self.state = RobotState.EMERGENCY_STOP
        return self.state

class WheelLocation(Enum):
    BACK_LEFT = 0
    BACK_RIGHT = 1
    FRONT_LEFT  = 2
    FRONT_RIGHT = 3
    CENTER_LEFT = 4
    CENTER_RIGHT = 5

class Wheel():
    def __init__(self, diameter, location):
        self._diameter = diameter
        self._location = location

class ActuatedWheel(Wheel):
    def __init__(self, wheel, motor, encoder):
        self.wheel = wheel
        self.motor = motor
        self.encoder = encoder
        
class ElectroMotor:
    def __init__(self, motortype, maxRPM):
        self._rpm = 0
        self.motor_type = motortype
        self._maxRPM = maxRPM

    def setRPM(self, value):
        self._rpm = value

    def getRPM(self):
        return (self._rpm) 

class Encoder:
    def __init__(self):
        self._count = 0

    def update(self):
        return "update"

    def getCount(self):
        return self._count




#test cases

def Test():
  #Test 1
  if issubclass(ActuatedWheel,Wheel) == True:
      print("Test 1 succeeded: the actuated wheel class is a sub class of the wheel class")
  else:
      print("Test 1 failed: the actuated wheel class is not a sub class of the wheel class")

  #Test 2
  myMotor = ElectroMotor("brushless",1200)
  if myMotor.getRPM() == 0:
      print("Test 2 succeeded: RPM initially is 0")
  else:
      print("Test 2 failed: the variable RPM is probably not initialized")
  
  #Test 3
  if myMotor.motor_type == "brushless":
      print("Test 3 succeeded: the motortype is correctly initialized")
  else:
      print("Test 3 failed: the motortype is not correctly initialized")
  
  #Test 4
  myMotor.setRPM(600)
  if myMotor.getRPM() == 600:
      print("Test 4 succeeded: RPM is correctly set to 600")
  else:
      print("Test 4 failed: the function setRPM is probably not correctly implemented")

  #Test 5
  myEncoder = Encoder()
  if myEncoder.getCount() == 0:
      print("Test 5 succeeded: Encoder count initially is 0")
  else:
      print("Test 5 failed: the variable for the encoder count is probably not initialized")

  #Test 6
  if myEncoder.update() == "update":
      print("Test 6 succeeded: Encoder count updated")
  else:
      print("Test 6 failed: the update function needs to return the word 'update' ")

  myWheel = Wheel(10, WheelLocation.CENTER_LEFT) 
  myActuatedWheel = ActuatedWheel(myWheel,myMotor,myEncoder)
  
  #Test 7
  if myActuatedWheel.motor.getRPM() == 600:
      print("Test 7 succeeded: wheel has the previously assigned rpm on the attached motor")
  else:
      print("Test 7 failed: wheel does not have the previously on the attached motor")

  #Test 8
  myRobot = MobileRobot("Wall-E", "007")
  print("Test 8 succeeded: "+ myRobot.assignWheel("actuated",10,WheelLocation.CENTER_LEFT))

 #Test 9
  if myRobot.getTaskStatus() == RobotState.WAITING_FOR_TASK:
      print("Test 9 succeeded: initially the robot is waiting for a task")
  else:
      print("Test 9 failed: probably getTaskStatus does not return WAITING_FOR_TASK state")
 #Test 10
  if myRobot.performTask("a task") == RobotState.TASK_FINISHED:
      print("Test 10 succeeded: after the task is performed the task is finished")
  else:
      print("Test 10 failed: probably performTask does not return the TASK_FINISHED state")
 #Test 11
  if myRobot.stopTask() == RobotState.TASK_STOPPED:
      print("Test 11 succeeded: the robot stuccesfully stopped")
  else:
      print("Test 11 failed: probably stopTask does not return the TASK_STOPPED state")
 #Test 12
  if myRobot.emergencyStop() == RobotState.EMERGENCY_STOP:
      print("Test 12 succeeded: emergency stop was succesfull")
  else:
      print("Test 12 failed: probably emergencyStop does not return the EMERGENCY_STOP state")



Test()

