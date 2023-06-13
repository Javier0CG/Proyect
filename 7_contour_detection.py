import cv2 as cv

#leer y redimensionar
met_original = cv.imread("Imagenes_para_prueba\met_hierro_nod.jpg")
met_rs = cv.resize(met_original, [int(met_original.shape[1]//3), int(met_original.shape[0]//3)])
cv.imshow("METALOGRAFIA_ORIGIANL", met_rs)


#convertir a escala de grises
met_rs_gray = cv.cvtColor(met_rs, cv.COLOR_BGR2GRAY) 
cv.imshow("METALOGRAFIA_REDIMESIONADA_GRIS", met_rs_gray)

#FILTRO GAUSSIANO

met_rs_gray_gauss = cv.GaussianBlur(met_rs_gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow("METALOGRAFIA_RS_G_GS", met_rs_gray_gauss)

#THRESHOLD

ret, thresh = cv.threshold(met_rs_gray, 50, 255, cv.THRESH_BINARY)
cv.imshow("METALOGRAFIA_RS_GRAY_THRESH", thresh)


#CONTOUR DETECTION (CANNY)

met_r_g_cy_gs = cv.Canny(met_rs_gray_gauss, 125, 175)
cv.imshow("METALOGRAFIA_RS_GRAY_GAUSS_CANNY", met_r_g_cy_gs)

met_rs_gray_gauss_3sh = cv.Canny(thresh, 125 , 175)
cv.imshow("METALOGRAFIA_RS_GRAY_GAUSS_3SH_CANNY", met_rs_gray_gauss_3sh)


contours, hierarchies = cv.findContours(met_r_g_cy_gs, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

















cv.waitKey(0)
