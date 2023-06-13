import cv2 as cv
import matplotlib as mlp
import numpy as np

print("______________________________________")
print("Open CV version:", cv.__version__)
print("Matplotlib version:", mlp.__version__)
print("Numpy version:", np.__version__)
print("______________________________________")

# # def diHola():
# #     print("HOLA")

# # diHola()

# # def Hola_con_nombre(nombre):
# #     print ("Hola" + nombre + "!")

# # Hola_con_nombre("Anne")

# # #Funcion con multiples parametros con sentencia de retorno

# # def multiplicacion(valor_1, valor_2):
# #     return valor_1*valor_2

# # print(multiplicacion(5,10000))

# print("ingresa tu nombre")
# nombre = input()

# print("hola", nombre)
# print(nombre, "cuantas manzanas tenias?")
# manzanas_iniciales = input()
# manzanas_iniciales = int(manzanas_iniciales)
# print("tenias " + str(manzanas_iniciales) + " manzanas")


# print(nombre, "cuantas manzanas te comiste")
# manzanas_comidas = input()
# manzanas_comidas = int(manzanas_comidas)
# print("te comiste " + str(manzanas_comidas) + " manzanas")

# def resta (manzanas_iniciales, manzanas_comidas):
#     print("YYYYYYYYYYYYYY te quedan " + str(manzanas_iniciales-manzanas_comidas) + " manzanas")

# print("prueba de funcion")
# resta(manzanas_iniciales,manzanas_comidas)

# resta(40,10)


# #Calcular el volumen 

# def calculo_volumen (largo, ancho, alto):
#     return (largo * ancho * alto)

# print(calculo_volumen(5, 5, 5))
# print(calculo_volumen(10, 15, 2))


#FOR


# iterable = [4, 5, 16, 984, 4]

# for elemento in iterable:
#     print(elemento * 654)


# print("prueba para diccionarios")
# diccionario = {"elemento_1" : 456, "elemento_2" : 4985, "elemento_3" : 555, "elemento_5" : .12}

# for k in diccionario:
#     print(k)

# for v in diccionario.values():
#     print(v)

# for k, v in diccionario.items():
#     print(k, "el valor del elemento es", v)

# for i in range(3):
#     print(i)

# for i_1 in range(20,30):
#     print(i_1)

# for i_2 in range(20,100,5):
#     print(i_2)

# coleccion = [2, 4, 6, 7, 8, 9, 10, 12, 15, 20]
# for e in coleccion:
#     if e == 15:
#         break
#     print(e)

# print("__________para numeros pares______")
# for e in coleccion:
#     if e % 2 !=0:
#         continue
#     print(e)

# print("____________para e<10___________________")

# for e in coleccion:
#     if e < 10:
#         continue
#     print(e)

# print("____________para e>10___________________")

# for e in coleccion:
#     if e > 10:
#         continue
#     print(e)

# print("____________para e==10___________________")

# for e in coleccion:
#     if e == 10:
#         continue
#     print(e)

# for e in coleccion:
#     if e == 10:
#         break

# numeracion = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# numdelista = int(input("tu numero de lista"))

# for element in numeracion:
#     if element == numdelista:
#         break
# else:
#     print("no se encontro el numero")

##Escriba un programa que pida la anchura y altura de un rectángulo y lo dibuje con caracteres producto (*):

# anchura = int(input("introduce la anchura: "))
# altura = int(input("introduce la altura: "))
# profundidad = int(input("introduce la profundidad"))

# print(anchura, altura)

# for i in range(altura):
#     for j in range(anchura):
#         print("* ", end="")
#     print()

# for i_1 in range(altura):
#     for j_1 in range(anchura):
#         print(i_1, "   ", end="")
#     print()

# for i_1 in range(10):
#     for j_1 in range(12):
#         print(j_1, "   ", end="")
#     print("__________________")

# lista_2 = ["juan", "javier", "josue", "adolfo", "ale"]

# for i_2 in lista_2:
#     for j_2 in lista_2:
#         print(i_2)
#     print("______________________")

##Escriba un programa que pida la anchura y altura de un rectángulo y el caracter a utilizar en el dibujo:

# anchura = int(input("introduce la anchura: "))
# altura = int(input("introduce la altura: "))
# figura = input("introduce la figura: ")

# for i_3 in range(10):
#     for j_3 in range(12):
#         print(j_3, end="     ")
#     print()

# for contador in range(10):
#     print(contador)

# arreglo_numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# for decena in arreglo_numeros:
#     for docena in arreglo_numeros:
#         print (decena/10, end="     ")
#     print()

# print()
# numero = 1
# print("El numero incicial es", numero)

# while numero <= 10: 
#     print(numero)
#     numero +=2


# print("DONE")


# def saludo(nombre, apellido):
#     print("hola", nombre, apellido)


# saludo("Javier", "Covarrubias")
# saludo("alan", "ochoa")
# saludo("alpha", 654656545)

# lista_nombres = ["javier", "alan", "su", "albert", "fer", "dian", "alph"]

# for nombre in lista_nombres:
#     print ("hola", nombre)

# def numero(numero_1, numero_2, numero_3):
#     num_1 = numero_1 + 456
#     num_2 = numero_2 + 687
#     num_3 = numero_3 + 874
#     return num_1 + num_2 + num_3


# print(numero(1000000000, 15, 20))





    

 




         
















