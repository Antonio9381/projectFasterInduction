import cv2 as cv
import matplotlib.pyplot as plt

def main():
    img = cv.imread("./Tasks/Opencv3/pics/Beach.png")

    cv.imshow("original", img)

    img_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # inspect the HSV values of the sand using matplotlib
    plt.imshow(img_HSV)
    plt.show()

    Sand_lower = (13, 50, 230)
    Sand_upper = (19, 120, 300)

    img_sand = cv.inRange(img_HSV, Sand_lower, Sand_upper)

    cv.imshow("find sand", img_sand)

    img_morph = cv.morphologyEx(img_sand, cv.MORPH_OPEN, (5, 5), iterations=5)
    img_morph = cv.morphologyEx(img_morph, cv.MORPH_CLOSE, (5, 5), iterations=10)

    cv.imshow("morphology", img_morph)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()