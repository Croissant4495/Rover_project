import cv2
import numpy as np
import time

from timeit import default_timer as timer
x1=y1=0
x=y=0
flag_triangles=0
time_=0.0
start=0.0
end=0.0
time_triangles=0.0
def get_limits(color):
    c = np.uint8([[color]]) 
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]  

   
    if hue >= 165:  
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)
    elif hue <= 15:  
        lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    else:
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit
def detect_red(x,y,image):
    flag=False
    red=[0,0,255]
    
    lower_limit=[0,100,100]
    
    upper_limit=[9,255,255]
    lower_limit2=[169,100,100]
    upper_limit2=[180,255,255]
    image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    hsv_value=image[y,x]  
    
    if hsv_value[0]>=lower_limit[0] and hsv_value[0]<=upper_limit[0]:
        # print("1")
        if hsv_value[1]>=lower_limit[1] and hsv_value[1]<=upper_limit[1]:
            # print("2")
            if hsv_value[2]>=lower_limit[2] and hsv_value[2]<=upper_limit[2]:
                flag=True
    else :
        flag=False
    if flag==False:
        if hsv_value[0]>=lower_limit2[0] and hsv_value[0]<=upper_limit2[0]:
        # print("1")
            if hsv_value[1]>=lower_limit2[1] and hsv_value[1]<=upper_limit2[1]:
            # print("2")
             if hsv_value[2]>=lower_limit2[2] and hsv_value[2]<=upper_limit2[2]:
                flag=True
        else :
            flag=False
    image=cv2.cvtColor(image,cv2.COLOR_HSV2BGR)
    return flag,image
def detect_orange(x,y,image):

    flag=False
    
    lower_limit=[10,100,100]
    
    upper_limit=[19,255,255]
    image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    hsv_value=image[y,x]  
    
    if hsv_value[0]>=lower_limit[0] and hsv_value[0]<=upper_limit[0]:
        # print("1")
        if hsv_value[1]>=lower_limit[1] and hsv_value[1]<=upper_limit[1]:
            # print("2")
            if hsv_value[2]>=lower_limit[2] and hsv_value[2]<=upper_limit[2]:
                flag=True
    else :
        flag=False
    image=cv2.cvtColor(image,cv2.COLOR_HSV2BGR)
    return flag,image
def detect_yellow(x,y,image):
    flag=False
    
    lower_limit=[20,100,100]
    
    upper_limit=[30,255,255]
    image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    hsv_value=image[y,x]  
   
    if hsv_value[0]>=lower_limit[0] and hsv_value[0]<=upper_limit[0]:
        # print("1")
        if hsv_value[1]>=lower_limit[1] and hsv_value[1]<=upper_limit[1]:
            # print("2")
            if hsv_value[2]>=lower_limit[2] and hsv_value[2]<=upper_limit[2]:
                flag=True
    else :
        flag=False
    image=cv2.cvtColor(image,cv2.COLOR_HSV2BGR)
    return flag,image
def detect_green(x,y,image):
    flag=False
    
    lower_limit=[31,100,100]
    
    upper_limit=[83,255,255]
    image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    hsv_value=image[y,x]  
    
    if hsv_value[0]>=lower_limit[0] and hsv_value[0]<=upper_limit[0]:
        
        if hsv_value[1]>=lower_limit[1] and hsv_value[1]<=upper_limit[1]:
            
            if hsv_value[2]>=lower_limit[2] and hsv_value[2]<=upper_limit[2]:
                flag=True
    else :
        flag=False
    image=cv2.cvtColor(image,cv2.COLOR_HSV2BGR)
    return flag,image
def detect_blue(x,y,image):
    flag=False
    
    lower_limit=[84,100,100]
    
    upper_limit=[130,255,255]
    image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    hsv_value=image[y,x]  
    
    if hsv_value[0]>=lower_limit[0] and hsv_value[0]<=upper_limit[0]:
        # print("1")
        if hsv_value[1]>=lower_limit[1] and hsv_value[1]<=upper_limit[1]:
            # print("2")
            if hsv_value[2]>=lower_limit[2] and hsv_value[2]<=upper_limit[2]:
                flag=True
    else :
        flag=False
    image=cv2.cvtColor(image,cv2.COLOR_HSV2BGR)
    return flag,image
def detect_purple(x,y,image):
    flag=False
    
    lower_limit=[131,100,100]
    
    upper_limit=[151,255,255]
    image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    hsv_value=image[y,x]  
    
    if hsv_value[0]>=lower_limit[0] and hsv_value[0]<=upper_limit[0]:
        # print("1")
        if hsv_value[1]>=lower_limit[1] and hsv_value[1]<=upper_limit[1]:
            
            if hsv_value[2]>=lower_limit[2] and hsv_value[2]<=upper_limit[2]:
                flag=True
    else :
        flag=False
    image=cv2.cvtColor(image,cv2.COLOR_HSV2BGR)
    return flag,image
def detect_pink(x,y,image):
    flag=False
    
    lower_limit=[152,100,100]
    
    upper_limit=[168,255,255]
    image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    hsv_value=image[y,x]  
    
    if hsv_value[0]>=lower_limit[0] and hsv_value[0]<=upper_limit[0]:
        # print("1")
        if hsv_value[1]>=lower_limit[1] and hsv_value[1]<=upper_limit[1]:
            # print("2")
            if hsv_value[2]>=lower_limit[2] and hsv_value[2]<=upper_limit[2]:
                flag=True
    else :
        flag=False
    image=cv2.cvtColor(image,cv2.COLOR_HSV2BGR)
    return flag,image
def detect_white(x,y,image):
    flag=False
    white=[255,255,255]
    lower_limit,upper_limit=get_limits(white)
    image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    hsv_value=image[y,x]  
    if hsv_value[0]>=lower_limit[0] and hsv_value[0]<=upper_limit[0]:
        if hsv_value[1]>=lower_limit[1] and hsv_value[1]<=upper_limit[1]:
            if hsv_value[2]>=lower_limit[2] and hsv_value[2]<=upper_limit[2]:
                flag=True
    else :
        flag=False
    image=cv2.cvtColor(image,cv2.COLOR_HSV2BGR)
    return flag,image
def detect_black(x,y,image):
    flag=False
    black=[0,0,0]
    lower_limit = np.array([0, 0, 0])
    upper_limit = np.array([360, 255, 100])
    
    image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    hsv_value=image[y,x]  
    if hsv_value[0]>=lower_limit[0] and hsv_value[0]<=upper_limit[0]:
        if hsv_value[1]>=lower_limit[1] and hsv_value[1]<=upper_limit[1]:
            if hsv_value[2]>=lower_limit[2] and hsv_value[2]<=upper_limit[2]:
                flag=True
    else :
        flag=False
    image=cv2.cvtColor(image,cv2.COLOR_HSV2BGR)
    return flag,image
def detection(x,y,image):
 
    string=None
    image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    
    hsv_value=image[y,x]
    
    image=cv2.cvtColor(image,cv2.COLOR_HSV2BGR)
    flag,image=detect_yellow(x,y,image)
    
    if flag:
        string="yellow"
        
        return string,image
    
    flag,image=detect_green(x,y,image)
    if flag:
        string="green"
        return string,image
    flag,image=detect_blue(x,y,image)
    if flag:
        string="blue"
        return string,image
    flag,image=detect_red(x,y,image)
    if flag:
        string="red"
        return string,image
    flag,image=detect_purple(x,y,image)
    if flag:
        string="purple"
        return string,image
    flag,image=detect_pink(x,y,image)
    if flag:
        string="pink"
        return string,image
    flag,image=detect_orange(x,y,image)
    if flag:
        string="orange"
        return string,image
    flag,image=detect_white(x,y,image)
    if flag:
        string="white"
        return string,image
    flag,image=detect_black(x,y,image)
    
    if flag:
        string="black"
        return string,image
    else:
        string ="invalid"
        return string,image
def color_count(flag):
    global red,black,blue,green,yellow,white,purple,pink,orange
    
    if flag=="yellow":
        yellow+=1
    elif flag=="white":
        white+=1
    elif flag=='black':
        black+=1
    elif flag=="blue":
        blue+=1
    elif flag=='red':
        red+=1
    elif flag=="purple":
        purple+=1
    elif flag=='green':
        green+=1
    elif flag=='pink':
        pink+=1
    elif flag=='orange':
        orange+=1  
def get_contour_point(contour):

  area = cv2.contourArea(contour)
  moments = cv2.moments(contour)

  center_of_mass = (moments['m10'] / area, moments['m01'] / area)
  return center_of_mass
def editing_image(img):
  if img is not None:
    imgContour=img.copy()
    
  imgBlur = cv2.GaussianBlur(img, (7, 7), 1) #removing noise
  imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

  imgCanny = cv2.Canny(imgGray,10,200) # detecting edges
  kernel = np.ones((3, 3))
  imgDil = cv2.dilate(imgCanny, kernel, iterations=1) #thicken the edges
  kernel=np.ones((3,3),np.uint8)
  imgDil=cv2.erode(imgDil,kernel)
  
  return imgDil,imgContour
def find_contours(img):
  global time_
  even=0
  start = timer()


  global flag_triangles,time_triangles
  global stars,squares,circles,triangles,rectangles,x,y,x1,y1
  stars=squares=circles=triangles=rectangles=0   # every time I call the function-> new counter
  global red,black,blue,green,yellow,white,purple,pink,orange
  red=black=blue=green=yellow=white=purple=pink=orange=0
  i=0
  color_array=[]
  imgDil,imgContour=editing_image(img)
  contours, hierarchy = cv2.findContours(imgDil, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  parent=[]
  c=-1
  contor_counter=0
  flag=False
  array=np.squeeze(hierarchy)
  z=[]
  if hierarchy is not None:
    if array.ndim==2:
      # print("hi")
      parent=array[:,3]
      max=np.max(parent)
      flag=True
 
  new_flag=0
  for cnt in contours:
    c+=1
    contor_counter+=1
    if hierarchy is not None and flag==True:
      if not(parent[c]==max):
        continue
    # if (contor_counter%30==0):
      # print(cnt)
    area = cv2.contourArea(cnt)
    if area < 700:
      continue
    peri = cv2.arcLength(cnt, True) 
    approx = cv2.approxPolyDP(cnt, 0.02 * peri, True) #number of points
    x , y , w, h = cv2.boundingRect(approx)
    x1 = approx.ravel()[0]
    y1 = approx.ravel()[1]
    ratio=w/h
    
    cv2.drawContours(imgContour, approx, -1, (0, 0, 0), 2)
    length=len(approx)
    here=0
    if length==4:
      if ratio >=0.95 and ratio<=1.05:
         squares+=1
         here=1
      else:

          rectangles+=1
          here=1

    elif length==3:
     
        triangles+=1
        here=1
  
    elif length==10:
        stars+=1
        here=1
    elif length==8:
      circles+=1
      here=1
    
    # x , y , w, h = cv2.boundingRect(approx)
    x1=(x+x+w)/2
    x1=round(x1)
    y1=(y+y+h)/2
    y1=round(y1)
    x1,y1=get_contour_point(cnt)
    x1=round(x1)
    y1=round(y1)
    if here==1:
        flag,imgC=detection(x1,y1,imgContour)
        color_array.append(flag)

    cv2.rectangle(imgContour, (x , y ), (x + w , y + h ), (0, 0, 0), 3)
  end = timer()
  time_+= end-start
  return imgContour,x1,y1,color_array,triangles,squares,rectangles,circles,stars
