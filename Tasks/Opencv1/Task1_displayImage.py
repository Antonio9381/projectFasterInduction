import cv2 as cv

def rescale(frame: cv.Mat, scale: float) -> cv.Mat: 
    height = int(frame.shape[0] * scale) 
    width = int(frame.shape[1] * scale) 
    dim = (width, height) 
 
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)

def main(): 
    leGOAT = cv.imread("./Tasks/Opencv1/photos/sexypic.jpg") 
    leGOAT = rescale(leGOAT, 0.67)
    cv.imshow("leGOAT", leGOAT)
    cv.waitKey(0)

if __name__ == "__main__": 
    main()