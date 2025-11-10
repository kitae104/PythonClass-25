import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="기초 데이터 분석 - 산점도 & 라인", layout="wide")
st.title("📊 기본 데이터 분석 (산점도 & 라인)")

st.write("CSV를 업로드하거나 예시 데이터를 이용해 **산점도**와 **라인 그래프**를 확인하세요.")

# -----------------------------
# 1) 파일 업로드 / 예시 데이터
# -----------------------------
uploaded_file = st.file_uploader("CSV 파일 업로드 (.csv)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ 파일 업로드 완료")
else:
    st.info("예시 데이터가 표시됩니다. (Height, Weight, BMI)")
    np.random.seed(42)
    df = pd.DataFrame({
        "Height": np.random.normal(170, 8, 120).round(1),
        "Weight": np.random.normal(70, 10, 120).round(1),
    })
    df["BMI"] = (df["Weight"] / ((df["Height"]/100) ** 2)).round(1)

# 숫자/문자 컬럼 분리
num_cols = df.select_dtypes(include=["number"]).columns.tolist()
all_cols = df.columns.tolist()

# -----------------------------
# 데이터 미리보기
# -----------------------------
with st.expander("📋 데이터 미리보기 / 요약 통계", expanded=True):
    st.dataframe(df.head())
    if len(num_cols) > 0:
        st.write(df[num_cols].describe())
    else:
        st.warning("수치형 컬럼이 없어 통계 요약을 건너뜁니다.")

# -----------------------------
# 2) 그래프 종류 선택
# -----------------------------
chart_type = st.radio("그래프 선택", ["산점도", "라인"], horizontal=True)

# -----------------------------
# 3) 산점도
# -----------------------------
if chart_type == "산점도":
    st.subheader("🔹 산점도(Scatter)")
    if len(num_cols) < 2:
        st.warning("산점도를 위해서는 최소 2개의 수치형 컬럼이 필요합니다.")
    else:
        col1, col2 = st.columns(2)
        with col1:
            x_col = st.selectbox("X축 컬럼", num_cols, index=0)
        with col2:
            # 기본값은 X와 다른 컬럼
            default_y_idx = 1 if len(num_cols) > 1 else 0
            y_col = st.selectbox("Y축 컬럼", num_cols, index=default_y_idx)

        # 선택된 컬럼이 같으면 경고
        if x_col == y_col:
            st.warning("X축과 Y축은 서로 다른 컬럼을 선택하세요.")
        else:
            fig, ax = plt.subplots()
            ax.scatter(df[x_col], df[y_col], alpha=0.7)
            ax.set_title(f"산점도: {x_col} vs {y_col}")
            ax.set_xlabel(x_col); ax.set_ylabel(y_col)
            st.pyplot(fig)

# -----------------------------
# 4) 라인 그래프
# -----------------------------
elif chart_type == "라인":
    st.subheader("🔹 라인(Line)")
    if len(num_cols) == 0:
        st.warning("라인 그래프를 그릴 수치형 컬럼이 없습니다.")
    else:
        # X축으로 사용할 컬럼(옵션)
        st.markdown("**X축(선택):** 시간/숫자 컬럼이 있으면 지정하세요. 지정하지 않으면 행 인덱스를 기준으로 그립니다.")
        possible_x = [c for c in all_cols if df[c].dtype.kind in "iufM"]  # 숫자/datetime 후보
        use_x = st.checkbox("X축 컬럼 사용", value=False)
        x_col = None
        if use_x and possible_x:
            x_col = st.selectbox("X축 컬럼 선택", possible_x, index=0)
            # datetime 자동 변환 시도
            if pd.api.types.is_object_dtype(df[x_col]):
                try:
                    df[x_col] = pd.to_datetime(df[x_col])
                except Exception:
                    pass
        elif use_x and not possible_x:
            st.info("적절한 X축 후보가 없어 인덱스를 사용합니다.")
            use_x = False

        # Y축으로 그릴 수치형 컬럼 여러 개 선택
        y_cols = st.multiselect("라인으로 표시할 수치형 컬럼(복수 선택 가능)", num_cols, default=num_cols[:2])

        if not y_cols:
            st.info("표시할 수치형 컬럼을 1개 이상 선택하세요.")
        else:
            plot_df = df.copy()
            if use_x and x_col is not None:
                plot_df = plot_df.set_index(x_col)

            st.line_chart(plot_df[y_cols])

# -----------------------------
# 작은 팁
# -----------------------------
with st.expander("💡 사용 팁"):
    st.markdown(
        """
- **산점도**: 두 변수의 관계(상관성)를 직관적으로 파악할 때 좋아요. (예: Height vs Weight)
- **라인 그래프**: 시간에 따른 변화나 연속적인 트렌드를 비교할 때 적합합니다.
- X축에 날짜/시간 컬럼이 있다면 체크박스로 X축 컬럼을 지정해보세요.
        """
    )
