# 예제 2: 카페 주문 계산기
# 사용 문법: 리스트, 딕셔너리, 반복문, 선택문, 함수

menu = {
    "아메리카노": 3000,
    "카페라떼": 4000,
    "쿠키": 2000,
    "샌드위치": 5000,
}

orders = ["아메리카노", "쿠키", "카페라떼", "샌드위치", "주스"]


def calculate_total(order_list, price_table):
    total = 0
    unknown_items = []

    for item in order_list:
        if item in price_table:
            total += price_table[item]
        else:
            unknown_items.append(item)

    return total, unknown_items


def apply_discount(total, order_count):
    # 4개 이상 주문 시 10% 할인
    if order_count >= 4:
        discounted = int(total * 0.9)
        return discounted, "10% 할인 적용"

    return total, "할인 없음"


def print_bill(order_list, price_table):
    print("=== 카페 주문 계산기 ===")
    print("주문 목록:", order_list)

    total, unknown_items = calculate_total(order_list, price_table)
    final_total, message = apply_discount(total, len(order_list))

    print(f"할인 전 금액: {total}원")
    print(f"최종 금액: {final_total}원 ({message})")

    if unknown_items:
        print("가격표에 없는 메뉴:", unknown_items)
    else:
        print("모든 메뉴가 정상 계산되었습니다.")


print_bill(orders, menu)
