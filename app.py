```python
import streamlit as st
import os
from google import genai
from google.genai import types

# 頁面基本設定
st.set_page_config(page_title="AI 學習助理", page_icon="🤖", layout="centered")

# --- 遊戲化成就系統初始化 ---
if "learning_count" not in st.session_state:
    st.session_state.learning_count = 0

# 計算等級 (每完成10次學習升一等)
current_level = (st.session_state.learning_count // 10) + 1
completed_in_level = st.session_state.learning_count % 10

# 徽章清單
badges = {
    1: "🌱 初學萌芽",
    2: "🔥 持之以恆",
    3: "🧠 知識達人",
    4: "⚡ 思考大師",
    5: "👑 終極學霸"
}

# --- 側邊欄：個人成就系統介面 ---
with st.sidebar:
    st.title("🏆 成就系統")
    st.markdown(f"### **目前等級：LV. {current_level}**")
    
    # 進度條
    progress_percentage = completed_in_level / 10.0
    st.progress(progress_percentage)
    st.caption(f"升級進度：{completed_in_level} / 10 次學習")
    
    st.markdown("---")
    st.markdown("🎖️ **已解鎖徽章：**")
    for lvl, badge_name in badges.items():
        if current_level >= lvl:
            st.success(badge_name)
        else:
            st.text(f"🔒 等級 {lvl} 解鎖")

# --- 主畫面介面 ---
st.title("🤖 我的 AI 學習助理")
st.write("在下方輸入你的問題，每次解惑都會累積學習經驗值喔！")

# 這裡可以安全地從環境變數讀取你的 API Key
api_key = os.environ.get("GEMINI_API_KEY")

user_input = st.text_area("請輸入你想請教 AI 的問題：", height=150)

if st.button("送出詢問並記錄學習", type="primary"):
    if not user_input:
        st.warning("請先輸入內容喔！")
    elif not api_key:
        st.error("尚未設定 GEMINI_API_KEY，請至 Streamlit 後台設定 Secrets。")
    else:
        with st.spinner("AI 正在思考中..."):
            try:
                # 初始化 Gemini 團隊最新的 2026 官方客戶端
                client = genai.Client(api_key=api_key)
                
                # 預設使用萬用且快速的 gemini-2.5-flash 模型
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=user_input,
                )
                
                # 顯示結果
                st.markdown("### 🤖 AI 回覆：")
                st.write(response.text)
                
                # 增加學習次數並觸發重整更新等級
                st.session_state.learning_count += 1
                st.rerun()
                
            except Exception as e:
                st.error(f"連線發生錯誤：{e}")
