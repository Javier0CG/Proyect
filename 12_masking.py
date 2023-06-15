import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#LEER Y REDIMENSIONAR

met_original = cv.imread("Imagenes_para_prueba\met_Zn-Al.jpg")
met_rs = cv.resize(met_original, [int(met_original.shape[1]//1), int(met_original.shape[0]//1)])
cv.imshow("METALOGRAFIA_ORIGIANL", met_rs)

#CREAR IMAGEN EN BLANCO

blank = np.zeros(met_rs.shape[:2], dtype='uint8')
cv.imshow('BLANK', blank)

#mask = cv.circle(blank, (met_rs.shape[1]//2, met_rs.shape[0]//2 + 45), 100, 255, -1)
#cv.imshow("MASCARA", mask)

##WE CAN CHANGE THE SHAPE

#PRUEBA CON FIGURAS MIX
circle = cv.circle(blank.copy(), (met_rs.shape[1]//2 + 45, met_rs.shape[0]//2 + 45), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)


# shape_combination

mix_shape = cv.bitwise_and(circle, rectangle)
cv.imshow("FIGURAS MIX", mix_shape)

#MASCARA CON CIRCULO

# masked = cv.bitwise_and(met_rs, met_rs, mask=mask)
# cv.imshow("MASCARA CON METALOGRAFIA", masked)

#MASCARA CON FIGURAS COMBINADAS

masked_2 = cv.bitwise_and(met_rs, met_rs, mask=mix_shape)
cv.imshow("MASCARA CON METALOGRAFIA", masked_2)



cv.waitKey(0)
