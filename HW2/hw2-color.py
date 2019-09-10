"""Programa para realizar el cambio de brillo entre canales"""

import cv2

def brillo_azul(imagen,valor_intensidad):
    """Función para aumentar el brillo de un canal pixel por pixel"""
    for i in range(0, imagen.shape[0]):
        for j in range(0, imagen.shape[1]):
            a = imagen[i,j][0]
            b = a + valor_intensidad
            if b > 255:
                b = 255
            imagen[i,j][0] = b

    return imagen

def brillo_verde(imagen,valor_intensidad):
    """Función para aumentar el brillo de un canal pixel por pixel"""
    for i in range(0, imagen.shape[0]):
        for j in range(0, imagen.shape[1]):
            a = imagen[i,j][1]
            b = a + valor_intensidad
            if b > 255:
                b = 255
            imagen[i,j][1] = b

    return imagen

def brillo_rojo(imagen,valor_intensidad):
    """Función para aumentar el brillo de un canal pixel por pixel"""
    for i in range(0, imagen.shape[0]):
        for j in range(0, imagen.shape[1]):
            a = imagen[i,j][2]
            b = a + valor_intensidad
            if b > 255:
                b = 255
            imagen[i,j][2] = b

    return imagen

def run():
    imagen = cv2.imread('images/'+str(input('Ingresa el nombre de la imagen: ')))

    cv2.imshow('Imagen Original',imagen)

    intensidad_canal_azul = int(input('¿Cuánto brillo deseas en el canal azul?: '))
    intensidad_canal_verde = int(input('¿Cuánto brillo deseas en el canal verde?: '))
    intensidad_canal_rojo = int(input('¿Cuánto brillo deseas en el canal rojo?: '))

    imagen_brillo_azul = brillo_azul(imagen,intensidad_canal_azul)
    imagen_brillo_verde = brillo_verde(imagen,intensidad_canal_azul)
    imagen_brillo_rojo = brillo_rojo(imagen,intensidad_canal_azul)

    nombre_image_nueva=input('¿Con cuál nombre quieres guardar las nuevas imagenes?: ')
    cv2.imwrite('images/'+nombre_image_nueva+'-blue.jpg', imagen_brillo_azul)
    cv2.imwrite('images/'+nombre_image_nueva+'-green.jpg', imagen_brillo_verde)
    cv2.imwrite('images/'+nombre_image_nueva+'-red.jpg', imagen_brillo_rojo)

if __name__=='__main__':
    run()
