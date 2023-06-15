import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#leer y redimensionar
met_original = cv.imread("Imagenes_para_prueba\met_hierro_nod.jpg")
met_rs = cv.resize(met_original, [int(met_original.shape[1]//3), int(met_original.shape[0]//3)])
cv.imshow("METALOGRAFIA_ORIGIANL", met_rs)


#CAUTION PLT IN RGB
plt.imshow(met_rs)
plt.show()

# met_rs_gray = cv.cvtColor(met_rs, cv.COLOR_BGR2GRAY)
# cv.imshow('METALOGRAFIA EN ESCALA DE GRISES', met_rs_gray)

# ## BGR 2 HSV

# met_rs_hsv = cv.cvtColor(met_rs, cv.COLOR_BGR2HSV)
# cv.imshow("METALOGRAFIA TRANSFORMADA A HSV", met_rs_hsv)

# ## BGR 2 L*a*b

# met_rs_lab = cv.cvtColor(met_rs, cv.COLOR_BGR2LAB)
# cv.imshow('METALOGRAFIA TRANSFORMADA A Lab', met_rs_lab)






# cv.waitKey(0)
# cv.destroyAllWindows