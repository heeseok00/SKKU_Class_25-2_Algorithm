import time

# 재귀 함수 방식
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# 반복문 방식
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def main():
    N = 35  # 출력할 항 개수

    # 재귀 실행
    print("===== Fibonacci Recursive =====")
    start = time.time()
    recursive_result = [fib_recursive(i) for i in range(N)]
    end = time.time()
    print("수열:", recursive_result)
    print(f"재귀 실행 시간: {end - start:.6f} 초\n")

    # 반복문 실행
    print("===== Fibonacci Iterative =====")
    start = time.time()
    iterative_result = [fib_iterative(i) for i in range(N)]
    end = time.time()
    print("수열:", iterative_result)
    print(f"반복문 실행 시간: {end - start:.6f} 초")

if __name__ == "__main__":
    main()
