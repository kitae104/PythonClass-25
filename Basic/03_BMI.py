# BMI 계산기
# 입력 -> 수치 계산 -> 조건 분기
height_cm = float(input("키(cm): "))
weight_kg = float(input("몸무게(kg): "))

height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)  # 지수 연산(**)

# 다중 분기 if-elif-else
if bmi < 18.5:
    level = "저체중"
elif bmi < 23:
    level = "정상"
elif bmi < 25:
    level = "과체중"
else:
    level = "비만"

print(f"BMI: {bmi:.2f}, 판정: {level}")  # 포맷 지정(.2f)
