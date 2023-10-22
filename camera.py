import cv2 #opencv library
import pytesseract
import numpy as np
from main import setCurrentBrakeForce, accelSpeed, setMaxSpeed, printCarInfo
import re
# define a video capture object 
vid = cv2.VideoCapture(0) 
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\gak\\Desktop\\tes\\tesseract.exe'

while(True): 
	ret, frame = vid.read()
	a, b, c = cv2.split(frame)
	gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	data = cv2.CascadeClassifier(r"stopSign.xml")

	found = data.detectMultiScale(gray, minSize=(20,20))
	amtFound = len(found)

	speedSign = cv2.CascadeClassifier(r"speedLimit.xml")
	foundSign = speedSign.detectMultiScale(gray, minSize=(20,20))
	foundSignLen = len(foundSign)

	if amtFound != 0:
		for(x,y,width,height) in found:
			cv2.rectangle(rgb, (x,y), (x+height, y+width), (0,255,0), 5)
			setCurrentBrakeForce(1.0)

	if foundSignLen != 0:
		text = pytesseract.image_to_string(gray, lang = 'eng', config = '--psm 6')
		setMaxSpeed(re.findall(r'\d+', text))
		print(re.findall(r'\d+', text))
		
	accelSpeed()
	printCarInfo()

		
	
	cv2.imshow('frame', rgb)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

vid.release()
cv2.destroyAllWindows()



