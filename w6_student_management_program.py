# 학생 성적 관리 프로그램

import json
import os
import statistics

students = []  # 학생 정보를 저장할 리스트
FILE_NAME = "students.json"  # 저장 파일 이름
# 형식: {"name": str, "id": str, "score": float}

def load_from_file():
    """프로그램 시작 시 파일에서 데이터 불러오기"""
    global students
    if os.path.exists(FILE_NAME):
        # 저장 파일이 있으면 JSON을 읽어 메모리에 적재
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            students = json.load(f)
        print(" 이전 저장 데이터를 불러왔습니다.")
    else:
        # 저장 파일이 없으면 빈 목록으로 시작
        students = []


def save_to_file():
    """학생 데이터를 파일에 저장"""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=4)
    print(" 데이터가 파일에 저장되었습니다.")


def add_student():
    """학생 정보 입력"""
    name = input("학생 이름: ").strip()
    student_id = input("학번: ").strip()
    try:
        # 숫자 외 입력은 예외 처리
        score = float(input("성적(점수): "))
    except ValueError:
        print(" 숫자를 입력해야 합니다.")
        return

    student = {"name": name, "id": student_id, "score": score}
    students.append(student)
    print(f" {name} 학생 정보가 등록되었습니다.")


def print_students():
    """전체 학생 목록 출력"""
    if not students:
        print("등록된 학생이 없습니다.")
        return
    print("\n--- 전체 학생 목록 ---")
    for i, s in enumerate(students, start=1):
        print(f"{i}. 이름: {s['name']}, 학번: {s['id']}, 성적: {s['score']:.2f}")


def quick_sort_by_score(arr, reverse=False):
    """점수 기준 퀵 정렬 (새 리스트 반환)

    평균 O(n log n), 최악 O(n^2)
    비안정 정렬(같은 점수의 상대적 순서 보장 X)
    reverse=True이면 내림차순
    """
    if len(arr) <= 1:
        return arr[:]
    # 가운데 원소의 점수를 피벗으로 사용
    pivot = arr[len(arr) // 2]["score"]
    less = [x for x in arr if x["score"] < pivot]
    equal = [x for x in arr if x["score"] == pivot]
    greater = [x for x in arr if x["score"] > pivot]
    if reverse:
        return quick_sort_by_score(greater, True) + equal + quick_sort_by_score(less, True)
    else:
        return quick_sort_by_score(less, False) + equal + quick_sort_by_score(greater, False)


def sort_students():
    """성적 기준으로 정렬"""
    if not students:
        print("정렬할 학생이 없습니다.")
        return

    # 정렬 알고리즘과 방향을 사용자가 선택
    print("정렬 알고리즘 선택: 1. 버블  2. 선택  3. 퀵")
    alg = input("선택: ").strip()
    print("1. 오름차순  2. 내림차순")
    order = input("정렬 방식 선택: ").strip()
    reverse = (order == "2")  # True면 내림차순

    n = len(students)
    if alg == "1":  # 버블 정렬: 인접 원소를 비교/교환하며 큰(작은) 값을 끝으로 보냄
        for i in range(n - 1):
            for j in range(n - i - 1):
                if (not reverse and students[j]["score"] > students[j + 1]["score"]) or (
                    reverse and students[j]["score"] < students[j + 1]["score"]
                ):
                    students[j], students[j + 1] = students[j + 1], students[j]
    elif alg == "2":  # 선택 정렬: i 위치에 올 최솟값(또는 최댓값)을 선택해 교환
        for i in range(n - 1):
            idx = i
            for j in range(i + 1, n):
                if (not reverse and students[j]["score"] < students[idx]["score"]) or (
                    reverse and students[j]["score"] > students[idx]["score"]
                ):
                    idx = j
            if idx != i:
                students[i], students[idx] = students[idx], students[i]
    elif alg == "3":  # 퀵 정렬: 새 리스트로 정렬 후 슬라이스 대입으로 원본 갱신
        students[:] = quick_sort_by_score(students, reverse=reverse)
    else:
        print(" 잘못된 입력입니다.")
        return

    print(" 정렬이 완료되었습니다.")


def search_student():
    """학생 이름 또는 학번으로 검색"""
    if not students:
        print("학생 데이터가 없습니다.")
        return

    print("1. 이름으로 검색  2. 학번으로 검색")
    mode = input("선택: ").strip()

    if mode == "1":
        target = input("검색할 이름: ").strip()
        key = "name"
    elif mode == "2":
        target = input("검색할 학번: ").strip()
        key = "id"
    else:
        print(" 잘못된 입력입니다.")
        return

    print("탐색 알고리즘 선택: 1. 순차  2. 이진")
    algo = input("선택: ").strip()

    found = []
    if algo == "1":  # 순차 탐색: 처음부터 끝까지 선형으로 비교
        found = [s for s in students if s[key] == target]
    elif algo == "2":  # 이진 탐색: 키로 정렬한 복사본에서 수행(원본 순서 보존)
        sorted_list = sorted(students, key=lambda s: s[key])
        lo, hi = 0, len(sorted_list) - 1
        idx = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if sorted_list[mid][key] == target:
                idx = mid
                break
            elif sorted_list[mid][key] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        if idx != -1:
            # 동일 키가 여러 건이면 중앙 인덱스에서 좌/우로 확장해 모두 수집
            start = idx
            while start - 1 >= 0 and sorted_list[start - 1][key] == target:
                start -= 1
            end = idx
            while end + 1 < len(sorted_list) and sorted_list[end + 1][key] == target:
                end += 1
            found = sorted_list[start : end + 1]
    else:
        print(" 잘못된 입력입니다.")
        return

    if found:
        for s in found:
            print(f"이름: {s['name']}, 학번: {s['id']}, 성적: {s['score']:.2f}")
    else:
        print("검색 결과가 없습니다.")


def find_max_min():
    """최고 점수와 최저 점수 학생 찾기"""
    if not students:
        print("학생 데이터가 없습니다.")
        return

    # 내장 max/min과 key 인자를 이용해 점수 기준으로 계산
    max_stu = max(students, key=lambda s: s["score"])
    min_stu = min(students, key=lambda s: s["score"])

    print(f" 최고 성적: {max_stu['name']} ({max_stu['score']:.2f}점)")
    print(f" 최저 성적: {min_stu['name']} ({min_stu['score']:.2f}점)")


def find_by_range():
    """특정 점수 범위 내 학생 조회"""
    if not students:
        print("학생 데이터가 없습니다.")
        return

    try:
        low = float(input("최소 점수: "))
        high = float(input("최대 점수: "))
    except ValueError:
        print(" 숫자를 입력해야 합니다.")
        return

    # 경계 포함: [low, high]
    found = [s for s in students if low <= s["score"] <= high]
    if found:
        print(f"\n{low}점 ~ {high}점 사이 학생 목록:")
        for s in found:
            print(f"- {s['name']} ({s['score']:.2f}점)")
    else:
        print("해당 범위 내 학생이 없습니다.")


def show_statistics():
    """성적 평균, 중앙값, 최빈값 계산"""
    if not students:
        print("학생 데이터가 없습니다.")
        return

    scores = [s["score"] for s in students]
    mean = statistics.mean(scores)
    median = statistics.median(scores)

    try:
        # 단일 최빈값이 없는 경우 예외 발생 -> 사용자 친화적으로 처리
        mode = statistics.mode(scores)
    except statistics.StatisticsError:
        mode = "없음"

    print(f"평균: {mean:.2f}")
    print(f"중앙값: {median:.2f}")
    print(f"최빈값: {mode}")


def main():
    """메인 메뉴"""
    load_from_file()

    # 메뉴 루프: 사용자 입력에 따라 기능 실행
    while True:
        print("\n===== 학생 성적 관리 프로그램 =====")
        print("1. 학생 정보 입력")
        print("2. 전체 학생 출력")
        print("3. 성적 정렬")
        print("4. 학생 탐색")
        print("5. 최고/최저 성적 학생 찾기")
        print("6. 성적 범위로 학생 찾기")
        print("7. 성적 통계 보기")
        print("8. 저장 후 종료")

        choice = input("메뉴 선택: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            print_students()
        elif choice == "3":
            sort_students()
        elif choice == "4":
            search_student()
        elif choice == "5":
            find_max_min()
        elif choice == "6":
            find_by_range()
        elif choice == "7":
            show_statistics()
        elif choice == "8":
            save_to_file()
            print("프로그램을 종료합니다.")
            break
        else:
            print(" 잘못된 입력입니다.")


if __name__ == "__main__":
    main()
