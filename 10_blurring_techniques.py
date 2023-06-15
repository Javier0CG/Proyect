import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#leer y redimensionar
met_original = cv.imread("Imagenes_para_prueba\met_Zn-Al.jpg")
met_rs = cv.resize(met_original, [int(met_original.shape[1]//1), int(met_original.shape[0]//1)])
cv.imshow("METALOGRAFIA_ORIGIANL", met_rs)

#CREAR IMAGEN EN BLANCO

# blank = np.zeros(met_rs.shape[:2], dtype='uint8')

#AVERAGING

met_rs_average = cv.blur(met_rs, (7,7))
cv.imshow('METALOGRAFIA CON FILTRO PROMEDIO', met_rs_average)

#GAUSSIAN

met_rs_gaussian = cv.GaussianBlur(met_rs, (7,7), 0)
cv.imshow('METALOGRAFIA CON FILTRO GAUSSIANO', met_rs_gaussian)

#MEDIAN 

met_rs_median = cv.medianBlur(met_rs, 7)
cv.imshow('METALOGRAFIA CON MEDIAN', met_rs_median)

#BILATERAL

met_rs_bilateral = cv.bilateralFilter(met_rs, 5, 15, 15)
cv.imshow('METALOGRAFIA CON BILATERAL', met_rs_bilateral)









cv.waitKey(0)
