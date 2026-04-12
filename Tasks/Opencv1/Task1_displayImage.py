import cv2 as cv

def main(): 
    leGOAT = cv.imread("./Tasks/Opencv1/photos/sexypic.jpg") 
    cv.imshow("leGOAT", leGOAT)
    cv.waitKey(0)

if __name__ == "__main__": 
    main()