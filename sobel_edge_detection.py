import cv2
import numpy as np
from IPython.display import Image

def sobel_edge_detection(image_path, output, blur_ksize, sobel_ksize, skipping_threshold):
    """
    image_path: link to image
    blur_ksize: kernel size parameter for Gaussian Blurry
    sobel_ksize: size of the extended Sobel kernel; it must be 1, 3, 5, or 7.
    skipping_threshold: ignore weakly edge
    """
    # read image
    img = cv2.imread(image_path)
    
    # convert BGR to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gaussian = cv2.GaussianBlur(gray, (blur_ksize, blur_ksize), 0)
    
    # sobel algorthm use cv2.CV_64F
    sobelx64f = cv2.Sobel(img_gaussian, cv2.CV_64F, 1, 0, ksize=sobel_ksize)
    abs_sobel64f = np.absolute(sobelx64f)
    img_sobelx = np.uint8(abs_sobel64f)

    sobely64f = cv2.Sobel(img_gaussian, cv2.CV_64F, 1, 0, ksize=sobel_ksize)
    abs_sobel64f = np.absolute(sobely64f)
    img_sobely = np.uint8(abs_sobel64f)
    
    # calculate magnitude
    img_sobel = (img_sobelx + img_sobely)/2
    
    # ignore weakly pixel
    for i in range(img_sobel.shape[0]):
        for j in range(img_sobel.shape[1]):
            if img_sobel[i][j] < skipping_threshold:
                img_sobel[i][j] = 0
            else:
                img_sobel[i][j] = 255

    cv2.imwrite(output,img_sobel)
    return img_sobel
    


if __name__ == "__main__":
    image_path = 'image_1.jpg'
    output = 'image_sobel.jpg'
    blur_ksize = 7
    sobel_ksize = 1
    skipping_threshold = 30
    sobel_edge_detection(image_path = image_path, blur_ksize=blur_ksize, output = output,
                               sobel_ksize=sobel_ksize, skipping_threshold=skipping_threshold)
    # Image(img2)

    # python3 -m sobel_edge_detection