import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.title("Aboriginal Tribes")



m = leafmap.Map(center=[23.97565, 120.9738819], zoom=4)
tribes = "https://github.com/8048-kh/Debris-rep/raw/refs/heads/master/nantou%20tribe.csv"
tribes_df = pd.read_csv(tribes)
tribe_names = tribes_df['tribe name'].tolist()

# Create a selectbox for tribe names
        
selected_tribe = st.selectbox(
    "選擇部落", tribe_names, key="selectbox_tribe"
)
selected_tribe_data = tribes_df[tribes_df['tribe name'] == selected_tribe].iloc[0]
latitude = selected_tribe_data['latitude']
longitude = selected_tribe_data['longitude']

# 更新地圖中心和縮放級別
m.center = (latitude, longitude)  
m.zoom = 20  # 設定縮放級別為 12 或任何你想要的級別

m.add_points_from_xy(
            tribes,
            x="longitude",
            y="latitude",
            icon_names=["gear", "map", "leaf", "globe"],
            spin=True,
            add_legend=True,
        )

m.to_streamlit(height=700)

# Display the selected tribe
st.write(f"您選擇的部落是：{selected_tribe}")
