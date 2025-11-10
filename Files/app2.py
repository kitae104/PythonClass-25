import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 제목과 설명
# -----------------------------
st.title("📊 Streamlit 기초 데이터 분석 프로그램")
st.write("이 프로그램은 CSV 파일을 불러와 간단히 데이터를 확인하고 그래프로 시각화할 수 있습니다.")

# -----------------------------
# 파일 업로드
# -----------------------------
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    # CSV 파일 읽기
    df = pd.read_csv(uploaded_file)
    st.success("✅ 파일이 성공적으로 업로드되었습니다!")

    # -----------------------------
    # 데이터 미리보기
    # -----------------------------
    st.subheader("📋 데이터 미리보기")
    st.dataframe(df.head())

    # -----------------------------
    # 기본 통계 정보
    # -----------------------------
    st.subheader("📈 기본 통계 요약")
    st.write(df.describe())

    # -----------------------------
    # 그래프 시각화
    # -----------------------------
    st.subheader("📊 그래프 시각화")
    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()

    if numeric_cols:
        col = st.selectbox("그래프로 보고 싶은 컬럼을 선택하세요", numeric_cols)

        fig, ax = plt.subplots()
        ax.hist(df[col], bins=20, color="skyblue", edgecolor="black")
        ax.set_title(f"'{col}' 분포 히스토그램")
        ax.set_xlabel(col)
        ax.set_ylabel("빈도수")

        st.pyplot(fig)
    else:
        st.warning("⚠️ 수치형 데이터가 없어 그래프를 그릴 수 없습니다.")
else:
    st.info("📁 CSV 파일을 업로드하면 데이터 분석이 시작됩니다.")