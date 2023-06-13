import cv2 as cv
import numpy as np
import matplotlib as mlp

met_fec = cv.imread("Imagenes_para_prueba\met_hierro_nod.jpg")
# cv.imshow("METALOGRAFIA ORIGINAL", met_fec)

met_fec_rs = cv.resize(met_fec, [int(met_fec.shape[1]//4), int(met_fec.shape[0]//4)])
cv.imshow("METALOGRAFIA ORIGINAL RESIZED", met_fec_rs)

# def translate(met_fec_rs, x, y):
#     transMat = np.float32([[1,0,x], [0,1,y]])
#     dimensions = (met_fec_rs.shape[1], met_fec.shape[0])
#     return cv.warpAffine(met_fec_rs, transMat, dimensions)

# ## -x   --- left
# ## -y   --- up
# ##  x   --- right
# ##  y   --- down

# translated = translate(met_fec_rs, 200, 10)
# cv.imshow("IMAGEN_TRANSLADADA", translated)

# ## ROTATION

# def rotate(met_fec_rs, angle, rotPoint=None):
#     (height,width) = met_fec_rs.shape[:2]

#     if rotPoint is None:
#         rotPoint = (width//2,height//2)
        
#     rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
#     dimensions = (width, height)

#     return cv.warpAffine(met_fec_rs, rotMat, dimensions)

# rotated_image = rotate(met_fec_rs, -45)
# cv.imshow("IMAGEN_ROTADA", rotated_image)

# rotated_image_2 = rotate(rotated_image,-45)
# cv.imshow("PRUEBA_2", rotated_image_2)

##RESIZED

#resized = cv.resize(met_fec, (500,500), interpolation=cv.INTER_CUBIC)
#cv.imshow("RESCALADO_IMAGEN", resized)

#FLIPPING AN IMAGEN

# flip = cv.flip(met_fec_rs, 1)
# cv.imshow("FLIP", flip)

# flip_1 = cv.flip(met_fec_rs, 2)
# cv.imshow("FLIP_1", flip_1)

# flip_2 = cv.flip(met_fec_rs, 3)
# cv.imshow("FLIP_2(-1)", flip_2)

# flip_3 = cv.flip(met_fec_rs, -3)
# cv.imshow("FLIP_3(-3)", flip_3)

##CROPING

met_fec_rec =met_fec_rs[200:400, 300:400]
cv.imshow("RECORTE",met_fec_rec)









cv.waitKey(0)