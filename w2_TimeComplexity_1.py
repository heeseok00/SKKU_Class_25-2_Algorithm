import random
import sys
import heapq
from operator import itemgetter
import time
import math

# 병합 정렬 구현
def merge_sort(arr):
    
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 병합 단계
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][1] < right[j][1]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # 남은 요소 추가
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def main():

    N = 1_000_000  # 영화 데이터 수
    print(f"{N:,}개의 영화 데이터 생성 중...")

    # 데이터 생성
    movies = [("Movie" + str(i+1), random.randint(1, 10)) for i in range(N)]

    # 정렬
    print("병합 정렬 수행 중...")
    start_time = time.time()
    sorted_movies = merge_sort(movies)

    # 시간 복잡도 T(n) 계산 (근사)
    end_time = time.time()

    # 결과 출력
    print("\n평점 TOP 5")
    for title, rating in sorted_movies[-5:]:
        print(f"{title} (평점 {rating})")

    print("\n평점 BOTTOM 5")
    for title, rating in sorted_movies[:5]:
        print(f"{title} (평점 {rating})")
    
    
    print(f"sort time: {end_time - start_time:.6f}초")

if __name__ == "__main__":
    main()
