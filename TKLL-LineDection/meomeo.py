import math
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Read image
src = cv.imread("Test3.png", cv.IMREAD_COLOR)

# Convert to grayscale image
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

# Use Canny to find edges
edges = cv.Canny(gray, 50, 200, None, 3)

cv.imshow('edges', edges)

cdst = src.copy()
cdstP = src.copy()

lines = cv.HoughLines(edges, 1, np.pi / 180, 150, None, 30, 30)

if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
        pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
        cv.line(cdst, pt1, pt2, (0,0,255), 3, cv.LINE_AA)

linesP = cv.HoughLinesP(edges, 1, np.pi / 180, 30, None, 10, 30)
if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)

cv.imshow('cdst', cdst)
cv.imshow('cdstP', cdstP)
k = cv.waitKey(0)
cv.destroyAllWindows()