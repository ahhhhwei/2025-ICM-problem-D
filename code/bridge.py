import os
import requests
import osmnx as ox
import folium
from folium.plugins import HeatMap
import numpy as np

# 设置代理（根据您的 Clash 配置修改）
proxies = {
    'http': 'http://127.0.0.1:7890',  # Clash 的 HTTP 代理
    'https': 'http://127.0.0.1:7890',  # Clash 的 HTTPS 代理
}

# 配置环境变量
os.environ['HTTP_PROXY'] = proxies['http']
os.environ['HTTPS_PROXY'] = proxies['https']

# 使用代理创建 session
session = requests.Session()
session.proxies.update(proxies)

# 将 session 传递给 osmnx
ox.settings.requests_session = session

try:
    # 步骤 1: 获取巴尔的摩城市的道路网络数据
    place_name = "Baltimore, Maryland, USA"
    print("正在下载道路网络数据...")
    graph = ox.graph_from_place(place_name, network_type='drive')
    print("道路网络数据下载完成！")

    # 将图转换为 GeoDataFrame
    nodes, edges = ox.graph_to_gdfs(graph)

    # 步骤 2: 模拟行车流量数据
    # 为每条道路随机生成一个行车流量值
    np.random.seed(42)  # 设置随机种子以确保结果可重复
    edges['traffic_flow'] = np.random.randint(10, 100, size=len(edges))

    # 步骤 3: 准备热力图数据
    heat_data = []
    for _, row in edges.iterrows():
        # 获取道路的几何中心
        line = row['geometry']
        if line.geom_type == 'LineString':
            center_point = line.centroid
            heat_data.append([center_point.y, center_point.x, row['traffic_flow']])

    # 步骤 4: 绘制热力图
    # 创建一个 Folium 地图，以巴尔的摩为中心
    map_center = [edges.unary_union.centroid.y, edges.unary_union.centroid.x]
    m = folium.Map(location=map_center, zoom_start=12)

    # 添加热力图层
    HeatMap(
        heat_data,
        radius=15,  # 调整热力点的半径
        blur=10,    # 调整热力点的模糊程度
        max_zoom=13  # 设置热力点的最大缩放级别
    ).add_to(m)

    # 保存地图为 HTML 文件
    output_file = 'baltimore_traffic_heatmap.html'
    m.save(output_file)
    print(f"热力图已生成并保存到 {output_file} 文件中。")

except requests.exceptions.ProxyError as e:
    print("代理配置错误，请检查代理地址和端口是否正确。")
    print(f"错误详情: {e}")
except Exception as e:
    print("程序运行出错，请检查网络连接或代码逻辑。")
    print(f"错误详情: {e}")