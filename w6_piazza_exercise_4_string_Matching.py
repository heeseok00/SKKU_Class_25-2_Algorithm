import time

def brute_force_string_match(text, pattern):
    positions = []  # 패턴이 나타나는 위치 저장용 리스트
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            positions.append(i)
    return positions


def main():
    # 파일 읽기
    with open("TheLittlePrince.txt", "r", encoding="utf-8") as f:
        text = f.read()

    pattern = "어린 왕자"

    print(f"탐색할 단어: '{pattern}'")

    start_time = time.time()
    positions = brute_force_string_match(text, pattern)
    end_time = time.time()

    print("\n=== 결과 ===")
    if positions:
        print(f"총 {len(positions)}번 등장했습니다.")
        print(f"등장 인덱스: {positions}")
    else:
        print("텍스트 내에 '어린 왕자'가 존재하지 않습니다.")

    print(f"\n실행 시간: {end_time - start_time:.6f}초")


main()
