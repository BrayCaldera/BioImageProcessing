"""Programa para Convertir una imagen rgb a grayscale"""

import cv2
from math import floor

def brillo(imagen):
    """Función para aumentar el brillo de una imagen BW pixel por pixel"""
    new_image = imagen
    for i in range(0, imagen.shape[0]):
        for j in range(0, imagen.shape[1]):
            new_blue = int(imagen[i,j,0])
            new_green = int(imagen[i,j,1])
            new_red = int(imagen[i,j,2])
            avg_of_channels = new_blue + new_green + new_red // 3
            if avg_of_channels > 255:
                avg_of_channels = 255
            new_image[i,j] = avg_of_channels

    return new_image

def run():
    imagen = cv2.imread('images/'+str(input('Ingresa el nombre de la imagen: ')), 
    cv2.IMREAD_COLOR)
    
    imagen_brillo = brillo(imagen)

    cv2.imwrite('images/'+str(
        input('¿Con cuál nombre quieres guardar la nueva imagen?: '))+
        '.jpg', imagen_brillo)

if __name__=='__main__':
    run()
