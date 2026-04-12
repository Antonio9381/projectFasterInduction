import cv2 as cv 
 
capture = cv.VideoCapture("./Tasks/Opencv1/videos/Gandalf_laugh.mp4") 

while True: 
    retval, frame = capture.read()     # retval is bool for successful read 

    # Exit loop once end of the video is reached 
    if not retval: 
        break 
    
    cv.imshow("Display name", frame) 
    
    # smaller number means faster video, if num is 0 it freezes
    if cv.waitKey(17) == ord('d'): #btw the num in waitKey is the delay in ms, so 17ms is approx 60fps
        break 

capture.release() 
cv.destroyAllWindows()