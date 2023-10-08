import requests
import cv2
import numpy as np
import imutils
  
# Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
url = "http://192.168.61.8:8080/video"
  
# While loop to continuously fetching data from the Url
capture = cv2.VideoCapture(url)
while(True):
   ret, frame = capture.read()
   cv2.imshow("livestream", frame)
   if cv2.waitKey(1) == ord('q'):
      break
capture.release()
cv2.destroyAllWindows()