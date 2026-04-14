import cv2 as cv
import numpy as np

def canny_threshold_values(img: cv.Mat, deviation: float=0.33) -> tuple[float, float]:   
    avgIntense = np.median(img) 
 
    minVal = avgIntense * (1 - deviation) 
    maxVal = avgIntense * (1 + deviation) 
 
    return minVal, maxVal 

def main():
    img = cv.imread("./Tasks/Opencv4/pics/dog.jpg")

    img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    img_gau = cv.GaussianBlur(img_grey, (5,5), 100) #kernal size of (7,7) can get rid of the floor

    min, max = canny_threshold_values(img_gau)

    img_canny = cv.Canny(img_gau, min, max)

    cv.imshow("canny", img_canny)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()