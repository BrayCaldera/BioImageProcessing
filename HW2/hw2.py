import cv2
import matplotlib
import numpy as np
import time

def brillo(imagen,valor_intensidad):
    tiempoIn = time.time()

    imagen_brillo=imagen
    for i in range(0,imagen_brillo.shape[0]):
        for j in range(0,imagen_brillo.shape[1]):
            imagen_brillo[i,j] += valor_intensidad

    tiempoFin = time.time()

    print('*--------*--------*--------*--------*--------*--------*--------*')
    print('Imagen Original: (x={}, y={})~R:{}, G:{}, B:{}'.format(50,150,imagen[50,150,2]
    ,imagen[50,150,1],imagen[50,150,0]))
    print('*--------*--------*--------*--------*--------*--------*--------*')
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, 'Segundos')
    print('*--------*--------*--------*--------*--------*--------*--------*')
    print('Ejemplo de los valores que cambiaron con la función brillo')
    print('*--------*--------*--------*--------*--------*--------*--------*')
    print('Imagen Brillo: (x={}, y={})~R:{}, G:{}, B:{}'.format(50,150,imagen_brillo[50,150,2]
    ,imagen_brillo[50,150,1],imagen_brillo[50,150,0]))

    cv2.imshow('Imagen con Brillo',imagen_brillo)

def run():
    imagen = cv2.imread('watch.jpg')
    cv2.imshow('Imagen Original',imagen)
    brillo(imagen,1)

    if cv2.waitKey(0) == True:
        cv2.destroyAllWindows()

if __name__=='__main__':
    run()