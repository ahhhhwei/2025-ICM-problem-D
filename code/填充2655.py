import pandas as pd

# 读取 CSV 文件
file_path = 'merged_nodes_with_aadt.csv'  # 替换为您的 CSV 文件路径
df = pd.read_csv(file_path)

# 检查 'AADT' 列是否存在
if 'AADT' in df.columns:
    # 填充空白值为 2655.0
    df['AADT'].fillna(81, inplace=True)

    # 保存修改后的数据到新的 CSV 文件
    df.to_csv('modified_nodes_with_aadt.csv', index=False)
    print("空白值已填充并保存到 'modified_nodes_with_aadt.csv' 文件中。")
else:
    print("CSV 文件中不存在 'AADT' 列。")