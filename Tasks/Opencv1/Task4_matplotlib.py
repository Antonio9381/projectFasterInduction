import cv2 as cv
import matplotlib.pyplot as plt

def main(): 
    img = cv.imread("./Tasks/Opencv1/photos/sexypic.jpg") 
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    plt.imshow(img)
    plt.axis('off')
    plt.title("leGOATs")
    plt.show()

if __name__ == "__main__": 
    main()