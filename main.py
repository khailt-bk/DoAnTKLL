import cv2                                      #nhap vao thu vien cv2
import numpy as np                              #nhan numpy duoi dang np
img = cv2.imread('Test5.png')                   #doc vao hinh anh
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    #chuyen doi hinh anh thanh hinh anh co tham do xam de giam do phuc tap khi su dung filter Canny
l_th = 200                                      #low threshold cua filter Canny
u_th = l_th + 100                               #high threshold cua filter Canny
edges = cv2.Canny(gray, l_th, u_th, apertureSize=3)  # filter phat hien canh
# cv2.imshow('ed', edges)
# cv2.waitKey(0)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 87) # thuat toan Hough Line Transform
if lines is not None:
    for line in lines:
        rho,theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        # x1 stores the rounded off value of (r * cos(theta) - 1000 * sin(theta))
        x1 = int(x0 + 1000 * (-b))
        # y1 stores the rounded off value of (r * sin(theta) + 1000 * cos(theta))
        y1 = int(y0 + 1000 * a)
        # x2 stores the rounded off value of (r * cos(theta) + 1000 * sin(theta))
        x2 = int(x0 - 1000 * (-b))
        # y2 stores the rounded off value of (r * sin(theta) - 1000 * cos(theta))
        y2 = int(y0 - 1000 * a)
        cv2.line(img, (x1,y1), (x2,y2), (0, 0, 255), 2) #vector dau ra voi hai phan tu r, theta

cv2.imshow('image', img)    #show ket qua la hinh anh voi cac duong thang
k = cv2.waitKey(0)
cv2.destroyAllWindows()