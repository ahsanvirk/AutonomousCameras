#Main Logic for brain
import playsound as playsound

class Car:
    curSpeed = 0
    curMaxSpeed = 55
    curBrakeForce = 0
    curObstacles = 0

def setMaxSpeed(maxSpeed):
    Car.curMaxSpeed = maxSpeed

def setCurrentSpeed(curSpeed):
    Car.curSpeed = curSpeed

def setCurrentBrakeForce(curForce):
    Car.curBrakeForce = curForce
    while(Car.curBrakeForce > .01):
        Car.curSpeed -= (Car.curBrakeForce * 10)
        if(Car.curSpeed == 0):
            Car.curBrakeForce = 0
            break

def warnDriver(): # call on close call
    playsound("man-scream-02.wav")
    pass
