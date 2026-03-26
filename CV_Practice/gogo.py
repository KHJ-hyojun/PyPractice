import cv2

# 1. 이미지 불러오기
img_color = cv2.imread('test.jpg')

# 이미지를 제대로 찾았는지 확인
if img_color is None:
    print("이미지를 찾을 수 없습니다. 터미널의 현재 폴더 위치를 확인해 주세요.")
else:
    # 2. 흑백 이미지로 변환
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    # 3. [핵심] 화면에 맞게 사진 크기 축소하기
    # fx=0.25, fy=0.25는 원본 크기의 25%(1/4)로 줄이겠다는 뜻입니다.
    img_color_small = cv2.resize(img_color, (0, 0), fx=0.25, fy=0.25)
    img_gray_small = cv2.resize(img_gray, (0, 0), fx=0.25, fy=0.25)

    # 4. 터미널에 데이터 크기 출력해서 확인하기
    print("=== 처리 완료 ===")
    print("원본 컬러 크기:", img_color.shape)
    print("축소된 흑백 크기:", img_gray_small.shape)

    # 5. 화면에 띄우기 (이제 파란 하늘만 보이지 않습니다!)
    cv2.imshow('Color Puffin', img_color_small)
    cv2.imshow('Gray Puffin', img_gray_small)

    # 창이 닫히지 않도록 대기
    cv2.waitKey(0)
    cv2.destroyAllWindows()