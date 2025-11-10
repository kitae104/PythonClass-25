import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 기본 데이터 분석 앱")

st.write("CSV 파일을 업로드해 간단히 분석하고 그래프를 볼 수 있습니다!")

# 파일 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("📋 데이터 미리보기")
    st.dataframe(df.head())

    st.subheader("📈 기본 통계 정보")
    st.write(df.describe())