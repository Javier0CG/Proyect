import cv2 as cv
import matplotlib as mlp


img = cv.imread("Imagenes_para_prueba\VID_20201101_183309.mp4")

def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[1] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


#For reading videos
capture = cv.VideoCapture("Imagenes_para_prueba\VID_20201101_183309.mp4")

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow("Video", frame)
    cv.imshow("Video resized", frame_resized)

    if cv.waitKey(100) & 0xFF==ord("d"):
        break


capture.release()
cv.destroyAllWindows()


# cv.waitKey(0)