import cv2
import matplotlib
import numpy as np

def cargar_imagen(nombre_imagen):
    img = cv2.imread(nombre_imagen)
    cv2.imshow('image',img[:,:,0])
    if cv2.waitKey(0) == True:
        cv2.destroyAllWindows()
    cv2.imshow('image',img[:,:,1])
    if cv2.waitKey(0) == True:
        cv2.destroyAllWindows()
    cv2.imshow('image',img[:,:,2])
    if cv2.waitKey(0) == True:
        cv2.destroyAllWindows()

def run():
    cargar_imagen('watch.jpg')
    if cv2.waitKey(0) == True:
        cv2.destroyAllWindows()
    #aumentar_brillo()

if __name__=='__main__':
    run()