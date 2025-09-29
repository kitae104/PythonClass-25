# 숫자 맞추기 게임
import random  # 표준 라이브러리 모듈 임포트 (모듈 import 문법)
# 컴퓨터가 1~100 사이의 임의의 수를 고른다.
secret = random.randint(1, 100)  # 함수 호출과 반환값 사용
count = 0  # 정수 변수 선언 및 초기화

print("숫자 맞추기 게임 시작! (1~100)")

while True:  # 무한 반복문 (while)
    try:
        guess = int(input("추측한 숫자: "))  # 표준 입력, 형변환(int)
    except ValueError:
        print("숫자를 입력해 주세요!")
        continue  # 현재 반복 스킵하고 다음 반복으로

    count += 1  # 대입연산자, 누적

    if guess == secret:  # 조건문 if/elif/else
        print(f"정답! 시도 횟수: {count}회")  # f-string(문자열 포매팅)
        break  # 반복 종료
    elif guess < secret:
        print("업! 더 큰 수예요.")
    else:
        print("다운! 더 작은 수예요.")
