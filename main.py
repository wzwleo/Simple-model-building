import streamlit as st
import pandas as pd

def render_sidebar():
    if st.sidebar.button("🔍 搜尋頁面", use_container_width=True, key="search_button"):
        st.session_state.current_page = 'search'

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
        
if __name__ == "__main__":
    main()
