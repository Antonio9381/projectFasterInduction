import cv2 as cv
import matplotlib.pyplot as plt

def main():
    img = cv.imread('./Tasks/Opencv2/img/backyard.png')
    
    img_reg_blur = cv.blur(img, (50, 50))
    img_gaussian_blur = cv.GaussianBlur(img, (55, 55), 0, 0)
    img_median_blur = cv.medianBlur(img, 15)
    img_bilateral_blur = cv.bilateralFilter(img, 50, 75, 75)

    plt.figure(figsize=(10, 10))

    plt.subplot(3, 2, 2)
    plt.imshow(cv.cvtColor(img_reg_blur, cv.COLOR_BGR2RGB))
    plt.xticks([ ])
    plt.yticks([ ])
    plt.title("reg blur")

    plt.subplot(3, 2, 3)
    plt.imshow(cv.cvtColor(img_gaussian_blur, cv.COLOR_BGR2RGB))
    plt.xticks([ ])
    plt.yticks([ ])
    plt.title("gaussian blur")

    plt.subplot(3, 2, 4)
    plt.imshow(cv.cvtColor(img_median_blur, cv.COLOR_BGR2RGB))
    plt.xticks([ ])
    plt.yticks([ ])
    plt.title("median blur")

    plt.subplot(3, 2, 5)
    plt.imshow(cv.cvtColor(img_bilateral_blur, cv.COLOR_BGR2RGB))
    plt.xticks([ ])
    plt.yticks([ ])
    plt.title("bilateral blur")

    plt.subplot(3, 2, 1)
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.xticks([ ])
    plt.yticks([ ])
    plt.title("original")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()