"""BRILLO DE LA IMAGEN A GRISES"""
def brillo(im):
    tiempoIn = time.time()
    ruta = ("C:/Users/CkriZz/Pictures/" + im)
    im = Image.open(ruta)
    im.show()
    im10 = im
    arreglo = np.array(im10.size)
    total = arreglo[0] * arreglo[1]
    i = 0
    suma = 0
    while i < im10.size[0]:
        j = 0
        while j < im10.size[1]:
            suma = suma + im10.getpixel((i, j))
            j+=1        
        i+=1
    brillo = suma / total    
    brillo = int(brillo)
    print("El brillo de la imagen es: ", brillo)
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, 'Segundos')