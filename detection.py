import cv2 
from matplotlib import pyplot as plt
import pytesseract

def findStoplight():

    img = cv2.imread(r"33.jpg")

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    data = cv2.CascadeClassifier(r"stopSign.xml")

    found = data.detectMultiScale(img_gray, minSize=(20,20))
    amtFound = len(found)

    if amtFound != 0:
        for(x, y, width, height) in found:
            cv2.rectangle(img_rgb, (x,y), (x+height, y+width), (0,255,0), 5)
            print("stop sign")

    plt.subplot(1,1,1)
    plt.imshow(img_rgb)
    plt.show()

def findSpeedLimit():
    img = cv2.imread(r"33.jpg")

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    data = cv2.CascadeClassifier(r"speedLimit.xml")

    found = data.detectMultiScale(img_gray, minSize=(20,20))
    amtFound = len(found)

    if amtFound != 0:
        for(x, y, width, height) in found:
            cv2.rectangle(img_rgb, (x,y), (x+height, y+width), (0,255,0), 5)
            

    plt.subplot(1,1,1)
    plt.imshow(img_rgb)
    plt.show()

# Read Signs
# If close to a object, brake incramentally
# if light is green, red, or yellow respond accordingly
# Help With Turning