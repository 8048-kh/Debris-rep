import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
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

town_counts = data.groupby('town').size().reset_index(name='count')

# 建立 chart_data
chart_data = pd.DataFrame({
    'town': town_counts['Town'],
    'count': town_counts['count']
})
st.write(
    f"""**Breakdown of rides per minute between {hour_selected}:00 and {(hour_selected + 1) % 24}:00**"""
)
st.altair_chart(
    alt.Chart(town_data)
    .mark_bar()
    .encode(
        x=alt.X("town:N", title="鄉鎮"),
        y=alt.Y("count:Q", title="數量"),
        tooltip=["town", "count"],
    )
    .configure_mark(opacity=0.7, color="blue")
    .properties(title="各鄉鎮數量統計")
    .interactive(),
    use_container_width=True,
)
