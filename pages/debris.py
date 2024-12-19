import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.title("Aboriginal Tribes")

# Create a Leafmap map object
m = leafmap.Map(center=[23.97565, 120.9738819], zoom=4)

# Load the tribes data
tribes = "https://github.com/8048-kh/Debris-rep/raw/refs/heads/master/Nantou_Tribe.csv"
debris = "https://github.com/8048-kh/Debris-rep/raw/refs/heads/master/debris_impact.geojson"
tribes_df = pd.read_csv(tribes)
tribe_names = tribes_df['tribe name'].tolist()

# Add points to the map
m.add_points_from_xy(
    tribes,
    x="longitude",
    y="latitude",
    icon_names=["gear", "map", "leaf", "globe"],
    spin=True,
    add_legend=True,
)

# Create a selectbox for tribe names
selected_tribe = st.selectbox(
    "選擇部落", tribe_names, key="selectbox_tribe"
)

# Get the data of the selected tribe
selected_tribe_data = tribes_df[tribes_df['tribe name'] == selected_tribe].iloc[0]

# Get coordinates from 'latitude' and 'longitude'
latitude = selected_tribe_data['latitude']
longitude = selected_tribe_data['longitude']
m.add_shp("https://github.com/8048-kh/Debris-rep/raw/refs/heads/master/shpfile/tribe_test.shp")
m.add_geojson(debris, layer_name='debris')
# Recenter and zoom to the selected tribe
#m.set_center(latitude, longitude, zoom=12)  # Dynamically update center and zoom level
m.set_center(longitude, latitude, zoom=15) 
# Add a marker for the selected tribe
m.add_marker(location=(latitude, longitude), tooltip=selected_tribe, popup=f"{selected_tribe}")
# Display the map in Streamlit
st.write(f"您選擇的部落是：{selected_tribe}")
m.to_streamlit(height=700)
