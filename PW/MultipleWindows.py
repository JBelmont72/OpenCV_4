'''CV_7.py create multiple windowa lesson 7 PW
python -m venv .venv
source .venv/bin/activate
use the pyenv
use the 3.9.6 ('pyenv':venv)  version in the interpreter!!wing multiple windows
THis works very well sho
'''
import sys
import cv2
print(cv2.__version__)
import numpy as np
print(f"This is version {sys.version}")
print(np.__version__)
# print(cv2.getBuildInformation())
width=1280       ##1280 x 640   :  640 X 360
height=640
rows=int(input('Number of ROWS'))
cols = int(input('Number of Columns'))
cam = cv2.VideoCapture(1)
# cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
square_height=int(height/rows)
square_width=int(width/cols)
def myCallback1(val):
    global myC
    myC=val
cv2.namedWindow('my Trackbars')
cv2.createTrackbar('canny','my Trackbars',60,100,myCallback1)

while True:
    ignore,  frame = cam.read()
    newFrame=cv2.resize(frame,(square_width,square_height))
    print(newFrame.shape)
    for row in range(0,rows,1):
        for col in range(0,cols,1):
            windowName="Window "+str(row)+' x '+str(col)
            if myC>50 and row==0 and col==1:
                newCanny=cv2.Canny(newFrame,50,100)
                cv2.imshow(windowName,newCanny)
                cv2.moveWindow(windowName,int(square_width*col),int(square_height*row+15))
                
            else:  
                cv2.imshow(windowName,newFrame)
                cv2.moveWindow(windowName,int(square_width*col),int(square_height*row+15))
             
    
    
                
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
cap = cv2.VideoCapture(0)