"""Histogram in Python con OpenCv and matplotlib"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

def rgbtogray(imagen):
    """Función para convertir una imagen rgb a black and white"""
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

def histogram(image):
    vector_histogram = []
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            vector_histogram.append(image[i,j,0])

    plt.figure(1)
    plt.hist(vector_histogram, bins=max(vector_histogram))
    plt.title('Histogram of the image with the max length bins')
    plt.xlabel('Value')
    plt.ylabel('Quantity')

    plt.figure(2)
    plt.hist(vector_histogram, bins=30)
    plt.title('Histogram of the image with 30 bins')
    plt.xlabel('Value')
    plt.ylabel('Quantity')

    plt.show()

if __name__=='__main__':
    image_name = input('Ingresa el nombre de la imagen: ')
    img = cv2.imread('Images/'+image_name)
    cv2.imshow('image',img)
    image_gray = rgbtogray(img)
    cv2.imshow('image',image_gray)
    histogram(image_gray)