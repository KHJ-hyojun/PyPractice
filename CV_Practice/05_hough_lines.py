import cv2
import numpy as np

img_color = cv2.imread('lane.png')
img_hls = cv2.cvtColor(img_color, cv2.COLOR_BGR2HLS)

# 흰색/노란색 마스크 생성
lower_white = np.array([0,200,0])
upper_white = np.array([179,255,255])
mask_white = cv2.inRange(img_hls, lower_white, upper_white)

lower_yellow = np.array([15, 30, 115])
upper_yellow = np.array([35, 204, 255])
mask_yellow = cv2.inRange(img_hls, lower_yellow, upper_yellow)

# 두 마스크를 합치고 원본에 씌우기 ( 흰색과 노란색만 남음 )
mask_combined = cv2.bitwise_or(mask_white, mask_yellow)
filtered_img = cv2.bitwise_and(img_color, img_color, mask = mask_combined)

# 필터링된 깔끔한 이미지로 윤곽선 추출
img_gray = cv2.cvtColor(filtered_img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img_gray, 50, 50)


# 허프 변환으로 직선 찾아내기
lines = cv2.HoughLinesP(
    edges,
    1,
    np.pi/180,
    threshold = 70,
    minLineLength = 40,
    maxLineGap = 5
)

# 찾은 직선을 원본 이미지에 빨간색으로 덧그리기
if lines is not None:
    for line in lines:
        x1,y1,x2,y2 = line[0]
        cv2.line(img_color, (x1,y1), (x2,y2), (0,0,255), 3)
    
cv2.imshow('1. Canny Edges', edges)
cv2.imshow('2. Lane Detection', img_color)

cv2.waitKey(0)
cv2.destroyAllWindows()