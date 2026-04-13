# 예제 1: 학생 성적 리포트
# 사용 문법: 리스트, 딕셔너리, 반복문, 선택문, 함수

students = [
    {"name": "민지", "scores": [88, 92, 81]},
    {"name": "준호", "scores": [70, 65, 72]},
    {"name": "서연", "scores": [95, 90, 98]},
]


def calculate_average(score_list):
    total = 0

    for score in score_list:
        total += score

    return total / len(score_list)


def make_level(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    else:
        return "D"


def print_report(student_list):
    print("=== 학생 성적 리포트 ===")

    for student in student_list:
        name = student["name"]
        scores = student["scores"]

        average = calculate_average(scores)
        level = make_level(average)

        if average >= 70:
            result = "합격"
        else:
            result = "보충 필요"

        print(f"이름: {name}")
        print(f"점수 목록: {scores}")
        print(f"평균: {average:.1f}, 등급: {level}, 결과: {result}")
        print("-")


print_report(students)
