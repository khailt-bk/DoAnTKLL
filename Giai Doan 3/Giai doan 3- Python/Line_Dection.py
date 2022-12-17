import cv2
import numpy as np
max_slider = 100
# Read image
img = cv2.imread('Picture 1.jpg', cv2.IMREAD_COLOR) # road.png is the filename
img = cv2.resize(img, (100,50))

red = cv2.imread('RED.png', cv2.IMREAD_COLOR)
red = cv2.resize(red, (100,50))

# Convert the image to gray-scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Find the edges in the image using canny detector
edges = cv2.Canny(gray, 50, 200)
# Detect points that form a line
lines = cv2.HoughLinesP(edges, 1, np.pi/180, max_slider, minLineLength=10, maxLineGap=250)
# Draw lines on the image
# for line in lines:
#     x1, y1, x2, y2 = line[0]
#     cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
# Show result
# np.savetxt('testcase_4.txt', (edges)/255, delimiter=',',fmt="%d", newline=' ] \n [ ')
data = np.loadtxt('Output1.txt', delimiter=' ',dtype= int , usecols=range(100))
print(data.shape)
# print(red)
# red = cv2.cvtColor(red, cv2.COLOR_BGR2GRAY)

for i in range(50):
    for j in range(100):
        if(data[i][j]== 0):
            red[i][j] = 0

# print(red)

Line_STM32 = cv2.addWeighted(img,0.8 ,red,1,1)
Line_STM32 = cv2.resize(Line_STM32, (600,300))
# print(Line_STM32)
cv2.imshow("Result Image", Line_STM32)
k = cv2.waitKey(0)



print(img.shape)
print(red.shape)
