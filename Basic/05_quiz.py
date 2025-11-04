import random

WORDS = {
    "algorithm": "알고리즘",
    "variable": "변수",
    "function": "함수",
    "dictionary": "딕셔너리",
    "iteration": "반복",
    "condition": "조건",
    "parameter": "매개변수",
    "exception": "예외",
}

def normalize(s: str) -> str:
    """문자열 전처리: 소문자, 양쪽 공백 제거"""
    return s.strip().lower()

def ask_question(eng: str, kor: str) -> bool:
    """한 문제를 출제하고 정답 여부를 반환"""
    user = input(f'"{eng}"의 한국어 뜻은? (종료: 종료) > ')
    if normalize(user) == "종료":
        # 종료 신호는 호출자(run_quiz)에서 처리
        raise KeyboardInterrupt
    return normalize(user) == normalize(kor)

def run_quiz():
    keys = list(WORDS.keys())
    random.shuffle(keys)  # 문제 순서 섞기
    correct = 0
    tried = 0
    print("== 플래시카드 단어 퀴즈 시작 ==")
    try:
        for eng in keys:
            kor = WORDS[eng]
            tried += 1
            if ask_question(eng, kor):
                correct += 1
                print("정답! ✅")
            else:
                print(f"오답! ❌ 정답: {kor}")
    except KeyboardInterrupt:
        print("\n사용자 종료 요청을 받았습니다.")
    finally:
        print(f"결과: 정답 {correct} / 시도 {tried} ({(correct/max(tried,1))*100:.1f}%)")
        
run_quiz()