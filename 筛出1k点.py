import pandas as pd

# 读取表1和表2的数据
nodes_file = 'key_nodes.csv'  # 表1的文件路径
edges_file = 'nodes_all_filtered.csv'  # 表2的文件路径

# 读取表1数据
nodes_df = pd.read_csv(nodes_file)
# 读取表2数据
edges_df = pd.read_csv(edges_file)

# 筛选出表2中匹配表1中osmid的数据行
matched_df = edges_df[edges_df['osmid'].isin(nodes_df['osmid'])]

# 保存筛选后的数据到新的CSV文件
output_file = 'key_nodes_new.csv'
matched_df.to_csv(output_file, index=False)

print(f"匹配后的数据已保存到 {output_file} 文件中。")