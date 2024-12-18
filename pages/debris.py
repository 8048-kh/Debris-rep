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

st.title("Marker Cluster")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[40, -100], zoom=4)
        tribe = 'https://github.com/8048-kh/Debris-rep/raw/refs/heads/master/nantou%20tribe.shp'
        debris = 'https://github.com/8048-kh/Debris-rep/raw/refs/heads/master/debris%20imp.shp'

        m.add_shp(tribe, layer_name='tribe')
        m.add_shp(debris, layer_name='debris')
        m.add_points_from_xy(
            tribe,
            x="longitude",
            y="latitude",
            color_column='region',
            icon_names=['gear', 'map', 'leaf', 'globe'],
            spin=True,
            add_legend=True,
        )
        
m.to_streamlit(height=700)
