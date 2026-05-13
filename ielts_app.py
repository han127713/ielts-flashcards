import streamlit as st
import pandas as pd
import random

# 設定網頁標題與圖示
st.set_page_config(page_title="我們倆的雅思單字本", page_icon="📖")

# 讀取妳剛剛上傳的 csv 檔案
@st.cache_data
def load_data():
    try:
        # 讀取 CSV
        df = pd.read_csv("ielts_words.csv")
        return df
    except:
        # 如果檔案還沒讀到，先給一個小提示
        return pd.DataFrame({"Word": ["請確認檔案已上傳"], "Definition": ["找不到檔案"], "Example": ["n/a"], "Type": ["n/a"]})

df = load_data()

st.title("🔥 雅思 500 核心詞彙衝刺")
st.write("這是我們專屬的背單字小站！")

# 初始化：如果還沒有抽過單字，就隨機抽一個
if 'current_word' not in st.session_state:
    st.session_state.current_word = df.sample(n=1).iloc[0]
    st.session_state.show_ans = False

# 換下一個單字的函數
def next_word():
    st.session_state.current_word = df.sample(n=1).iloc[0]
    st.session_state.show_ans = False

# 顯示介面
word_info = st.session_state.current_word

st.markdown(f"### 目前單字：")
st.markdown(f"<h1 style='color: #11CAA0;'>{word_info['Word']}</h1>", unsafe_allow_html=True)

# 按鈕區
if st.button("查看翻譯與例句"):
    st.session_state.show_ans = True

if st.session_state.show_ans:
    st.success(f"**中文意思：** {word_info['Definition']}")
    st.info(f"**例句練習：** {word_info['Example']}")

st.write("---")

if st.button("換下一個 ➡️"):
    next_word()
    st.rerun()

# 側邊欄顯示清單
with st.sidebar:
    st.header("所有單字一覽")
    st.dataframe(df[["Word", "Definition"]])