#two
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# 示例数据：节点数据
nodes_data = {
    'osmid': [1, 2, 3, 4, 5, 6, 7, 8],
    'x': [39.2, 39.3, 39.4, 39.5, 39.6, 39.7, 39.8, 39.9],
    'y': [-76.8, -76.7, -76.6, -76.5, -76.4, -76.3, -76.2, -76.1]
}

# 示例数据：边数据
edges_data = {
    'u': [1, 2, 3, 4, 5, 6, 7, 1, 3, 5, 7],
    'v': [2, 3, 4, 5, 6, 7, 8, 4, 6, 8, 2],
    'length': [1.5, 2.0, 3.0, 1.0, 2.5, 3.5, 4.0, 2.0, 1.5, 3.0, 2.5],  # 权重1：边的长度
    'maxspeed': [50, 60, 70, 40, 55, 65, 75, 45, 50, 60, 55],         # 权重2：最大速度
    'color': ['red', 'blue', 'green', 'orange', 'purple', 'yellow', 'pink', 'cyan', 'magenta', 'brown', 'gray'],  # 边的颜色
    'width': [2, 3, 4, 2, 3, 4, 5, 3, 4, 5, 3]  # 边的宽度
}

# 将数据转换为DataFrame
nodes_df = pd.DataFrame(nodes_data)
edges_df = pd.DataFrame(edges_data)

# 创建一个有向图
G = nx.DiGraph()

# 添加节点
for _, row in nodes_df.iterrows():
    G.add_node(row['osmid'], pos=(row['x'], row['y']))  # 使用 x 和 y 作为节点位置

# 添加边，并为每条边添加权重和其他属性
for _, row in edges_df.iterrows():
    G.add_edge(row['u'], row['v'], length=row['length'], maxspeed=row['maxspeed'], color=row['color'], width=row['width'])

# 使用 spring_layout 自动调整节点位置
pos = nx.spring_layout(G, seed=42)  # seed 参数用于固定布局，便于重复绘制

# 绘制图
plt.figure(figsize=(12, 8))

# 绘制节点
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue', edgecolors='black', linewidths=1)

# 绘制边
edges = G.edges(data=True)
edge_colors = [edge[2]['color'] for edge in edges]  # 获取边的颜色
edge_widths = [edge[2]['width'] for edge in edges]  # 获取边的宽度
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=20, edge_color=edge_colors, width=edge_widths)

# 添加节点标签
nx.draw_networkx_labels(G, pos, font_size=12, font_color='black', font_weight='bold')

# 添加边权重（以长度为例）
edge_labels = nx.get_edge_attributes(G, 'length')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)

# 设置标题
plt.title("Complex Directed Graph with Weighted Edges", fontsize=16)

# 显示图形
plt.axis('off')  # 关闭坐标轴
plt.show()