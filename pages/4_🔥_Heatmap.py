import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
Web App URL: <https://geotemplate.streamlit.app>
GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Heatmap")

with st.expander("See source code"):
    with st.echo():
        filepath = "https://github.com/8048-kh/Debris-rep/raw/refs/heads/master/Data/Debris_Points.csv"
        m = leafmap.Map(center=[40, -100], zoom=4, tiles="filepath")
        m.add_heatmap(
            filepath,
            latitude="Y",
            longitude="X",
            value="ID",
            name="Heat map",
            radius=20,
        )
m.to_streamlit(height=700)
