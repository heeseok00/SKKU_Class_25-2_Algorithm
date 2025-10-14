import itertools
import time

# 그래프 인접 행렬 
graph = [
    [0, 2, 3, 2, 3],
    [2, 0, 3, 4, 1],
    [3, 3, 0, 2, 4],
    [2, 4, 2, 0, 5],
    [3, 1, 4, 5, 0]
]

def path_cost(path):
    total = 0
    for i in range(len(path) - 1):
        total += graph[path[i]][path[i + 1]]
    total += graph[path[-1]][path[0]]  # 마지막 도시에서 시작점으로 복귀
    return total

def brute_force_tsp():
    vertices = [0, 1, 2, 3, 4]
    start = 0  # 1번 정점에서 출발
    vertices.remove(start)

    min_cost = float('inf')
    best_path = []

    for perm in itertools.permutations(vertices):
        path = [start] + list(perm)
        cost = path_cost(path)
        if cost < min_cost:
            min_cost = cost
            best_path = path

    return best_path, min_cost

def main():
    start_time = time.time()

    best_path, min_cost = brute_force_tsp()

    end_time = time.time()

    # 출력 형식 
    print(f"최적 경로: {[v + 1 for v in best_path] + [1]}")
    print(f"최소 비용: {min_cost}")
    print(f"실행 시간: {end_time - start_time:.6f} 초")

main()
