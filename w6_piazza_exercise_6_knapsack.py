import itertools
import time

def brute_force_knapsack(weights, values, capacity):
    n = len(weights)
    max_value = 0
    best_combo = None

    # 가능한 모든 조합을 완전탐색
    for r in range(1, n + 1):
        for combo in itertools.combinations(range(n), r):
            total_weight = sum(weights[i] for i in combo)
            total_value = sum(values[i] for i in combo)
            if total_weight <= capacity and total_value > max_value:
                max_value = total_value
                best_combo = combo

    return best_combo, max_value


def main():
    n = int(input("아이템 개수 입력: "))
    capacity = int(input("배낭의 최대 무게 입력: "))

    weights = []
    values = []

    for i in range(n):
        w = int(input(f"아이템 {i+1}의 무게: "))
        weights.append(w)
        v = int(input(f"아이템 {i+1}의 가치: "))
        values.append(v)

    start_time = time.time()
    best_combo, max_value = brute_force_knapsack(weights, values, capacity)
    end_time = time.time()

    print("\nBrute Force Knapsack 결과")
    print("--------------------------")
    print(f"최대 가치: {max_value}")

    if best_combo:
        # 인덱스를 1부터 표시
        print(f"선택된 아이템 번호: {[i + 1 for i in best_combo]}")
    else:
        print("선택된 아이템이 없습니다.")

    print(f"실행 시간: {end_time - start_time:.6f}초")
    print("--------------------------")


main()
