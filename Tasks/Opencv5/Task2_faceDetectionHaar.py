import cv2 as cv
import matplotlib.pyplot as plt

def prepImgForFaceDetection(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.equalizeHist(gray)
    return gray

def HaarFaceDetection(img, scaleFactor = 1.1, neighbors = 5, minSize = (60, 60)):
    img_prep = prepImgForFaceDetection(img)
    
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(img_prep, scaleFactor=scaleFactor, minNeighbors=neighbors, minSize=minSize)

    print('faces found: ', len(faces))

    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return img

def main():
    img = cv.imread(".\Tasks\Opencv5\pics\sexypic.jpg")

    img_faced = HaarFaceDetection(img, scaleFactor=1.04, neighbors=5, minSize=(20, 20))

    cv.imshow('face', img_faced)

    cv.waitKey(0)
    cv.destroyAllWindows()

    cap = cv.VideoCapture("./Tasks/Opencv5/vids/rareFootageOfGOAT.mp4")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_faced = HaarFaceDetection(frame, scaleFactor=1.02, neighbors=2, minSize=(600, 600))

        frame_faced = cv.resize(frame_faced, (0, 0), fx=0.5, fy=0.5)

        cv.imshow('face', frame_faced)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()