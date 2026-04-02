import cv2

img_color = cv2.imread('test.jpg')

if img_color is None:
    print("이미지를 찾을 수 없습니다. 경로를 확인해주세요")
else:
    # 연산량 감소를 위한 흑백(GrayScale) 변환
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    # 화면 및 연산에 맞게 해상도 1/4로 물리적 축소
    img_color_small = cv2.resize(img_color, (0,0), fx=0.25, fy=0.25)
    img_gray_small = cv2.resize(img_gray, (0,0), fx=0.25, fy=0.25)
    
    cv2.imshow('Color - Resized', img_color_small)
    cv2.imshow('Gray - Resized', img_gray_small)

    cv2.waitKey(0)
    cv2.destroyAllWindows()