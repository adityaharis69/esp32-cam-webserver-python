import cv2
import numpy as np
import urllib.request

url='http://192.168.100.81/cam-hi.jpg'

win_nama='ESP32'
cv2.namedWindow(win_nama,cv2.WINDOW_AUTOSIZE)

while(1):
    imgResponse=urllib.request.urlopen(url)
    imgNP=np.array(bytearray(imgResponse.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNP,-1)

    cv2.imshow(win_nama,img)
    keluar=cv2.waitKey(1) & 0xFF
    if keluar ==27:
        break
cv2.destroyAllWindows()

