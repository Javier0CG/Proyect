import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype="uint8")
cv.imshow("Blank", blank)

# img = cv.imread("Imagenes_para_prueba\prueba_segmentacion_SAM.png")
# cv.imshow("castelan", img)

#oaint the image
# blank[200:300, 300:400] = 0,255,0
# cv.imshow("green", blank)

# cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=cv.FILLED)
# cv.imshow("rectangle", blank)

# ##DRAW A CIRCLE

# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=6)
# cv.imshow("circle", blank)

# # print(blank.shape)
# # print(blank.shape[0]//2)
# # print(blank.shape[1]//2)
# # print(blank.shape[2]//2)

# #DRAW A LINE

# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
# cv.imshow("line", blank)

##WRITE TEXT

cv.putText(blank, "hello world", (250,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0),2)
cv.imshow("Text", blank)




cv.waitKey(0)
