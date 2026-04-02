import cv2
import numpy as np

img_color = cv2.imread('test.jpg')
img_color_small = cv2.resize(img_color, (0,0), fx=0.25,fy=0.25)

#BGR색을 조명에 강한 HSV색상으로 변환
img_hsv = cv2.cvtColor(img_color_small, cv2.COLOR_BGR2HSV)

# 타겟 색상(주황~빨강)의 최소/최대 임계값 설정
lower_orange = np.array([5,100,100])
upper_orange = np.array([25,255,255])

# 범위 안에 들어오는 픽셀만 하얀색으로 칠해서 마스크 만들기
mask = cv2.inRange(img_hsv, lower_orange, upper_orange)

# 마스크를 도장 틀처럼 사용해 원본 이미지에서 타겟만 오려내기
result = cv2.bitwise_and(img_color_small,img_color_small,mask=mask)

cv2.imshow('1. Original', img_color_small)
cv2.imshow('2. Mask (White = Found)', mask)
cv2.imshow('3. Fina; Result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()