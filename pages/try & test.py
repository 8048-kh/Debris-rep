import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.title("Aboriginal Tribes")

# Create a Leafmap map object with layer control
m = leafmap.Map(center=[23.97565, 120.9738819], zoom=4, layer_control=True)

# Load the tribes data
tribes = "https://github.com/8048-kh/Debris-rep/raw/refs/heads/master/Nantou_Tribe.csv"
tribes_df = pd.read_csv(tribes)
tribe_names = tribes_df['tribe name'].tolist()

# Add points to the map
m.add_points_from_xy(
    tribes,
    x="longitude",
    y="latitude",
    icon_names=["gear", "map", "leaf", "globe"],
    #spin=True,
    add_legend=True,
    layer_name="部落點",  # 設定圖層名稱
)

# Add shp layers
#m.add_shp(
#    "https://github.com/8048-kh/Debris-rep/raw/refs/heads/master/shpfile/tribe_test.shp",
#    layer_name="部落範圍",  # 設定圖層名稱
#)
m.add_shp(
    "https://github.com/8048-kh/Debris-rep/raw/refs/heads/master/shpfile/debris_impect.shp",
    layer_name="土石流影響範圍",  # 設定圖層名稱
)

# Create a selectbox for tribe names
selected_tribe = st.selectbox("選擇部落", tribe_names, key="selectbox_tribe")

# Get the data of the selected tribe
selected_tribe_data = tribes_df[tribes_df['tribe name'] == selected_tribe].iloc[0]

# Get coordinates from 'latitude' and 'longitude'
latitude = selected_tribe_data['latitude']
longitude = selected_tribe_data['longitude']

# Recenter and zoom to the selected tribe
m.set_center(longitude, latitude, zoom=15)

# Add a marker for the selected tribe
m.add_marker(location=(latitude, longitude), tooltip=selected_tribe, popup=f"{selected_tribe}")

# Display the selected tribe
st.write(f"您選擇的部落是：{selected_tribe}")

# Display the map in Streamlit
m.to_streamlit(height=700)
