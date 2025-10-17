def add_matrix(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def sub_matrix(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def strassen(a, b):
    # 2x2 행렬 기준
    if len(a) == 1:
        return [[a[0][0] * b[0][0]]]

    # 행렬 분할
    a00, a01 = a[0][0], a[0][1]
    a10, a11 = a[1][0], a[1][1]
    b00, b01 = b[0][0], b[0][1]
    b10, b11 = b[1][0], b[1][1]

    # M1 ~ M7 계산
    m1 = (a00 + a11) * (b00 + b11)
    m2 = (a10 + a11) * b00
    m3 = a00 * (b01 - b11)
    m4 = a11 * (b10 - b00)
    m5 = (a00 + a01) * b11
    m6 = (a10 - a00) * (b00 + b01)
    m7 = (a01 - a11) * (b10 + b11)

    # C 계산
    c00 = m1 + m4 - m5 + m7
    c01 = m3 + m5
    c10 = m2 + m4
    c11 = m1 - m2 + m3 + m6

    return [[c00, c01], [c10, c11]]


def main():
    A = [[10, 8],
         [12, 11]]

    B = [[4, 9],
         [8, 13]]

    print("A =", A)
    print("B =", B)
    print("\nStrassen's Matrix Multiplication 결과:\n")

    result = strassen(A, B)

    for row in result:
        print(row)


if __name__ == "__main__":
    main()
