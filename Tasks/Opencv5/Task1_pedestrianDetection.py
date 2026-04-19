import cv2 as cv
import matplotlib.pyplot as plt

def main():
    cap = cv.VideoCapture("./Tasks/Opencv5/vids/siJingPingEyes.mp4")

    background_sub = cv.createBackgroundSubtractorMOG2()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        bg_mask = background_sub.apply(frame)
        #background sub make anything that moves in the video white and the rest black, so we can easily detect pedestrians

        ppl_mor = cv.morphologyEx(bg_mask, cv.MORPH_OPEN, cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5)), iterations=2)

        img_white = cv.inRange(ppl_mor, (127), (255))

        img_morph = cv.morphologyEx(img_white, cv.MORPH_CLOSE, cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5)), iterations=6)

        img_open = cv.morphologyEx(img_morph, cv.MORPH_OPEN, cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5)), iterations=2)

        # cv.imshow('Pedestrian Detection', img_morph)

        cnt, _ = cv.findContours(img_open, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        for i in cnt:
            area = cv.contourArea(i)
            if area < 500:
                continue

            x,y,w,h = cv.boundingRect(i)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv.imshow('Pedestrian Detection', frame)

        if cv.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()