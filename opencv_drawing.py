import numpy as np
import cv2 as cv

def nothing(x):
    pass

def paint(event, x, y, flags, param):
    global ix, iy, img, size, r, g, b

    if event == cv.EVENT_LBUTTONDOWN:
        ix, iy = x, y
        cv.circle(img, (ix, iy), size, (b, g, r), -1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        cv.circle(img, (x, y), size, (b, g, r), -1)

#Tworzy pole do rysowania w dowolnym kolorze
img = np.zeros((400, 800, 3), np.uint8)  #Wielkość okna
cv.namedWindow('image')  #Nazwa okna

#Stwórz suwaki R G B
cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)

#Wielkość pędzla
size_label = 'Size: 0 : OFF \n1 : ON'
cv.createTrackbar(size_label, 'image', 0, 100, nothing)

#Stworzenie suwaka do włączenia gumki
rubber_on_off = 'Rubber: 0 : OFF \n1 : ON'
cv.createTrackbar(rubber_on_off, 'image', 0, 1, nothing)

ix, iy = -1, -1
size = 0
r = 0
g = 0
b = 0
rubber = 0

cv.setMouseCallback('image', paint)

#Pętla utrzymująca okno
while True:
    #klawisz esc = wyłączenie
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    #Sprawdzenie aktualnego położenia suwaków
    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')
    s = cv.getTrackbarPos(size_label, 'image')
    rubber = cv.getTrackbarPos(rubber_on_off, 'image')

    #Ustawienie wielkości pędzla
    if s == 0:
        size = 0
    else:
        size = s

    if rubber == 0:
    	continue
    else:
    	r,g,b = 0,0,0

cv.destroyAllWindows()