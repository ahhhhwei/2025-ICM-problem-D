import pandas as pd
import folium

# 读取 CSV 文件
data = pd.read_csv('nodes_all_location.csv')  # 假设您的数据保存在 points.csv 文件中

# tiles= 'https://wprd01.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scl=1&style=7'

# 创建地图对象
# bj_map = folium.Map(location=[39.25, -76.58], zoom_start=11, tiles='CartoDB positron')
# bj_map = folium.Map(location=[39.25, -76.58], zoom_start=11, tiles=tiles)
bj_map = folium.Map(location=[39.25, -76.58], zoom_start=11, tiles='OpenStreetMap')
# # 遍历数据并添加标记点
# for index, row in data.iterrows():
#     folium.Marker(
#         location=[row['y'], row['x']],  # 注意：folium 中经纬度顺序为 [纬度, 经度]
#         # popup=f"OSM ID: {row['osmid']}",  # 弹出标签显示 OSM ID
#         icon=folium.Icon(color='blue')  # 设置标记颜色
#     ).add_to(bj_map)

# 遍历数据并添加标记点（仅显示前1000个点）
for index, row in data.head(1000).iterrows():
    folium.Marker(
        location=[row['y'], row['x']],  # 注意：folium 中经纬度顺序为 [纬度, 经度]
        icon=folium.Icon(color='blue')  # 设置标记颜色
    ).add_to(bj_map)

# 保存地图到 HTML 文件
bj_map.save('nodes_all.html')
print("地图已生成并保存到 nodes_all.html 文件中。")