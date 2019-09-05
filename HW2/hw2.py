import cv2
import matplotlib
import numpy as np

def brillo(imagen,valor_intensidad):

    for i in range(0,imagen.shape[0]):
        for j in range(0,imagen.shape[1]):
            imagen[i,j] += valor_intensidad


    return imagen

def print_resultados(imagen,imagen_brillo):
    print('*--------*--------*--------*--------*--------*--------*--------*')
    print('Imagen original: (x={}, y={})~R:{}, G:{}, B:{}'.format(50,150,imagen[50,150,2]
    ,imagen[50,150,1],imagen[50,150,0]))
    print('*--------*--------*--------*--------*--------*--------*--------*')
    print('Imagen Brillo: (x={}, y={})~R:{}, G:{}, B:{}'.format(50,150,imagen_brillo[50,150,2]
    ,imagen_brillo[50,150,1],imagen_brillo[50,150,0]))

def run():
    imagen = cv2.imread('watch.jpg')
    cv2.imshow('Imagen Original',imagen)
    imagen_brillo = brillo(imagen,2)
    cv2.imshow('Imagen con Brillo',imagen_brillo)

    print_resultados(imagen,imagen_brillo)

    if cv2.waitKey(0) == True:
        cv2.destroyAllWindows()

if __name__=='__main__':
    run()