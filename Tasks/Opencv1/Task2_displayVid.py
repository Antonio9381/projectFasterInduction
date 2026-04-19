import cv2 as cv 

def rescale(frame: cv.Mat, scale: float) -> cv.Mat: 
    height = int(frame.shape[0] * scale) 
    width = int(frame.shape[1] * scale) 
    dim = (width, height) 
 
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)
 
capture = cv.VideoCapture("./Tasks/Opencv1/videos/Gandalf_laugh.mp4") 

while True: 
    retval, frame = capture.read()

    if not retval: 
        break 

    frame = rescale(frame, 0.67)
    
    cv.imshow("Display name", frame) 
    
    # smaller number means faster video, if num is 0 it freezes
    if cv.waitKey(17) == ord('d'): #btw the num in waitKey is the delay in ms, so 17ms is approx 60fps
        break 

capture.release() 
cv.destroyAllWindows()