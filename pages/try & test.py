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
#m.add_geojson(tribes, layer_name='tribes')
m.add_points_from_xy(
            tribes,
            x="longitude",
            y="latitude",
            spin=False,
        )
m.add_marker(location=(latitude, longitude), tooltip=selected_tribe, popup=f"{selected_tribe}")
m.to_streamlit(height=700)
