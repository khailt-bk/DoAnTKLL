import cv2 as cv2
import numpy as np
video = cv2.VideoCapture('http://192.168.0.102:8080/video')
while(True):
    ret, frame = video.read()
    resize_fr = cv2.resize(frame, (600, 400))
    gray = cv2.cvtColor(resize_fr, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 100)
    cv2.imshow('frame', resize_fr)
    if cv2.waitKey(1) == ord('f'):
        cv2.imshow('frame', canny)
        np.savetxt('Video.txt', (canny), delimiter=' ', fmt="%d")
    if cv2.waitKey(1) == ord('q'):
        break
video.release()
# data = np.loadtxt("Video.txt", delimiter=" ",dtype=int , skiprows=1)
print(data)
cv2.destroyAllWindow()



