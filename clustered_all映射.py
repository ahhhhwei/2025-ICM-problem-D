import pandas as pd
import folium

# 读取 CSV 文件
data = pd.read_csv('clustered_bus_stops.csv')  # 假设您的数据保存在 nodes_all_location.csv 文件中

# 创建地图对象
# bj_map = folium.Map(location=[39.25, -76.58], zoom_start=11, tiles='OpenStreetMap')
# bj_map = folium.Map(location=[39.25, -76.58], zoom_start=11, tiles='https://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}{r}.png', attr='Stamen Toner Lite')
# bj_map = folium.Map(location=[39.25, -76.58], zoom_start=11, tiles='Stamen Toner Lite', attr='Stamen Toner Lite')
bj_map = folium.Map(location=[39.25, -76.58], zoom_start=11, tiles=None)  # 先不设置底图

# 添加 OpenStreetMap 底图并设置透明度
folium.TileLayer(
    tiles='OpenStreetMap',  # 使用 OpenStreetMap 底图
    attr='OpenStreetMap',   # 设置底图属性
    opacity=0.5,            # 设置底图透明度（0 到 1 之间，0 为完全透明，1 为不透明）
    name='OpenStreetMap'    # 设置底图名称
).add_to(bj_map)

# 定义颜色映射
color_map = {
    4: 'red',    # Cluster == 4 时，标注为红色
    0: 'darkorange', # Cluster == 0 时，标注为橙色
    1: 'orange',   # Cluster == 1 时，标注为粉色
    3: 'darkblue', # Cluster == 3 时，标注为淡粉色
    2: 'blue'  # Cluster == 2 时，标注为淡蓝色
}

# # 遍历数据并添加标记点（仅显示前1000个点）
# for index, row in data.head(1000).iterrows():
#     cluster = row['Cluster']
#     if cluster in color_map:
#         folium.Marker(
#             location=[row['y'], row['x']],  # 注意：folium 中经纬度顺序为 [纬度, 经度]
#             icon=folium.Icon(color=color_map[cluster])  # 设置标记颜色
#         ).add_to(bj_map)
# # 遍历数据并添加标记点
# for index, row in data.iterrows():
#     cluster = row['Cluster']
#     if cluster in color_map:
#         folium.Marker(
#             location=[row['Y'], row['X']],  # 注意：folium 中经纬度顺序为 [纬度, 经度]
#             icon=folium.Icon(color=color_map[cluster])  # 设置标记颜色
#         ).add_to(bj_map)
#
# 遍历数据并添加圆形标记点
for index, row in data.iterrows():
    cluster = row['Cluster']
    if cluster in color_map:
        folium.CircleMarker(
            location=[row['Y'], row['X']],  # 注意：folium 中经纬度顺序为 [纬度, 经度]
            radius=1,  # 设置圆点的半径
            color=color_map[cluster],  # 设置圆点的颜色
            fill=True,  # 填充圆点
            fill_opacity=0.6  # 设置填充的透明度
        ).add_to(bj_map)

# 保存地图到 HTML 文件
bj_map.save('clustered_all.html')
print("地图已生成并保存到 nodes_all.html 文件中。")