import streamlit as st

# 設定網頁全寬與標題
st.set_page_config(page_title="English Vocabulary Instructor", page_icon="🎓", layout="wide")

st.markdown("""
    <style>
    /* 隱藏 Streamlit 預設的多餘邊距，讓 AI App 填滿螢幕 */
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
    }
    iframe {
        width: 100%;
        height: calc(100vh - 50px);
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# 這裡請替換成你在 AI Studio 點擊 Publish 後得到的真實網址
ai_studio_app_url = "這裡貼上你剛剛複製的Publish網址"

# 將 AI Studio 的完美介面內嵌進來
st.components.v1.iframe(ai_studio_app_url, height=800, scrolling=True)
