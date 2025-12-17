import os
import streamlit as st
from groq import Groq

API_KEY = os.environ.get("GROQ_API_KEY")

if not API_KEY:
    st.error("API Key 尚未設定！請在 Streamlit Secrets 裡新增 GROQ_API_KEY")
else:
    client = Groq(api_key=API_KEY)

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "system", "content": "你是友善的助手"},
                {"role": "user", "content": "請簡單介紹台灣夜市文化"}
            ]
        )

        # 正確取得內容
        content = getattr(response.choices[0].message, "content", None)
        if content:
            st.write(content)
        else:
            st.warning("回傳資料沒有 content 欄位")

    except Exception as e:
        st.error(f"呼叫 Groq API 失敗: {e}")
