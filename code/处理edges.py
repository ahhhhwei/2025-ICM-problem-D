# import pandas as pd
#
# # 读取 CSV 文件
# file_path = 'edges_all_filtered_small.csv'  # 替换为您的 CSV 文件路径
# df = pd.read_csv(file_path)
#
# # 处理 lanes 列：空值填充为 1
# df['lanes'].fillna(1, inplace=True)
#
# # 处理 maxspeed 列：去除单位 mph，并填充空值为 10
# # 提取数值部分（假设速度单位都是 mph）
# df['maxspeed'] = df['maxspeed'].str.extract(r'(\d+)').astype(float)
# # 填充空值为 10
# df['maxspeed'].fillna(10, inplace=True)
#
# # 处理 oneway 列：TRUE 替换为 1，FALSE 替换为 0
# df['oneway'] = df['oneway'].map({'TRUE': 1, 'FALSE': 0})
#
# # 保存处理后的数据到新的 CSV 文件
# output_file = 'modified_edges.csv'
# df.to_csv(output_file, index=False)
# print(f"处理后的数据已保存到 {output_file} 文件中。")
import pandas as pd

# 读取 CSV 文件
file_path = 'edges_all_filtered_small.csv'  # 替换为您的 CSV 文件路径
df = pd.read_csv(file_path)

# 处理 lanes 列：空值填充为 1
df['lanes'].fillna(1, inplace=True)

# 处理 maxspeed 列：去除单位 mph，并填充空值为 10
# 提取数值部分（假设速度单位都是 mph）
df['maxspeed'] = df['maxspeed'].str.extract(r'(\d+)').astype(float)
# 填充空值为 10
df['maxspeed'].fillna(10, inplace=True)

# 处理 oneway 列：TRUE 替换为 1，FALSE 替换为 0
# 确保所有值的大小写一致，并去除空格
# 先将列转换为字符串类型，再使用 .str 方法
df['oneway'] = df['oneway'].astype(str).str.strip().str.upper().map({'TRUE': 1, 'FALSE': 0})

# 保存处理后的数据到新的 CSV 文件
output_file = 'modified_edges.csv'
df.to_csv(output_file, index=False)
print(f"处理后的数据已保存到 {output_file} 文件中。")