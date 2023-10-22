import cv2 #opencv library
import pytesseract
import numpy as np
from main import setCurrentBrakeForce, accelSpeed, setMaxSpeed, printCarInfo
import re
import threading
# define a video capture object 
vid = cv2.VideoCapture(0) 
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\gak\Desktop\New folder\tesseract.exe"

def __draw_label(img, text, pos, bg_color):
   font_face = cv2.FONT_HERSHEY_SIMPLEX
   scale = 1.0
   color = (255, 255, 255)
   thickness = cv2.FILLED
   margin = 2
   txt_size = cv2.getTextSize(text, font_face, scale, thickness)

   end_x = pos[0] + txt_size[0][0] + margin
   end_y = pos[1] - txt_size[0][1] - margin

   cv2.rectangle(img, pos, (end_x, end_y), bg_color, thickness)
   cv2.putText(img, text, pos, font_face, scale, color, 1, cv2.LINE_AA)

while(True): 
	ret, frame = vid.read()
	a, b, c = cv2.split(frame)
	gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	data = cv2.CascadeClassifier(r"stopSign.xml")
	faces = cv2.CascadeClassifier(r"test.xml")

	found = data.detectMultiScale(gray, minSize=(30,30))
	facesFound = faces.detectMultiScale(gray, minSize=(20,20))
	amtFound = len(found)
	amtFaces = len(facesFound)

	speedSign = cv2.CascadeClassifier(r"speedLimit.xml")
	foundSign = speedSign.detectMultiScale(gray, minSize=(20,20))
	foundSignLen = len(foundSign)

	if amtFaces != 0:
		for(x,y,width,height) in facesFound:
			cv2.rectangle(rgb, (x,y), (x+height, y+width), (255,5,3), 5)

	if foundSignLen != 0:
		text = pytesseract.image_to_string(gray, lang = 'eng', config = '--psm 6')
		for i in re.findall(r'\d+', text):
			if(int(i) > 25 or int(i) % 5 == 0 or int(i) % 10 == 0):
				if i != 0:
					print(i)
		
	if amtFound != 0:
		for(x,y,width,height) in found:
			cv2.rectangle(rgb, (x,y), (x+height, y+width), (0,255,0), 5)
			__draw_label(frame, 'Stop', (20,20), (0,0,0))
			cv2.imshow("Frame", frame)
   			# Display the resulting frame
			#setCurrentBrakeForce(1.0)	
	accelSpeed()

	# Infared sensitive camera that deduces flair

		
	
	cv2.imshow('frame', rgb)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

vid.release()
cv2.destroyAllWindows()



