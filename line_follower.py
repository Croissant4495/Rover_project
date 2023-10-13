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
    upper_black = np.array([114, 40, 40])
    hsv_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    mask = np.zeros(image.shape, dtype=np.uint8)
   
    mask = cv2.inRange(hsv_image, lower_black, upper_black)
    new=cv2.bitwise_and(image,image,mask=mask)
  
    median_filtered_image = cv2.medianBlur(mask, 7)
    

    return median_filtered_image
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
    return image
# cap=cv2.VideoCapture('http://192.168.1.9:4747/video')


x=1
def control():
    global x
    # cap=cv2.VideoCapture("track.mp4")
    cap=cv2.VideoCapture('http://192.168.185.174:8080/video')
    while True:
        ret,frame=cap.read()
        
        if not ret:
            break
        h,w,_=frame.shape
        w=round(w/3)
        h=round(h/3)
        # print(f"shape: {frame.shape}")
        frame=frame[0:3*w,h:2*h]
        # print(f"shape2  {frame.shape}")
        frame = cv2.resize(frame, (160, 120))
        low_b=np.uint8([5,5,5])
        high_b=np.uint8([0,0,0])
        mask=remove_background(frame)
        # mask=detect_black(frame)
        thresh,mask=cv2.threshold(mask,50,200,cv2.THRESH_BINARY)
        contours,hierachy=cv2.findContours(mask,1,cv2.CHAIN_APPROX_NONE)
        if len(contours)>0:
            c=max(contours,key=cv2.contourArea)
            M=cv2.moments(c)
            if M["m00"]!=0: # contour is not empty(area)
                cx=int(M["m10"]/M["m00"])
                cy=int(M["m01"]/M["m00"])
                print("CX: "+str(cx)+" CY "+str(cy))
                if cx>=120:
                    print("Turn left")
                    
                    get_x(2)

                if cx<120 and cx>40:
                    print("ON track")
                    get_x(1)

                if cx<=40:
                    print("turn right")
                    get_x(3)

                cv2.circle(frame,(cx,cy),5,(255,0,0),-1)
            
            cv2.drawContours(frame,c,-1,(0,255,0),1)
        else :
            print("backward")
            get_x(4)

        # print(x)
        cv2.imshow("mask",mask)
        cv2.imshow("frame",frame)
        key=cv2.waitKey(1)
        if key==27:
            break
    cap.release()
    cv2.destroyAllWindows()
    # print(frame.shape)
control()
