
print("__________________________________________________________________________")
import cv2 as cv
import numpy as np
import matplotlib

print("OpenCV", cv.__version__)
print("Numpy", np.__version__)
print("Matplotlib", matplotlib.__version__)

img = cv.imread("castelan.png")
cv.imshow("titulodelaventana", img)
cv.waitKey(0)
cv.destroyAllWindows()








