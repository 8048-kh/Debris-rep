import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import geopandas as gpd
st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.title("Aboriginal Tribes")

# Create a Leafmap map object
m = leafmap.Map(center=[23.97565, 120.9738819], zoom=4)

# Load the tribes data
tribes = "https://github.com/8048-kh/Debris-rep/raw/refs/heads/master/Data/Nantou_Tribe.csv"
streams = "https://github.com/8048-kh/Debris-rep/raw/refs/heads/master/Data/streams.geojson"
tribes_df = pd.read_csv(tribes)
tribe_names = tribes_df['tribe name'].tolist()

# Add points to the map
# Create a selectbox for tribe names
selected_tribe = st.selectbox(
    "選擇部落", tribe_names, key="selectbox_tribe"
)

# Get the data of the selected tribe
selected_tribe_data = tribes_df[tribes_df['tribe name'] == selected_tribe].iloc[0]

# Get coordinates from 'latitude' and 'longitude'
latitude = selected_tribe_data['latitude']
longitude = selected_tribe_data['longitude']
m.add_shp("https://github.com/8048-kh/Debris-rep/raw/refs/heads/master/shpfile/tribetest/tribes_p1.shp")
gdf = gpd.read_file("https://github.com/8048-kh/Debris-rep/raw/refs/heads/master/Data/streams.geojson")  # 替換為您的 GeoJSON 檔案路徑

color_dict = {
    "低": "green",
    "中": "yellow",
    "高": "red",
}

def style_callback(feature):
    return {
        "color": color_dict.get(feature["properties"]["Risk"], "gray"),
        "weight": 2,
    }

m = leafmap.Map()
m.add_geojson(
    gdf, 
    style_callback=style_callback,
        add_legend=True,
)
legend_dict = {
    "低": "green",
    "中": "yellow",
    "高": "red",
}

m.add_legend(
    title="Risk Level",
    legend_dict=legend_dict,
    opacity=1.0,
    position="bottomright",
)

# Recenter and zoom to the selected tribe
m.set_center(longitude, latitude, zoom=15) 
m.add_marker(location=(latitude, longitude), tooltip=selected_tribe, popup=f"{selected_tribe}")
# Display the map in Streamlit
st.write(f"您選擇的部落是：{selected_tribe}")
m.to_streamlit(height=700)
