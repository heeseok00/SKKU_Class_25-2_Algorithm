def karatsuba(x, y):
    # 한 자리 수일 경우 곱셈 바로 수행
    if x < 10 or y < 10:
        return x * y

    # 자릿수 기준 절반으로 분할
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    high1, low1 = divmod(x, 10**m)
    high2, low2 = divmod(y, 10**m)

    # 부분 곱 계산
    z0 = karatsuba(low1, low2)                         # 하위 곱
    z2 = karatsuba(high1, high2)                       # 상위 곱
    z1 = karatsuba(low1 + high1, low2 + high2) - z0 - z2  # 중간항

    # 결과 합산
    return (z2 * 10**(2 * m)) + (z1 * 10**m) + z0


def main():
    x, y = 2462, 8014
    print(f"수식: {x} * {y}\n")

    result = karatsuba(x, y)
    print(f"결과: {result}")


if __name__ == "__main__":
    main()
