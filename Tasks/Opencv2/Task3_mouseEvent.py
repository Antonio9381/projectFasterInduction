import cv2 as cv 
import numpy as np 
 
x0, y0 = None, None         # The initial coordinates of the moues event 
drawing = False 
shape = "rectangle"
 
def draw_rectangle(event, x, y, flags, *params) -> None: 
    """ 
    Mouse event handling function. 
    Draws a rectangle on mouse event. 
    """ 
    global x0, y0, drawing 
 
    image, = params                         # Unpack params tuple 
    colour = [0,0,255]                      # Green 

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        x0, y0 = x, y   
    
    pt1, pt2 = (x0, y0), (x, y)
 
    if event == cv.EVENT_MOUSEMOVE and drawing:
        if shape == "rectangle":
            cv.rectangle(image, pt1, pt2, colour, -1)
        elif shape == "line":
            cv.line(image, pt1, pt2, colour, 3)

    elif event == cv.EVENT_LBUTTONUP and drawing:
        drawing = False
        if shape == "rectangle":
            cv.rectangle(image, pt1, pt2, colour, -1)
        elif shape == "line":
            cv.line(image, pt1, pt2, colour, 3)
 
    return None 
 
def main() -> None: 
    global shape

    blank = np.zeros((720, 720, 3), dtype=np.uint8)
 
    cv.namedWindow("Image")
    cv.setMouseCallback("Image", draw_rectangle, param=(blank)) 
 
    while True: 
        cv.imshow("Image", blank) 
        key = cv.waitKey(1) 
 
        if key == ord('r'):
            shape = "rectangle"
            print("Shape: rectangle")
        elif key == ord('l'):
            shape = "line"
            print("Shape: line")
        elif key == ord('d'):
            break
    
    cv.destroyAllWindows() 
 
if __name__ == "__main__": 
    main() 
