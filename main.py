import easyocr
import cv2
from time import sleep
reader = easyocr.Reader([ 'en' ]) # this needs to run only once to load the model into memory

camera = cv2.VideoCapture( 0 )

while True:
    return_value, image = camera.read()
    cv2.imshow( 'Lectura de Camara', image )
    cv2.imwrite( 'placa.jpg', image )
    result = reader.readtext( 'placa.jpg' )
    sleep( 300 )
    print( result )
