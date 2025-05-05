# import osmnx as ox
# import folium
# from folium.plugins import HeatMap
# import numpy as np

# # 步骤 1: 获取巴尔的摩城市的道路网络数据
# place_name = "Baltimore, Maryland, USA"
# graph = ox.graph_from_place(place_name, network_type='drive')

# # 将图转换为 GeoDataFrame
# nodes, edges = ox.graph_to_gdfs(graph)

# # 步骤 2: 模拟行车流量数据
# # 为每条道路随机生成一个行车流量值
# edges['traffic_flow'] = np.random.randint(10, 100, size=len(edges))

# # 步骤 3: 准备热力图数据
# heat_data = []
# for _, row in edges.iterrows():
#     # 获取道路的几何中心
#     line = row['geometry']
#     if line.geom_type == 'LineString':
#         center_point = line.centroid
#         heat_data.append([center_point.y, center_point.x, row['traffic_flow']])

# # 步骤 4: 绘制热力图
# # 创建一个 Folium 地图，以巴尔的摩为中心
# m = folium.Map(location=[edges.unary_union.centroid.y, edges.unary_union.centroid.x], zoom_start=12)

# # 添加热力图层
# HeatMap(heat_data, radius=10).add_to(m)

# # 保存地图为 HTML 文件
# m.save('baltimore_traffic_heatmap.html')
import matplotlib.pyplot as plt

# 初始化参数
cwnd = 1  # 初始拥塞窗口大小
ssthresh = 16  # 初始慢启动阈值
cwnd_list = [cwnd]  # 存储每个时间步的拥塞窗口大小
time_steps = [0]  # 存储时间步，初始时间为 0
t = 0  # 初始时间

# 模拟慢启动阶段
while cwnd < ssthresh:
    cwnd *= 2
    t += 1
    cwnd_list.append(cwnd)
    time_steps.append(t)

# 模拟拥塞避免阶段
while True:
    cwnd += 1
    t += 1
    cwnd_list.append(cwnd)
    time_steps.append(t)
    # 模拟发生拥塞
    if cwnd > 30:
        ssthresh = cwnd // 2  # 使用整数除法
        cwnd = 1
        break

# 模拟拥堵结束后的恢复阶段
while cwnd < ssthresh:
    cwnd *= 2
    t += 1
    cwnd_list.append(cwnd)
    time_steps.append(t)
while True:
    cwnd += 1
    t += 1
    cwnd_list.append(cwnd)