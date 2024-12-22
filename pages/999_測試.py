import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Heatmap")

with st.expander("See source code"):
    with st.echo():
        filepath = "https://github.com/8048-kh/Debris-rep/raw/refs/heads/master/Data/Debris_Points.csv"
        m = leafmap.Map(center=[23.926170, 120.988871], zoom=9.5)
        m.add_heatmap(
            filepath,
            latitude="Y",
            longitude="X",
            value="TR_num",
            name="Heat map",
            radius=20,
        )
m.to_streamlit(height=700)
