import itertools
import time

# 주어진 10x10 cost matrix
cost_matrix = [
    [13, 6, 7, 12, 14, 15, 10, 11, 15, 4],
    [8, 14, 11, 9, 6, 14, 7, 9, 16, 12],
    [10, 8, 10, 10, 8, 15, 11, 5, 7, 9],
    [13, 13, 16, 9, 13, 16, 15, 9, 14, 16],
    [11, 4, 9, 14, 12, 11, 5, 16, 8, 14],
    [7, 10, 12, 13, 4, 11, 16, 12, 15, 9],
    [6, 11, 10, 11, 13, 15, 7, 16, 11, 12],
    [7, 15, 5, 10, 4, 16, 12, 4, 10, 16],
    [5, 14, 10, 15, 8, 8, 8, 14, 14, 4],
    [8, 11, 4, 16, 8, 12, 4, 14, 9, 6]
]

def calculate_cost(assignment):
    """각 사람의 작업 할당 비용의 총합 계산"""
    total = 0
    for person, job in enumerate(assignment):
        total += cost_matrix[person][job]
    return total

def brute_force_assignment():
    n = len(cost_matrix)
    jobs = range(n)
    min_cost = float('inf')
    best_assignment = None

    # 모든 가능한 작업 배정 순열 탐색
    for perm in itertools.permutations(jobs):
        cost = calculate_cost(perm)
        if cost < min_cost:
            min_cost = cost
            best_assignment = perm

    return best_assignment, min_cost

def main():
    print("=== Brute Force Job Assignment Problem ===\n")

    start_time = time.time()
    best_assignment, min_cost = brute_force_assignment()
    end_time = time.time()

    print("최적 작업 배정 결과:")
    for person, job in enumerate(best_assignment):
        print(f"사람 {person + 1} → 작업 {job + 1}")
    print(f"\n최소 총 비용: {min_cost}")
    print(f"실행 시간: {end_time - start_time:.6f} 초")

main()
