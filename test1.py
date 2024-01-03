import cv2
import numpy as np
url = "http://192.168.1.123:4747/video"

cap = cv2.VideoCapture(1)

fore_fram = None

while True:
    state,fram = cap.read()
                                                                   
    gray = cv2.cvtColor(fram,cv2.COLOR_BGRA2GRAY)
    back_fram = cv2.GaussianBlur(gray,(11,11),0)

    if fore_fram is None:                             
        fore_fram = back_fram

    diff_fram = cv2.absdiff(back_fram,fore_fram)
    _,thresh = cv2.threshold(diff_fram,25,255,cv2.THRESH_BINARY)
    
    dilate = cv2.dilate(thresh,None,iterations=4)
    contour,_ = cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for i in contour:
        x,y,w,h = cv2.boundingRect(i)
        cv2.rectangle(fram,(x,y),(x+h,x+y),(0,255,255),3)

    cv2.imshow("test",fram)


    fore_fram = back_fram
    d =  cv2.waitKey(1)
    if d == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
