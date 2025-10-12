import random
import string
import time

# 사용할 문자 집합
upper = string.ascii_uppercase   # A-Z
lower = string.ascii_lowercase   # a-z
digits = string.digits           # 0-9
special = "!&*#"
charset = upper + lower + digits + special

# 비밀번호 생성 (첫 글자는 문자만 가능)
def make_password(length=8):
    first_char = random.choice(upper + lower)
    rest = ''.join(random.choice(charset) for _ in range(length - 1))
    return first_char + rest

# 무차별 대입 알고리즘 (8자리 대응)
def brute_force(target):
    start_time = time.time()
    attempt = 0

    print("[비밀번호 찾기 시작]")
    print(f"목표 비밀번호: {target}")
    print("-" * 40)

    for c1 in (upper + lower):            # 첫 글자: 문자만 가능
        for c2 in charset:
            for c3 in charset:
                for c4 in charset:
                    for c5 in charset:
                        for c6 in charset:
                            for c7 in charset:
                                for c8 in charset:
                                    attempt += 1
                                    guess = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8
                                    if attempt % 1000000 == 0:
                                        print(f"{attempt}번째 시도 중... ({guess})")
                                    if guess == target:
                                        end_time = time.time()
                                        print(f"\n[성공] {attempt}번째 시도만에 비밀번호를 찾았습니다!")
                                        print(f"비밀번호: {guess}")
                                        print(f"걸린 시간: {end_time - start_time:.2f}초")
                                        return
    print("실패: 비밀번호를 찾지 못했습니다.")

def main():
    password = make_password(8)  # 8자리 비밀번호 생성
    brute_force(password)

if __name__ == "__main__":
    main()
