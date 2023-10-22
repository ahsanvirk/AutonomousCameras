import cv2 
import numpy as np
from matplotlib import pyplot as plt
import easyOCR
from main import setCurrentSpeed, setMaxSpeed, setCurrentBrakeForce

def findStoplight(): # Steven Will Work On At Hotel | Push Every 10 Minutes
    img = cv2.imread(r"33.jpg")
    colorBoundries = [
         ([17, 15, 100], [50, 56, 200]), # red
         ([25, 146, 190], [62, 174, 250]) # yellow
         #if it doesnt find these two assume green
    ]

    for(lower, upper) in colorBoundries:
         lower = np.array(lower, dtype="uint8")
         upper = np.array(upper, dtype="uint8")

         mask = cv2.inrange(img, lower, upper)
         output = cv2.bitwise_and(img, img, mask=mask)
         print(output)

         cv2.imshow("images", np.hstack[img, output])
         cv2.waitKey(0)

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

def findSpeedLimit(): # Steven Will Work On At Hotel | Pushes Every 10 Minutes
    img = cv2.imread(r"untitled.png")

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    data = cv2.CascadeClassifier(r"speedLimit.xml")

    found = data.detectMultiScale(img_gray, minSize=(20,20))
    amtFound = len(found)

    if amtFound != 0:
        for(x, y, width, height) in found:
                img_noise = cv2.medianBlur(img_gray,3)
                img_thresh = cv2.threshold(img_noise, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
                reader = easyocr.Reader(['en'])
                result = reader.readtext(img,paragraph="False")
                df= pd.DataFram(result)

                print(df[1])
                setMaxSpeed(df[1])
                
            

    plt.subplot(1,1,1)
    plt.imshow(img_rgb)
    plt.show()

# Read Signs
# If close to a object, brake incramentally
# if light is green, red, or yellow respond accordingly
# Help With Turning