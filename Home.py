import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Web App URL: <https://nantoudebris.streamlit.app/>
GitHub Repository: <https://github.com/8048-kh/Debris-rep/tree/master>
Image：https://esg.businesstoday.com.tw/article/category/180687/post/202308060025/%E7%AB%9F%E8%A2%AB%E5%9C%9F%E7%9F%B3%E6%B5%81%E5%9F%8B%E4%BA%867%E6%AC%A1%EF%BC%81%E5%8D%97%E6%8A%95%E4%BB%81%E6%84%9B%E9%84%89%E9%80%99%E9%96%93%E5%8A%A0%E6%B2%B9%E7%AB%99%E3%80%8C%E5%8F%B2%E4%B8%8A%E8%A2%AB%E6%8E%A9%E5%9F%8B%E6%9C%80%E5%A4%9A%E6%AC%A1%E5%BB%BA%E7%89%A9%E3%80%8D%EF%BC%8C%E6%A9%AB%E8%B7%A824%E5%B9%B4%E7%85%A7%E7%89%87%E6%9B%9D%E5%85%89
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://s3-ap-northeast-1.amazonaws.com/lazybusiness/data/nellhung_175/images/2023/08/0806/1.jpeg"
st.sidebar.image(logo)

# Customize page title
st.title("南投原鄉部落與土石流分布")

st.markdown(
    """
    南投原鄉部落與土石流潛勢溪流、土石流潛勢溪流範圍分布
    """
)

st.header("目錄")

markdown = """
1. 原鄉部落座標與資訊
2. 原鄉部落與土石流潛勢溪流
3. 原鄉部落與土石流潛勢溪流範圍

"""

st.markdown(markdown)


m = leafmap.Map(center=[23.932630, 120.986852], zoom=10)
#tribes = "https://github.com/8048-kh/Debris-rep/raw/refs/heads/master/Data/Nantou_Tribe.csv"
tribes_df = pd.read_csv("https://github.com/8048-kh/Debris-rep/raw/refs/heads/master/Data/Nantou_Tribe.csv")
st.header("部落名稱")
st.table(tribes_df[["tribe name"]])
