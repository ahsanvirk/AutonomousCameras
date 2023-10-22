#Main Logic for brain
#import playsound as playsound
import time

class Car:
    curSpeed = 0
    curMaxSpeed = 25
    curBrakeForce = 0
    curObstacles = 0

def getCurSpeed():
    return Car.curSpeed

def getMaxSpeed():
    return Car.curMaxSpeed

def setMaxSpeed(maxSpeed):
    Car.curMaxSpeed = maxSpeed

def accelSpeed():
    while Car.curSpeed != Car.curMaxSpeed:
        Car.curSpeed += 5

def setCurrentBrakeForce(curForce):
    Car.curBrakeForce = curForce
    while(Car.curBrakeForce > .01):
        Car.curSpeed -= (Car.curBrakeForce * 10)
        if(Car.curSpeed == 0):
            Car.curBrakeForce = 0
            break

starttime = time.monotonic()
def printCarInfo():
    
    print(Car.curSpeed , " Current Speed\n",
	   	Car.curMaxSpeed , " Current Max Speed\n",
		Car.curBrakeForce , " Current Brake Force"
	)

def warnDriver(): # call on close call
    #playsound("man-scream-02.wav")
    pass
