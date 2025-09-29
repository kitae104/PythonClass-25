# 가위바위보 게임
import random

choices = ["가위", "바위", "보"]  # 리스트 자료형
win_map = {("가위", "보"), ("바위", "가위"), ("보", "바위")}  # 집합(set)과 튜플

user = input("가위/바위/보 중 하나를 입력: ").strip()  # 문자열 메서드(strip)
if user not in choices:
    print("입력 오류!")
else:
    comp = random.choice(choices)
    print(f"컴퓨터: {comp}, 사용자: {user}")

    if user == comp:
        print("비겼습니다!")
    elif (user, comp) in win_map:
        print("이겼습니다!")
    else:
        print("졌습니다!")
