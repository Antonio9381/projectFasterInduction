import cv2 as cv

def main():
    cap = cv.VideoCapture("./Tasks/Opencv2/vids/Gandalf_laugh.mp4")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        blurred_frame = cv.bilateralFilter(frame, 15, 50, 50)

        cv.imshow("Blurred Video", blurred_frame)

        if cv.waitKey(7) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()