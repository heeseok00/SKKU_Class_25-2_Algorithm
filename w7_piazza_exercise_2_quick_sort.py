import random
import time

# 퀵 정렬 함수
def quick_sort(arr, depth=0):
    indent = "  " * depth  # 단계별 들여쓰기

    if len(arr) <= 1:
        return arr

    pivot = arr[0]  # 가장 앞의 값을 피벗으로 설정
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    print(f"{indent}Pivot: {pivot} | Left: {left} | Right: {right}")  # 단계별 출력

    sorted_left = quick_sort(left, depth + 1)
    sorted_right = quick_sort(right, depth + 1)

    merged = sorted_left + [pivot] + sorted_right
    print(f"{indent}병합 결과: {merged}")
    return merged


def main():
    # 임의의 수 1000개 생성
    data = [random.randint(1, 10000) for _ in range(1000)]
    print("정렬 전 데이터 (일부):", data[:10], "...\n")

    start_time = time.time()  # 실행 시간 측정 시작
    sorted_data = quick_sort(data)
    end_time = time.time()    # 실행 시간 측정 종료

    print("\n정렬 후 데이터 (일부):", sorted_data[:10], "...\n")
    print(f"실행 시간: {end_time - start_time:.6f}초")


if __name__ == "__main__":
    main()
