import cv2

img_color = cv2.imread('test.jpg')

if img_color is None:
    print("이미지를 찾을 수 없습니다. 터미널 위치를 확인해 주세요")
else:
    img_gray = cv2.cvtColor(img_color,cv2.COLOR_BGR2GRAY)

    img_gray_small = cv2.resize(img_gray, (0,0), fx = 0.25, fy = 0.25)

    edges = cv2.Canny(img_gray_small, 100, 200)

    cv2.imshow('1 , Grayscale Puffin', img_gray_small)
    cv2.imshow('2, EdgePufin', edges)

    cv2.waitey(0)
    cv2.destroyAllWindows()