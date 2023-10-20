import cv2
import numpy as np
"""range of black
size and height
coordinates
black or noise detection
area
"""
def get_x(x):
    return x
    
def detect_black(image):
    
    lower_black = np.array([0, 0, 0])
    # upper_black = np.array([114, 40, 40])
    upper_black = np.array([200, 100, 100])
    hsv_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    mask = np.zeros(image.shape, dtype=np.uint8)
    mask = cv2.inRange(hsv_image, lower_black, upper_black)
    blurred = cv2.GaussianBlur(mask, (5, 5), 0)
    median = cv2.medianBlur(blurred, 5)

    contrasted = cv2.convertScaleAbs(median, alpha=1.5, beta=0)
    kernel = np.ones((5, 5), np.uint8)


    #dilated_image = cv2.dilate(contrasted, kernel)
    eroded_image=cv2.erode(contrasted,kernel)
    #new=cv2.bitwise_and(image,image,mask=mask)
    new=cv2.bitwise_not(eroded_image)

    return contrasted,new
def black(image):
    
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([114, 40, 40])
    
    hsv_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    mask = np.zeros(image.shape, dtype=np.uint8)
    mask = cv2.inRange(hsv_image, lower_black, upper_black)
    new=cv2.bitwise_and(image,image,mask=mask)
    median_filtered_image = cv2.medianBlur(mask, 7)
    #print(mask.shape)
    #mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    return mask
def get_contour_point(contour):

  area = cv2.contourArea(contour)
  moments = cv2.moments(contour)

  center_of_mass = (moments['m10'] / area, moments['m01'] / area)
  return center_of_mass
def remove_background(image):

    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _,image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) #automatically calculates the optimal threshold value for the image, which is the value that best separates the foreground from the background
    contours,_ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    largest_contour = sorted(contours, key=cv2.contourArea, reverse=True)[0] # Find the largest contour in the image.

   
    cv2.fillConvexPoly(image, largest_contour, 255) # fills the contour with white.
    image = cv2.bitwise_not(image) #inverts the image
    algo = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
    foreground_mask = algo.apply(image)
    image = cv2.bitwise_not(image)

    image[foreground_mask == 0] = 0 # Remove the background from all areas that are not surrounded by the whiteline.
    image=cv2.bitwise_not(image)
    kernel=kernel = np.ones((5, 5), np.uint8)
    image=cv2.erode(image,kernel)
    return image
def detect_line(image):
    edges = cv2.Canny(image, 50, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)
    if lines is None:
        return False
    else:
        return True
def otsu2(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    kernel=np.ones((5, 5), np.uint8)
    contours = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

   
    smallest_contour = sorted(contours, key=cv2.contourArea, reverse=False)[0] # Find the largest contour in the image.
    image=cv2.erode(image,kernel)
    image=cv2.dilate(image,kernel)
   
    cv2.fillConvexPoly(image, smallest_contour, 0)
    return image
def detect_lines(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)
    if lines is None:
        return None, image
    largest_line = None
    max_votes = 0
    for line in lines:
        votes = line[0][0]
        if votes > max_votes:
            max_votes = votes
            largest_line = line[0]
    x1, y1, x2, y2 = largest_line
    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    slope=(y2-y1)/(x2-x1)
    angle=np.arctan(slope)
    angle_in_degrees = angle * 180 / np.pi
    return angle_in_degrees,image
# cap=cv2.VideoCapture('http://192.168.1.9:4747/video')
x=1
first_time = True
def control():
    global x
    # cap=cv2.VideoCapture("track.mp4")
    if first_time:
        cap=cv2.VideoCapture('http://192.168.1.9:4747/video')
        first_time = False

    ret,frame=cap.read()

    if ret:
        image=frame.copy()
        h,w,_=frame.shape
        
        h=round(h/3)
        frame=frame[2*h:3*h, 0:w]
        # mask=remove_background(frame)
        # mask,_=detect_black(frame)
        mask=otsu2(frame)
        contours,hierachy=cv2.findContours(mask,1,cv2.CHAIN_APPROX_NONE)
        # print("here")
        w=round(w/4)
        #if len(contours)>0 and detect_line(mask)==True :
        if len(contours)>0  :
            c=max(contours,key=cv2.contourArea)
            # if (cv2.contourArea(c)<1000):
            #     print("backwards")
            #     continue
                
            M=cv2.moments(c)
            if M["m00"]!=0: # contour is not empty
                cx=int(M["m10"]/M["m00"])
                cy=int(M["m01"]/M["m00"])
                #print("CX: "+str(cx)+" CY "+str(cy))
                # if (cv2.contourArea(c)<1000):
                #      print("backwards")
                if cx>=3*w:
                    x=3
                elif cx<3*w and cx>w:
                    x=1
                elif cx<=w:
                    x=2
                cv2.circle(frame,(cx,cy),5,(255,0,0),-1)
                
                cv2.drawContours(frame,c,-1,(0,255,0),1)
            else :
                print("backward")
                x = 4

