# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
# Tao duong dan toi file anh
path = r'D:\pythonProject1\pic\anhthucte.jpg'
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread(path)
# Kiem tra anh truoc xu ly
cv2.imshow('anhthucte',img)
cv2.waitKey(2000)
# Su dung thuat toan
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))
# Loc bộ lọc Sobel theo phuong ngang va phuong thang dung
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelX = np.uint8(np.absolute(sobelX))
# Loc bộ lọc Sobel theo phuong ngang va phuong thang dung
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))
# Loc bộ lọc Sobel theo phuong ngang va phuong thang dung
sobelCombined = cv2.bitwise_or(sobelX, sobelY)
# Bien so 100 va 150 co su tham doi
# Ket qua theo loc Candy
edges = cv2.Canny(img,100,150)
# Tao file chua cac anh can xu ly
titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombined', 'Canny']
images = [img, lap, sobelX, sobelY, sobelCombined, edges]

for i in range(6):
    # Chuyen anh ve file 8-bit de xu ly
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
