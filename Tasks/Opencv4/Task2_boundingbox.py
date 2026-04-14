import cv2 as cv
import numpy as np

def canny_threshold_values(img: cv.Mat, deviation: float=0.33) -> tuple[float, float]:   
    avgIntense = np.median(img) 
 
    minVal = avgIntense * (1 - deviation) 
    maxVal = avgIntense * (1 + deviation) 
 
    return minVal, maxVal 

def main():
    img = cv.imread("./Tasks/Opencv4/pics/blueballed.png")

    img_grey = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

    min, max = canny_threshold_values(img_grey)

    img_edged = cv.Canny(img_grey, min, max)

    cnt, _ = cv.findContours(img_edged, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    cnt = cnt[0]

    x,y,w,h = cv.boundingRect(cnt)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    cv.imshow('contour ball', img)

    cv.waitKey(0)
    cv.destroyAllWindows

if __name__ == "__main__":
    main()