import requests
import cv2
import numpy as np
import imutils
import keyboard

  
# Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
url = "http://192.168.185.174:8080/video"
button_arr = [0, 0, 0, 0, 0, 0]

# While loop to continuously fetching data from the Url
capture = cv2.VideoCapture(url)
while(True):
   button_arr = [0, 0, 0, 0, 0, 0]

   if keyboard.is_pressed("w"):
      button_arr[0] = 1
   if keyboard.is_pressed("a"):
      button_arr[1] = 1
   if keyboard.is_pressed("d"):
      button_arr[2] = 1
   if keyboard.is_pressed("s"):
      button_arr[3] = 1
   if keyboard.is_pressed("j"):
      button_arr[4] = 1
   if keyboard.is_pressed("k"):
      button_arr[5] = 1
   print(button_arr)

   ret, frame = capture.read()
   cv2.imshow("livestream", frame)
   if cv2.waitKey(1) == ord('q'):
      break
capture.release()
cv2.destroyAllWindows()