import random
import math
import time

# 두 점 사이의 거리 계산
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# 최근접 점 쌍 찾기 (분할 정복)
def closest_pair(points):
    n = len(points)
    if n <= 3:
        # 점이 3개 이하이면 브루트포스로 계산
        min_dist = float('inf')
        pair = None
        for i in range(n):
            for j in range(i + 1, n):
                d = distance(points[i], points[j])
                if d < min_dist:
                    min_dist = d
                    pair = (points[i], points[j])
        return pair, min_dist

    mid = n // 2
    mid_x = points[mid][0]

    left_pair, left_dist = closest_pair(points[:mid])
    right_pair, right_dist = closest_pair(points[mid:])
    d = min(left_dist, right_dist)
    best_pair = left_pair if left_dist <= right_dist else right_pair

    # 중간 근처 점들 확인
    strip = [p for p in points if abs(p[0] - mid_x) < d]
    strip.sort(key=lambda p: p[1])

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j][1] - strip[i][1] >= d:
                break
            dist_ij = distance(strip[i], strip[j])
            if dist_ij < d:
                d = dist_ij
                best_pair = (strip[i], strip[j])

    return best_pair, d


def main():
    # 100개의 점 생성 (x좌표 중복 없음)
    random.seed(42)
    points = [(x, random.randint(0, 1000)) for x in random.sample(range(1000), 100)]
    points.sort(key=lambda p: p[0])

    print("생성된 점 개수:", len(points))
    print("일부 점 예시:", points[:5], "\n")

    start = time.time()
    pair, dist = closest_pair(points)
    end = time.time()

    print("가장 가까운 두 점:", pair)
    print(f"거리: {dist:.4f}")
    print(f"실행 시간: {end - start:.6f}초")


if __name__ == "__main__":
    main()
