
print("__________________________________________________________________________")
import cv2 as cv
import numpy as np
import matplotlib 


print("OpenCV", cv.__version__)
print("Numpy", np.__version__)
print("Matplotlib", matplotlib.__version__)

# img = cv.imread("castelan.png")
# cv.imshow("titulodelaventana", img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# img = cv.imread("C:\Users\jacov\OneDrive\Desktop\simasit\cisneropreciado.png")
# cv.imshow("titulodelaventana2", img)
# cv.waitKey(0)

# img = cv.imread("covarrubiasgarcia.png")
# cv.imshow("titulodelaventana3", img)
# cv.waitKey(0)

# capture = cv.VideoCapture("VID_20201101_183309.mp4")   
# while True: 
#     isTrue, frame = capture.read()
#     cv.imshow("video", frame)

#     if cv.waitKey(10) & 0xFF==ord("d"):
#         break   

# capture.release()
# cv.destroyAllWindows()


img = cv.imread("guerrabravo.png")
cv.imshow("Pruebaderesize", img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture("C:\Users\jacov\OneDrive\Desktop\simasit\VID_20201101_183309.mp4")

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow("video", frame)
    cv.imshow("video Resized", frame_resized)

    if cv.waitKey(10) & 0xFF==ord("d"):
        break   

capture.release()
cv.destroyAllWindows()




cv.waitKey(0)









