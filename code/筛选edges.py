import pandas as pd

# 读取 edges 和 nodes 数据
edges = pd.read_csv('edges_drive.csv')  # 假设 edges 数据保存在 edges.csv 文件中
nodes = pd.read_csv('nodes_drive_filtered.csv')  # 假设 nodes 数据保存在 nodes.csv 文件中

# 获取 nodes 中的 osmid 列作为筛选依据
osmid_set = set(nodes['osmid'])

# 筛选 edges 中的 u 和 v 列，保留与 osmid 有交集的行
filtered_edges = edges[(edges['u'].isin(osmid_set)) & (edges['v'].isin(osmid_set))]

# 将筛选后的数据保存为新的 CSV 文件
filtered_edges.to_csv('edges_drive_filtered.csv', index=False)

print("筛选完成，结果已保存到csv 文件中")