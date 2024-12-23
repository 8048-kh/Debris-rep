import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import altair as alt
st.set_page_config(layout="wide")
st.title("土石流潛勢溪流範圍熱區圖")


filepath = "https://github.com/8048-kh/Debris-rep/raw/refs/heads/master/Data/Debris_Points.csv"
df = pd.read_csv(filepath)
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

town_counts = df.groupby('Town').size().reset_index(name='count')

# 建立 chart_data
chart_data = pd.DataFrame({
    'town': town_counts['Town'],
    'count': town_counts['count']
})
chart_data = chart_data.sort_values(by=['count'], ascending=False)

st.altair_chart(
    alt.Chart(chart_data)
    .mark_bar()
    .encode(
        x=alt.X("town:N", title="鄉鎮", sort='-y'),
        y=alt.Y("count:Q", title="數量"),
        tooltip=["town", "count"],
    )
    .configure_mark(opacity=0.7, color="blue")
    .properties(title="原鄉部落與土石流潛勢溪流數量統計")
    .interactive(),
    use_container_width=True,
)
town_list = df['town'].unique().tolist()
selected_town = st.selectbox("選擇鄉鎮", town_list)

# 篩選資料並計算 Vill 數量
filtered_df = df[df['town'] == selected_town]
vill_counts = filtered_df.groupby('Vill').size().reset_index(name='count')

# 建立 chart_data
vill_data = pd.DataFrame({
    'Vill': vill_counts['Vill'],
    'count': vill_counts['count']
})

# 將資料由高到低排序
vill_data = vill_data.sort_values(by=['count'], ascending=False)

# 繪製圖表
st.altair_chart(
    alt.Chart(vill_data)
    .mark_bar()
    .encode(
        x=alt.X("Vill:N", title="Vill", sort='-y'),
        y=alt.Y("count:Q", title="數量"),
        tooltip=["Vill", "count"],
    )
    .configure_mark(opacity=0.7, color="blue")
    .properties(title=f"{selected_town} 各 Vill 數量統計")
    .interactive(),
    use_container_width=True,
)
