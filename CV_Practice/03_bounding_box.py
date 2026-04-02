import cv2
img_color = cv2.imread('test.jpg')

if img_color is None:
    print("이미지를 찾을 수 없습니다.")
else:
    # 전처리 및 엣지 추출
    img_color_small = cv2.resize(img_color, (0, 0), fx=0.25, fy=0.25)
    img_gray_small = cv2.cvtColor(img_color_small, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(img_gray_small, 100, 200)

    # 흩어진 선들을 덩어리(Contour)로 묶어내기
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) > 0:
        # 수많은 덩어리 중 면적이 가장 큰 것 1개만 필터링
        largest_contour = max(contours, key=cv2.contourArea)

        # 덩어리를 감싸는 최소 크기의 직사각형 좌표 추출
        x, y, w, h = cv2.boundingRect(largest_contour)

        # 원본 이미지 위에 초록색(0, 255, 0) 타겟 박스 그리기
        cv2.rectangle(img_color_small, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img_color_small, 'Target Object', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow('Bounding Box Result', img_color_small)
    cv2.waitKey(0)
    cv2.destroyAllWindows()