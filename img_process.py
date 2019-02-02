import cv2 as cv
import numpy as np

def Graying(img):
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)

def Hsving(img):
    return cv.cvtColor(img, cv.COLOR_BGR2HSV)

def Thresholding(Gray_img):
    return cv.threshold(Gray_img, 120, 255, cv.THRESH_BINARY)

def Resizing(img):
    return cv.resize(img, (img.shape[0]//2, img.shape[1]//2))

def Averaging(img):
    return cv.blur(img, (5, 5))

def Boxing(img):
    return cv.boxFilter(img, -1, (5, 5), normalize=1)

def Mediuming(img):
    return cv.medianBlur(img, 5)

def Gaussing(img):
    return cv.GaussianBlur(img, (5, 5), 0)

def Sobeling(Gray_img):
    Sobel_x = cv.Sobel(Gray_img, cv.CV_64F, 1, 0, 3)
    Sobel_y = cv.Sobel(Gray_img, cv.CV_64F, 0, 1, 3)
    Sobel_x_img = cv.convertScaleAbs(Sobel_x)
    Sobel_y_img = cv.convertScaleAbs(Sobel_y)
    return cv.addWeighted(Sobel_x_img, 0.5, Sobel_y_img, 0.5, 0)

def Laplacing(Gray_img):
    return cv.Laplacian(Gray_img, cv.CV_64F, 3)

def Cannying(Gray_img):
    return cv.Canny(Gray_img, 50, 200)

def img_inversion(img):
    '''
    功能: 对二值图像进行反转
    :param img: 二值图像
    :return: 反转的二值图像
    '''
    dst = np.zeros((img.shape[0], img.shape[1], 1), np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # 遍历图像的所有灰度像素
            Pixel = img[i][j]
            dst[i][j] = 255 - Pixel
    return dst
