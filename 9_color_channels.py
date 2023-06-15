import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#leer y redimensionar
met_original = cv.imread("Imagenes_para_prueba\met_Zn-Al.jpg")
met_rs = cv.resize(met_original, [int(met_original.shape[1]//1), int(met_original.shape[0]//1)])
cv.imshow("METALOGRAFIA_ORIGIANL", met_rs)

#CREAR IMAGEN EN BLANCO

blank = np.zeros(met_rs.shape[:2], dtype='uint8')


## SEPARAR EN BGR

b, g, r = cv.split(met_rs)

cv.imshow('BLUE', b)
cv.imshow('RED', r)
cv.imshow('GREEN', g)

print(met_rs.shape)
print(b.shape)
print(r.shape)
print(g.shape)

## UNIR

merged = cv.merge([b, g, r])
cv.imshow('Merged Image', merged)

## SOLO UN CANAL

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('COMPONENTE EN B', blue)
cv.imshow('COMPONENTE EN G', green)
cv.imshow('COMPONENTE EN R', red)




cv.waitKey(0)