from img_processing import *
import cv2 as cv
# 读取图像
img = cv.imread('wallpaper.png')
# 使用椭圆绘制爱心图形
cv.ellipse(img, (540, 440), (10, 20), -17, 330, 60,  (120, 40, 240), 5)
cv.ellipse(img, (550, 440), (10, 20), +17, 470, 200, (120, 40, 240), 5)
# 绘制五角星
pt1 = (525, 270)
pt2 = (565, 310)
pt3 = (550, 245)
pt4 = (535, 310)
pt5 = (575, 270)
pts = np.array([[pt1], [pt2], [pt3], [pt4], [pt5]])
cv.polylines(img, [pts], True, (140, 80, 255), 4)
# 添加文字
cv.putText(img, 'M', (400, 230), cv.FONT_HERSHEY_COMPLEX, 3, (255, 180, 40), 2)
cv.putText(img, 'I', (420, 330), cv.FONT_HERSHEY_COMPLEX, 3, (40, 200, 40), 2)
cv.putText(img, 'N', (400, 430), cv.FONT_HERSHEY_COMPLEX, 3, (220, 140, 220), 2)
cv.putText(img, 'O', (400, 530), cv.FONT_HERSHEY_COMPLEX, 3, (128, 128, 255), 2)
# 显示图像
cv.imshow('img', img)
cv.imwrite('result.png', img)
cv.waitKey(0)
