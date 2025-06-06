#one
# import folium
#
# print(folium.__version__)
#
# # define the world map
# world_map = folium.Map()
# # save world map
# world_map.save('test_01.html')
#
# # define the national map
# national_map = folium.Map(location=[35.3, 100.6], zoom_start=4)
# # save national map
# national_map.save('test_02.html')
#
# # define the national map
# city_map = folium.Map(location=[39.93, 116.40], zoom_start=10)
# # save national map
# city_map.save('test_03.html')

import folium

# bj_map = folium.Map(location=[39.93, 115.40], zoom_start=12, tiles='Stamen Terrain')
# bj_map = folium.Map(location=[39.93, 115.40], zoom_start=12, tiles='CartoDB positron')
bj_map = folium.Map(location=[39.25, -76.58], zoom_start=12, tiles='CartoDB positron')

folium.Marker(
    location=[39.25, -76.58],
    popup='Mt. Hood Meadows',
    icon=folium.Icon(icon='cloud')
).add_to(bj_map)

folium.Marker(
    location=[39.18, -76.71],
    popup='Timberline Lodge',
    icon=folium.Icon(color='green')
).add_to(bj_map)

folium.Marker(
    location=[39.33, -76.45],
    popup='Some Other Location',
    icon=folium.Icon(color='red', icon='info-sign')  # 标记颜色  图标
).add_to(bj_map)

bj_map.save('test_04.html')


# import folium
#
# # bj_map = folium.Map(location=[39.93, 116.40], zoom_start=12, tiles='Stamen Toner')
# bj_map = folium.Map(location=[39.93, 116.40], zoom_start=12, tiles='CartoDB positron')
#
#
# folium.Circle(
#     radius=200,
#     location=(39.92, 116.43),
#     popup='The Waterfront',
#     color='#00FFFF',  # 颜色
#     fill=False,  # 填充
# ).add_to(bj_map)
#
# folium.CircleMarker(
#     location=(39.93, 116.38),
#     radius=50,  # 圆的半径
#     popup='Laurelhurst Park',
#     color='#FF1493',
#     fill=True,
#     fill_color='#FFD700'
# ).add_to(bj_map)
#
# bj_map.save('test_05.html')


# import folium
#
# # dynamic_tagging = folium.Map(
# #     location=[46.8527, -121.7649],
# #     tiles='Stamen Terrain',
# #     zoom_start=13
# # )
# dynamic_tagging = folium.Map(
#     location=[46.8527, -121.7649],
#     tiles='CartoDB positron',  # 使用 CartoDB positron 瓦片图层
#     zoom_start=13
# )
#
# folium.Marker(
#     [46.8354, -121.7325],
#     popup='Camp Muir'
# ).add_to(dynamic_tagging)
#
# dynamic_tagging.add_child(folium.ClickForMarker(popup='Waypoint'))
# dynamic_tagging.save('test_06.html')