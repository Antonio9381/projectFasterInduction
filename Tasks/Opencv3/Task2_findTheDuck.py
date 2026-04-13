import cv2 as cv

def main():
    img = cv.imread("./Tasks/Opencv3/pics/Duck.png")

    img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    
    img_col_thresholded_doc = cv.inRange(img, (15, 100, 100), (35, 255, 255))

    cv.imshow("Color Thresholded Image", img_col_thresholded_doc)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()