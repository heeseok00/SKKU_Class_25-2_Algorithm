import random
import string
import time

# 사용 가능한 문자 정의
upper = string.ascii_uppercase   # A-Z
lower = string.ascii_lowercase   # a-z
digits = string.digits           # 0-9
special = "!&*#"
charset = upper + lower + digits + special

# 비밀번호 생성 (첫 글자는 문자만 가능)
def make_password(length=5):
    first_char = random.choice(upper + lower)
    rest = ''.join(random.choice(charset) for _ in range(length - 1))
    return first_char + rest

# 브루트포스 시도 함수
def brute_force(target):
    start_time = time.time()
    attempt = 0

    print("[비밀번호 찾기 시작]")
    print(f"목표 비밀번호: {target}")
    print("-" * 40)

    # 가능한 모든 조합 시도 (단순 예시)
    for c1 in (upper + lower):
        for c2 in charset:
            for c3 in charset:
                for c4 in charset:
                    for c5 in charset:
                        attempt += 1
                        guess = c1 + c2 + c3 + c4 + c5
                        if attempt % 500000 == 0:
                            print(f"{attempt}번째 시도 중... ({guess})")
                        if guess == target:
                            end_time = time.time()
                            print(f"\n[성공] {attempt}번째 시도만에 비밀번호를 찾았습니다!")
                            print(f"비밀번호: {guess}")
                            print(f"걸린 시간: {end_time - start_time:.2f}초")
                            return
    print("\n[실패] 모든 조합을 시도했지만 비밀번호를 찾지 못했습니다.")

def main():
    password = make_password()  # 랜덤 비밀번호 생성
    brute_force(password)

if __name__ == "__main__":
    main()
