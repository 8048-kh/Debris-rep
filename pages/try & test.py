import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Web App URL: <https://geotemplate.streamlit.app>
GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
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
tribes = "https://github.com/8048-kh/Debris-rep/raw/refs/heads/master/Data/Nantou_Tribe.csv"
tribes_df = pd.read_csv(tribes_url)
st.header("部落名稱")
st.table(tribes_df[["tribe name"]])
