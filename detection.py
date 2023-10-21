import cv2 
from matplotlib import pyplot as plt

img = cv2.imread(r"C:\Users\gak\Desktop\sgins\p\npr.brightspotcdn.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

data = cv2.CascadeClassifier(r"cascade.xml")

found = data.detectMultiScale(img_gray, minSize=(20,20))
amtFound = len(found)

if amtFound != 0:
    for(x, y, width, height) in found:
        cv2.rectangle(img_rgb, (x,y), (x+height, y+width), (0,255,0), 5)
        print("stop sign")

plt.subplot(1,1,1)
plt.imshow(img_rgb)
plt.show()