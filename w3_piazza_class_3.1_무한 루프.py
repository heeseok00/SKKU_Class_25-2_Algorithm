def is_prime(n):
    if n <= 1:
        return False

    i = 2
    flag = True
    while i > 0:
        if n % i == 0 and i != n:
            flag =  False
        elif i == n:
            flag =  True
        i += 1
    
    return flag

def main():
    n = int(input("정수를 입력하세요: "))
    if is_prime(n):
        print(f"{n}은(는) 소수입니다.")
    else:
        print(f"{n}은(는) 소수가 아닙니다.")

main()
