# Divide and Conquer - 시험 공부 우선순위 정하기

# 과목별 챕터를 분할하여 각 챕터의 우선도를 계산하고,
# 분할 정복(merge sort) 방식으로 정렬해 출력하는 프로그램

def merge_sort(chapters):
    if len(chapters) <= 1:
        return chapters

    mid = len(chapters) // 2
    left = merge_sort(chapters[:mid])
    right = merge_sort(chapters[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # 우선순위(priority)가 높은 순서대로 정렬 (큰 값 먼저)
    while i < len(left) and j < len(right):
        if left[i][1] > right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def main():
    print("=== 시험 공부 우선순위 정하기 프로그램 ===\n")

    subjects = {}
    n = int(input("시험 과목 수를 입력하세요: "))

    for _ in range(n):
        subject = input("\n과목 이름: ")
        days_left = int(input(f"{subject} 시험까지 남은 일수: "))
        importance = int(input(f"{subject} 중요도 (1~10): "))

        c = int(input(f"{subject} 과목의 챕터 수: "))
        chapters = []

        for i in range(c):
            name = input(f" - {i+1}번째 챕터 이름: ")
            progress = int(input("   공부한 정도 (1~10): "))

            # 시험 공부 우선도 계산식
            priority = (11 - days_left) * importance * (11 - progress)
            chapters.append((name, priority))

        subjects[subject] = chapters

    print("\n=== 과목별 공부 우선순위 ===")

    for subject, chapter_list in subjects.items():
        sorted_chapters = merge_sort(chapter_list)
        print(f"\n[{subject}] 추천 공부 순서:")
        for name, priority in sorted_chapters:
            print(f" - {name} (우선도 점수: {priority})")

    print("\n정렬 완료! 시험 일정과 공부 진행도를 반영한 우선순위가 정리되었습니다.")


if __name__ == "__main__":
    main()
