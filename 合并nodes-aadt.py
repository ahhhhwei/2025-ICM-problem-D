import pandas as pd

# 读取表1和表2的数据
table1 = pd.read_csv('nodes_all_filtered_small.csv')  # 表1的文件路径
table2 = pd.read_csv('AADT_processed.csv')  # 表2的文件路径

# 使用merge方法根据osmid匹配表2中的AADT值到表1
# 选择左连接（left join），保留表1的所有行，即使在表2中没有匹配的行
merged_table = pd.merge(table1, table2, on='osmid', how='left')

# 将NaN值替换为空字符串
merged_table['AADT'] = merged_table['AADT'].fillna('')

# 查看合并后的前几行数据
print("合并后的数据预览：")
print(merged_table.head())

# 保存合并后的数据到新的CSV文件
merged_table.to_csv('merged_nodes_with_aadt.csv', index=False)
print("匹配后的数据已保存到 'merged_nodes_with_aadt.csv' 文件中。")