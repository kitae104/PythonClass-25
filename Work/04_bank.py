# 미니 은행 프로그램 (메뉴, 함수, 상태)
balance = 0  # 전역 상태 변수

def show_menu():
    # 여러 줄 문자열(삼중 따옴표)
    print("""
[미니 뱅크]
1) 잔액 조회
2) 입금
3) 출금
4) 종료
""")

def get_amount(prompt):
    # 유효성 검사(예외 처리)
    try:
        amt = int(input(prompt))
        if amt <= 0:
            print("양의 정수를 입력하세요.")
            return None
        return amt
    except ValueError:
        print("숫자를 입력하세요.")
        return None

while True:
    show_menu()
    choice = input("메뉴 선택: ").strip()

    if choice == "1":
        print(f"현재 잔액: {balance}원")
    elif choice == "2":
        amt = get_amount("입금액: ")
        if amt:
            balance += amt  # 누적 대입
            print(f"입금 완료! 잔액: {balance}원")
    elif choice == "3":
        amt = get_amount("출금액: ")
        if amt:
            if amt > balance:
                print("잔액 부족!")
            else:
                balance -= amt
                print(f"출금 완료! 잔액: {balance}원")
    elif choice == "4":
        print("이용해 주셔서 감사합니다.")
        break
    else:
        print("잘못된 입력입니다. 1~4 중 선택하세요.")
