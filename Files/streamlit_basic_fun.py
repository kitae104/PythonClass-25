import random

import streamlit as st

st.set_page_config(page_title="파이썬 첫걸음 놀이터", page_icon="🎈", layout="centered")

st.title("🎈 파이썬 첫걸음 놀이터")
st.write("Streamlit 위젯으로 파이썬 기초 문법을 재미있게 연습해봐요!")

st.markdown("---")
st.subheader("1) 내 관심사 고르기")

name = st.text_input("이름을 입력해 주세요", placeholder="예: 민지")

hobbies = ["게임", "운동", "독서", "음악", "요리", "여행"]
selected_hobbies = st.multiselect("좋아하는 활동을 골라보세요", hobbies)

if st.button("관심사 요약 보기"):
    if not name:
        st.warning("이름을 먼저 입력해 주세요.")
    elif not selected_hobbies:
        st.info(f"{name}님, 활동을 1개 이상 선택해 주세요.")
    else:
        st.success(f"{name}님의 관심사 요약")
        # for 반복문으로 선택한 항목을 하나씩 출력
        for idx, hobby in enumerate(selected_hobbies, start=1):
            st.write(f"{idx}. {hobby}")

st.markdown("---")
st.subheader("2) 점심 메뉴 추천기")

# 딕셔너리: 카테고리별 메뉴 리스트
menu_dict = {
    "한식": ["비빔밥", "김치찌개", "불고기덮밥"],
    "양식": ["파스타", "햄버거", "샌드위치"],
    "일식": ["초밥", "우동", "돈카츠"],
    "분식": ["떡볶이", "김밥", "라면"],
}

category = st.selectbox("먹고 싶은 메뉴 카테고리를 선택하세요", list(menu_dict.keys()))
spicy = st.checkbox("매운 음식도 괜찮아요")

if st.button("오늘의 메뉴 뽑기"):
    candidates = menu_dict[category][:]

    # if 조건문으로 후보 메뉴 조정
    if not spicy and category in ["한식", "분식"]:
        mild_words = ["찌개", "떡볶이", "라면"]
        filtered = []
        for food in candidates:
            is_mild = True
            for word in mild_words:
                if word in food:
                    is_mild = False
            if is_mild:
                filtered.append(food)

        if filtered:
            candidates = filtered

    picked = random.choice(candidates)
    st.success(f"오늘의 추천 메뉴는 {picked} 입니다!")

    st.caption("카테고리의 전체 메뉴")
    for food in menu_dict[category]:
        st.write(f"- {food}")

st.markdown("---")
st.subheader("3) 지금 배운 문법 체크")

checks = {
    "리스트": "여러 값을 순서대로 저장",
    "딕셔너리": "키-값으로 데이터 저장",
    "if": "조건에 따라 다른 코드 실행",
    "for": "여러 값을 반복 처리",
    "입력 위젯": "사용자 값 받기",
}

show_detail = st.toggle("문법 설명 보기")
if show_detail:
    for key, value in checks.items():
        st.write(f"• {key}: {value}")

st.info("실행해보면서 값을 바꿔보면, 조건문과 반복문의 동작이 더 쉽게 이해됩니다.")
