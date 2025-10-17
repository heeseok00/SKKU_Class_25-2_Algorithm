import cv2
import numpy as np

points = []
all_points = []

# 벡터 기울기 계산
def inclination(p1, p2):
    return p2[0] - p1[0], p2[1] - p1[1]

# 세 점의 회전 방향(ccw) 판별
def ccw(p1, p2, p3):
    v, u = inclination(p1, p2), inclination(p2, p3)
    return v[0] * u[1] > v[1] * u[0]

# 볼록 껍질 계산
def convex_hull(positions):
    global points
    convex = []
    for p3 in positions:
        while len(convex) >= 2:
            p1, p2 = convex[-2], convex[-1]
            if ccw(p1, p2, p3):
                break
            convex.pop()
        convex.append(p3)
    points.extend(convex)

# 마우스로 클릭 시 점 추가
def find_points(event, x, y, flags, param):
    global all_points
    if event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img, (x, y), 3, (255, 255, 255), -1)
        all_points.append([x, y])

if __name__ == "__main__":
    image_path = input("사진 경로를 입력하세요 (예: C:/Users/Desktop/face.jpg) : ")
    save_dir = image_path[:image_path.find('.')]

    try:
        img = cv2.imread(image_path)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', find_points)
    except:
        print("이미지를 불러올 수 없습니다. 경로를 다시 확인하세요.")
        exit()

    print("이미지 위를 클릭해서 점을 찍은 뒤, ESC 또는 스페이스바를 눌러 진행하세요.")

    while True:
        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27 or k == ord(' '):
            break

    # 점들을 정렬 후 볼록 껍질 계산
    all_points = sorted(all_points, key=lambda pos: (pos[0], pos[1]))
    convex_hull(all_points)
    points.pop()
    all_points.reverse()
    convex_hull(all_points)
    points.pop()

    # 결과 선 그리기
    pts = np.array(points, np.int32).reshape((-1, 1, 2))
    img = cv2.polylines(img, [pts], True, (255, 255, 255), 2)

    cv2.imshow('Convex Hull', img)
    cv2.imwrite(save_dir + '_convexhull.jpg', img)
    print("결과 이미지가 저장되었습니다:", save_dir + "_convexhull.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
