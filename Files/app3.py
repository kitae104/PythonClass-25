import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="기초 데이터 분석 앱", layout="wide")

st.title("📊 Streamlit 기초 데이터 분석 (여러 그래프)")

st.write("CSV를 업로드하고 원하는 **그래프 타입**을 선택해서 시각화해보세요.")

# -----------------------------
# 파일 업로드 & 데이터 준비
# -----------------------------
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ 파일 업로드 완료")
else:
    st.info("예시 데이터가 표시됩니다. (BMI 비슷한 구조: Height, Weight, BMI)")
    np.random.seed(42)
    df = pd.DataFrame({
        "Height": np.random.normal(170, 8, 120).round(1),
        "Weight": np.random.normal(70, 10, 120).round(1),
    })
    df["BMI"] = (df["Weight"] / ((df["Height"]/100) ** 2)).round(1)

# -----------------------------
# 데이터 미리보기 & 통계
# -----------------------------
with st.expander("📋 데이터 미리보기 / 요약 통계", expanded=True):
    st.dataframe(df.head())
    st.write(df.describe())

# -----------------------------
# 사이드바: 그래프 설정
# -----------------------------
st.sidebar.header("⚙️ 시각화 설정")
chart_type = st.sidebar.selectbox(
    "그래프 종류",
    ["히스토그램", "선(Line)", "막대(Bar)", "박스(Box)", "산점도(Scatter)", "상관 히트맵"]
)

numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
cat_cols = df.select_dtypes(exclude=["number"]).columns.tolist()

# 공통 옵션
st.sidebar.markdown("---")
st.sidebar.caption("아래 옵션은 그래프 종류에 따라 달라집니다.")

# -----------------------------
# 그래프 그리기
# -----------------------------
st.subheader(f"📊 {chart_type} 그래프")

if not numeric_cols:
    st.warning("수치형 컬럼이 없어 그래프를 그릴 수 없습니다.")
else:
    if chart_type == "히스토그램":
        col = st.sidebar.selectbox("대상 컬럼", numeric_cols)
        bins = st.sidebar.slider("구간(bins)", min_value=5, max_value=50, value=20, step=1)

        fig, ax = plt.subplots()
        ax.hist(df[col].dropna(), bins=bins, edgecolor="black")
        ax.set_title(f"'{col}' 분포 히스토그램")
        ax.set_xlabel(col)
        ax.set_ylabel("빈도수")
        st.pyplot(fig)

    elif chart_type == "선(Line)":
        cols = st.sidebar.multiselect("표시할 컬럼(2개 이상 가능)", numeric_cols, default=numeric_cols[:2])
        if cols:
            st.line_chart(df[cols])
        else:
            st.info("표시할 수치형 컬럼을 선택해주세요.")

    elif chart_type == "막대(Bar)":
        agg_col = st.sidebar.selectbox("집계 대상(수치형)", numeric_cols)
        if cat_cols:
            group_col = st.sidebar.selectbox("그룹(범주형)", cat_cols)
            agg_fn = st.sidebar.selectbox("집계 방식", ["mean", "sum", "median", "max", "min"], index=0)
            grouped = getattr(df.groupby(group_col)[agg_col], agg_fn)().sort_values(ascending=False)
            st.bar_chart(grouped)
        else:
            st.info("범주형 컬럼이 없어 전체 평균 막대를 표시합니다.")
            st.bar_chart(pd.Series({agg_col: df[agg_col].mean()}))

    elif chart_type == "박스(Box)":
        col = st.sidebar.selectbox("대상 컬럼", numeric_cols)
        fig, ax = plt.subplots()
        ax.boxplot(df[col].dropna(), vert=True)
        ax.set_title(f"'{col}' 박스플롯")
        ax.set_ylabel(col)
        st.pyplot(fig)

    elif chart_type == "산점도(Scatter)":
        x = st.sidebar.selectbox("X 축", numeric_cols, index=0)
        y = st.sidebar.selectbox("Y 축", numeric_cols, index=min(1, len(numeric_cols)-1))
        size_opt = st.sidebar.checkbox("점 크기 컬럼 사용", value=False)
        size_col = None
        if size_opt:
            size_col = st.sidebar.selectbox("크기 컬럼", numeric_cols, index=0)

        fig, ax = plt.subplots()
        if size_col:
            sizes = (df[size_col].fillna(df[size_col].median()) - df[size_col].min() + 1)
            ax.scatter(df[x], df[y], s=20 + (sizes / sizes.max()) * 80, alpha=0.7)
        else:
            ax.scatter(df[x], df[y], alpha=0.7)
        ax.set_title(f"산점도: {x} vs {y}")
        ax.set_xlabel(x); ax.set_ylabel(y)
        st.pyplot(fig)

    elif chart_type == "상관 히트맵":
        corr = df[numeric_cols].corr(numeric_only=True)
        fig, ax = plt.subplots()
        im = ax.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
        ax.set_xticks(range(len(corr.columns)))
        ax.set_yticks(range(len(corr.index)))
        ax.set_xticklabels(corr.columns, rotation=45, ha="right")
        ax.set_yticklabels(corr.index)
        ax.set_title("상관계수 히트맵")
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        st.pyplot(fig)

# -----------------------------
# 작은 팁
# -----------------------------
with st.expander("💡 사용 팁"):
    st.markdown(
        """
- **히스토그램**: 한 컬럼의 분포를 확인할 때.
- **선(Line)**: 시간순 데이터나 연속 변화 비교.
- **막대(Bar)**: 범주별 합계/평균 비교.
- **박스(Box)**: 이상치와 분포 요약 파악.
- **산점도(Scatter)**: 두 변수의 관계(상관) 탐색.
- **상관 히트맵**: 여러 수치형 변수 간 상관관계 한눈에 보기.
        """
    )