"""Programa para realizar el cambio de brillo entre canales"""

import cv2

def brillo_azul(imagen,valor_intensidad):
    """Función para aumentar el brillo de una imagen BW pixel por pixel"""
    for i in range(0, imagen.shape[0]):
        for j in range(0, imagen.shape[1]):
            a = imagen[i,j][0]
            b = a + valor_intensidad
            if b > 255:
                b = 255
            imagen[i,j][0] = b

    return imagen

def brillo_verde(imagen,valor_intensidad):
    pass

def brillo_rojo(imagen,valor_intensidad):
    pass

def run():
    imagen = cv2.imread('images/'+str(input('Ingresa el nombre de la imagen: ')))

    cv2.imshow('Imagen Original',imagen)

    intensidad_canal_azul = int(input('¿Cuánto brillo deseas en el canal azul?: '))
    intensidad_canal_verde = int(input('¿Cuánto brillo deseas en el canal verde?: '))
    intensidad_canal_rojo = int(input('¿Cuánto brillo deseas en el canal rojo?: '))

    imagen_brillo_azul = brillo_azul(imagen,intensidad_canal_azul)
    imagen_brillo_azul = brillo_verde(imagen,intensidad_canal_azul)
    imagen_brillo_azul = brillo_rojo(imagen,intensidad_canal_azul)

    cv2.imwrite('images/'+str(
        input('¿Con cuál nombre quieres guardar las nuevas imagenes?: '))+
        '.jpg', imagen_brillo_azul)

if __name__=='__main__':
    run()
