import random
import time

# 병합 정렬 함수
def merge_sort(arr, depth=0):
    indent = "  " * depth  # 단계별 들여쓰기
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    print(f"{indent}분할: {left} | {right}")  # 분할 과정 출력

    sorted_left = merge_sort(left, depth + 1)
    sorted_right = merge_sort(right, depth + 1)

    merged = merge(sorted_left, sorted_right)
    print(f"{indent}병합: {merged}")  # 병합 과정 출력

    return merged


# 병합 함수
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def main():
    # 임의의 수 100개 생성
    data = [random.randint(1, 1000) for _ in range(100)]
    print("정렬 전 데이터 (일부):", data[:10], "...\n")

    start_time = time.time()  # 실행 시간 측정 시작
    sorted_data = merge_sort(data)
    end_time = time.time()    # 실행 시간 측정 종료

    print("\n정렬 후 데이터 (일부):", sorted_data[:10], "...\n")
    print(f"실행 시간: {end_time - start_time:.6f}초")


if __name__ == "__main__":
    main()
