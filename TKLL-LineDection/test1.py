import cv2
import numpy as np
import matplotlib.pyplot as plt
#kich thuoc khung hinh
left= 200
right= 1100
# dinh cua hinh tam giac
y = 250
x = 550

def canny(image):
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny

def region(image):
    height = image.shape[0]
    polygons = np.array([
    [(left, height), (right, height), (x, y)]
    ])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(canny, mask)
    return masked_image

def display_Lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            print(line)
            x1, y1, x2, y2= line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0 ,0), 10)
    return line_image
image= cv2.imread('lane1.png')
lane_image = np.copy(image)
canny = canny(lane_image)
cropped_image = region(canny)
lines= cv2.HoughLinesP(cropped_image,2, np.pi/180,100 , np.array([]), minLineLength=40, maxLineGap=5)
line_image = display_Lines(lane_image, lines)
combo_image = cv2.addWeighted(lane_image, 0.8, line_image,1 , 1)
plt.imshow(canny)
plt.show()
print(image.shape[0], 'image')
#cv2.imshow("result", canny)
cv2.imshow("result", combo_image)
cv2.waitKey(0)