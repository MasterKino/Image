
from img_process import *
import cv2 as cv
# 计时起点
e1 = cv.getTickCount()
# 读取图像
img01 = cv.imread('boy01.png')
img02 = cv.imread('boy02.png')
img03 = cv.imread('boy03.png')
img04 = cv.imread('boy04.png')
img05 = cv.imread('boy05.png')
img06 = cv.imread('boy06.png')
img07 = cv.imread('boy07.png')
img08 = cv.imread('boy08.png')
img09 = cv.imread('boy09.png')
# 显示图像
cv.imshow('01', img_inversion(Sobeling(Graying(Gaussing(img01)))))
cv.moveWindow('01', 0, 0)
cv.imshow('02', img_inversion(Sobeling(Graying(Gaussing(img02)))))
cv.moveWindow('02', 50, 50)
cv.imshow('03', img_inversion(Sobeling(Graying(Gaussing(img03)))))
cv.moveWindow('03', 100, 90)
cv.imshow('04', img_inversion(Sobeling(Graying(Gaussing(img04)))))
cv.moveWindow('04', 150, 130)
cv.imshow('05', img_inversion(Sobeling(Graying(Gaussing(img05)))))
cv.moveWindow('05', 200, 170)
cv.imshow('06', img_inversion(Sobeling(Graying(Gaussing(img06)))))
cv.moveWindow('06', 250, 210)
cv.imshow('07', img_inversion(Sobeling(Graying(Gaussing(img07)))))
cv.moveWindow('07', 300, 250)
cv.imshow('08', img_inversion(Sobeling(Graying(Gaussing(img08)))))
cv.moveWindow('08', 350, 290)
cv.imshow('09', img_inversion(Sobeling(Graying(Gaussing(img09)))))
cv.moveWindow('09', 350, 290)
# 计时终点
e2 = cv.getTickCount()
# 输出程序运行时间
print('程序运行时间为: %s 秒.' % ((e2 - e1) / cv.getTickFrequency()))
cv.waitKey(0)
