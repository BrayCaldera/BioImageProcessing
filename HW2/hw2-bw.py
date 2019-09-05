import cv2

def brillo(imagen,valor_intensidad):

    for i in range(0, imagen.shape[0]):
        for j in range(0, imagen.shape[1]):
            a = imagen[i,j]
            b = a + valor_intensidad
            if b > 255:
                b = 255
            imagen[i,j] = b

    return imagen

def run():
    imagen = cv2.imread('images/'+str(input('Ingresa el nombre de la imagen: '))
    , cv2.IMREAD_GRAYSCALE)

    intensidad = int(input('¿Cuánto brillo deseas?: '))
    imagen_brillo = brillo(imagen,intensidad)

    cv2.imwrite('images/'+str(
        input('¿Con cuál nombre quieres guardar la nueva imagen?: '))+
        '.jpg', imagen_brillo)

if __name__=='__main__':
    run()