print("_______________________")
import cv2 as cv

print("_______________________")

img = cv.imread("Imagenes_para_prueba\linx.jpg")
# cv.imshow("ORIGINAL", img)
img_2 = cv.imread("Imagenes_para_prueba\met319.png")
# cv.imshow("319", img_2)
img_3 = cv.imread("Imagenes_para_prueba\met354.png")
# cv.imshow("354", img_3)
img_4 = cv.imread("Imagenes_para_prueba\met390.png")
# cv.imshow("390", img_4)
img_5 = cv.imread("Imagenes_para_prueba\met_alum.jpg")
# cv.imshow("390", img_5)
img_6 = cv.imread("Imagenes_para_prueba\met_Zn-Al.jpg")
# cv.imshow("390", img_6)
img_7 = cv.imread("Imagenes_para_prueba\met_hierro_nod.jpg")
# cv.imshow("390", img_7)

lista = [img, img_2, img_3, img_4]

# #CONVERT TO GRAY

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("GRAY", gray)


# ##BLUR

# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow("PRUEBA_BLUR", blur)

#EDGE CASCADE (CANNY)

# canny = cv.Canny(img_7, 100, 100)
# cv.imshow("PRUEBA_CANNY",canny)

#RESCALE IMAGES

hierro_nod = cv.resize(img_7, [int(img_7.shape[1]//2), int(img_7.shape[0]//2)])
# cv.imshow("ORIGINAL", img_7)
# cv.imshow("PRUEBA DE REESCALADO", hierro_nod)

# print(img_7.shape)
# print(hierro_nod.shape)


#DILATING THE IMAGE

# dilated_image = cv.dilate(hierro_nod, (3,3), iterations=5)
# cv.imshow("PRUEBA_DILATACION_HIERRO", dilated_image)

# canny = cv.Canny(dilated_image, 200, 200)
# cv.imshow("PRUEBA_CANNY_DILATED_HIERRO",canny)

#ERODE IMAGES

# imagenes = [hierro_nod, hierro_nod, hierro_nod, hierro_nod, hierro_nod, hierro_nod, hierro_nod, hierro_nod, hierro_nod, hierro_nod]
# nu_iterations = [1, 2, 3, 4, 5, 6, 7, 10, 15, 50]

# eroded = cv.erode(hierro_nod, (3,3),iterations=1)
# cv.imshow("original", hierro_nod)
# cv.imshow("eroded", eroded)

##RESIZE IMAGES

# image_resized_cubic = cv.resize(img_7, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow("RESIZED_WITH_CUBIC", image_resized_cubic)

# image_resized_linear = cv.resize(img_7, (500,500), interpolation=cv.INTER_LINEAR)
# cv.imshow("RESIZED_WITH_LINEAR", image_resized_linear)

# image_resized = cv.resize(img_7, (500,500))
# cv.imshow("RESIZED_WITHOUT_INTERPOLATION", image_resized)


##CROPPING

croping_image = img_7[100:750, 200:400]
croping_image_2 = img_7[0:100, 200:400]

cv.imshow("11111111", croping_image)
cv.imshow("222222222", croping_image_2)

print(img_7.shape)
print(croping_image.shape)



cv.waitKey(0)
cv.destroyAllWindows()

