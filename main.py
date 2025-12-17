import streamlit as st
import pandas as pd
from groq import Groq
from sidebar import render_sidebar

from dotenv import load_dotenv

def main():
    
    st.set_page_config(layout="wide")
    render_sidebar()
    
    st.title("簡易模型建置")
    st.write("___")
    
    uploaded_file = st.file_uploader("請上傳 CSV 檔案", type="csv")
    
    if uploaded_file is not None:
        # 讀取 CSV
        df = pd.read_csv(uploaded_file)
        
        # 顯示前幾筆資料
        st.write("資料前五筆：")
        st.dataframe(df.head())
        
        # 顯示基本統計資訊
        st.write("資料統計摘要：")
        st.write(df.describe())
    # 讀取 .env 裡的 KEY
    load_dotenv()
    API_KEY = os.environ.get("GROQ_API_KEY")
    
    if API_KEY is None:
        raise ValueError("請先設定 GROQ_API_KEY")
    
    # 設定 client
    client = Groq(api_key=API_KEY)
    
    # 呼叫聊天 API
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",  # 使用 Groq 支援的模型
        messages=[
            {"role": "system", "content": "你是友善的助手"},
            {"role": "user", "content": "用 Groq API 回答我吧！"}
        ]
    )
    
    print("AI 回應：", response.choices[0].message["content"])
if __name__ == "__main__":
    main()
