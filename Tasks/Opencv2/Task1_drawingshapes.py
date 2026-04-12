import cv2 as cv
import numpy as np

def main(): 
    img = np.zeros((512, 512, 3), dtype=np.uint8) 

    cv.line(img, (0, 0), (511, 511), (255, 0, 0), thickness=2)

    cv.rectangle(img, (100, 100), (350, 300), (0, 255, 0), thickness=3)

    cv.circle(img, (400, 400), 50, (0, 0, 255), thickness=-1)

    poly = np.array([[300, 150], [400, 150], [450, 250], [350, 250]], np.int32)
    cv.polylines(img, [poly], isClosed=True, color=(255, 255, 0), thickness=2)

    cv.imshow("Shapes", img)
    cv.waitKey(0)

if __name__ == "__main__":
    main()