import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def main():
    # 정렬할 데이터 1000개 생성
    data = [random.randint(1, 10000) for _ in range(1000)]

    print(f"정렬할 데이터 개수: {len(data)}개\n")

    # 정렬 실행 시간 측정 (데이터 생성 시간 제외)
    start_time = time.time()
    sorted_data = bubble_sort(data)
    end_time = time.time()

    print("정렬이 완료되었습니다.")
    print(f"실행 시간: {end_time - start_time:.6f}초\n")

    # 정렬 결과 일부 출력
    print("정렬 결과 (앞 20개만 표시):")
    print(sorted_data[:20])

if __name__ == "__main__":
    main()
