import numpy as np
import cv2 as cv
# criando uma imagem preta
img= np.zeros((512,512,3), np.uint8)
#criando uma linha horizontal azul
cv.line(img, (0,250), (500,250), (255,0,0),5)

font=cv.FONT_HERSHEY_DUPLEX
cv.putText(img,'OpenCV',(10,240), font, 4, (255,255,255),2, cv.LINE_AA)
cv.namedWindow ('carregando a imagem')
cv.imshow('carregando a imagem', img) 
k=cv.waitKey()