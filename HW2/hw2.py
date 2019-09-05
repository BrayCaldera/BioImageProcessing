import cv2
import matplotlib
import numpy as np

def brillo(imagen,valor_intensidad):

    for i in range(0, imagen.shape[0]):
        for j in range(0, imagen.shape[1]):
            a = imagen[i,j]
            b = a + valor_intensidad
            if b > 255:
                b = 255
            imagen[i,j] = b

    return imagen

def print_resultados(imagen,imagen_brillo):
    print('*--------*--------*--------*--------*--------*--------*--------*')
    print('Imagen original: (x={}, y={})~L:{}'.format(50,150,imagen[50,150]))
    print('*--------*--------*--------*--------*--------*--------*--------*')
    print('Imagen Brillo: (x={}, y={})~L:{}'.format(60,160,imagen_brillo[60,160]))

def run():
    imagen = cv2.imread(str(input('Ingresa el nombre de la imagen: '))
    , cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Imagen Original',imagen)
    imagen_brillo = brillo(imagen,50)
    cv2.imshow('Imagen con Brillo',imagen_brillo)

    print_resultados(imagen,imagen_brillo)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    run()