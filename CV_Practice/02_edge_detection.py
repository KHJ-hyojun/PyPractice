import cv2

img_color = cv2.imread('test.jpg')

if img_color is None:
    print("이미지를 찾을 수 없습니다.")
else:
    img_color_small = cv2.resize(img_color, (0,0), fx=0.25,fy=0.25)
    img_gray_small = cv2.cvtColor(img_color_small, cv2.COLOR_BGR2GRAY)

    # Canny 알고리즘으로 윤곽선 추출 (최소 임계값100, 최대 임계값 200)
    edges = cv2.Canny(img_gray_small, 100, 200)

    cv2.imshow('Canny Edges', edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()