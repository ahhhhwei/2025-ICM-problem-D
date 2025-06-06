import pandas as pd
import folium

# 读取 CSV 文件
data = pd.read_csv('Bus_Stops.csv')  # 假设您的数据保存在 points.csv 文件中


# 创建地图对象

bj_map = folium.Map(location=[39.25, -76.58], zoom_start=11, tiles='OpenStreetMap')

# # 遍历数据并添加标记点（仅显示前1000个点）
# for index, row in data.head(1000).iterrows():
#     folium.Marker(
#         location=[row['y'], row['x']],  # 注意：folium 中经纬度顺序为 [纬度, 经度]
#         icon=folium.Icon(color='blue')  # 设置标记颜色
#     ).add_to(bj_map)

# # 遍历数据并添加标记点
for index, row in data.iterrows():
    folium.Marker(
        location=[row['Y'], row['X']],  # 注意：folium 中经纬度顺序为 [纬度, 经度]
        # popup=f"OSM ID: {row['osmid']}",  # 弹出标签显示 OSM ID
        icon=folium.Icon(color='blue')  # 设置标记颜色
    ).add_to(bj_map)
    # folium.CircleMarker(
    #     location=[row['Y'], row['X']],  # 注意：folium 中经纬度顺序为 [纬度, 经度]
    #     radius=1,  # 设置圆形标记的半径
    #     color='blue',  # 设置标记颜色
    #     fill=True,  # 是否填充
    #     fill_color='blue',  # 填充颜色
    #     fill_opacity=0.5,  # 填充透明度
    # ).add_to(bj_map)

# 保存地图到 HTML 文件
bj_map.save('bus_stops_all_another.html')
print("地图已生成并保存到 bus_stops_all.html 文件中。")