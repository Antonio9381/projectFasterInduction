import cv2 as cv

def main():
    cap = cv.VideoCapture("./Tasks/Opencv3/vids/Gandalf_laugh.mp4")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        _, thresholded_frame = cv.threshold(frame_gray, 140, 255, cv.THRESH_BINARY)
        thresholded_adaptive = cv.adaptiveThreshold(frame_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, -2)

        cv.imshow("thres vid", thresholded_frame)
        cv.imshow("adapt thres vid", thresholded_adaptive)

        if cv.waitKey(17) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()