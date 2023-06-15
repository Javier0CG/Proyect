import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#leer y redimensionar
# met_original = cv.imread("Imagenes_para_prueba\met_Zn-Al.jpg")
# met_rs = cv.resize(met_original, [int(met_original.shape[1]//1), int(met_original.shape[0]//1)])
# cv.imshow("METALOGRAFIA_ORIGIANL", met_rs)

#CREAR IMAGEN EN BLANCO

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370,370), 255, -1) 
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('RECTANGULO', rectangle)
cv.imshow('CIRCULO', circle)

##BITWISE AND

bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('BITWISE AND', bitwise_and)

## bitwise or

bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("BIWISE OR", bitwise_or)

## BITWISE XOR

bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('BITWISE XOR', bitwise_xor)

## BITWISE NOT

bitwise_not = cv.bitwise_not(circle, rectangle)
cv.imshow('bitwise not', bitwise_not)
















cv.waitKey(0)
