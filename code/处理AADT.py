# import pandas as pd
#
# # 读取 CSV 文件
# input_file = 'AADT_filtered.csv'  # 替换为你的输入文件路径
# df = pd.read_csv(input_file)
#
# # 创建一个空的列表来存储结果
# result = []
#
# # 遍历每一行
# for index, row in df.iterrows():
#     # 提取 node start 和 node(s) end 中的节点标号
#     nodes_start = row['node start'].strip('{}').split(', ')
#     nodes_end = row['node(s) end'].strip('{}').split(', ')
#
#     # 计算每个节点的 AADT 分配值
#     total_nodes = len(nodes_start) + len(nodes_end)
#     if total_nodes > 0:
#         aadt_value = row['AADT (Current)'] / total_nodes
#     else:
#         aadt_value = 0  # 如果没有节点，则分配值为 0
#
#     # 将每个节点及其对应的 AADT 分配值添加到结果列表中
#     for node in nodes_start + nodes_end:
#         result.append([node, aadt_value])
#
# # 将结果转换为 DataFrame
# result_df = pd.DataFrame(result, columns=['Node', 'AADT'])
#
# # 保存到新的 CSV 文件
# output_file = 'AADT_processed.csv'  # 输出文件路径
# result_df.to_csv(output_file, index=False)
#
# print(f"处理完成，结果已保存到 {output_file}")
# import pandas as pd
#
# # 读取 CSV 文件
# input_file = 'AADT_filtered.csv'  # 替换为你的输入文件路径
# df = pd.read_csv(input_file)
#
# # 创建一个空的列表来存储结果
# result = []
#
# # 遍历每一行
# for index, row in df.iterrows():
#     # 提取 node start 和 node(s) end 中的节点标号
#     # 确保值为字符串类型，并处理可能的空值或非字符串值
#     nodes_start = str(row['node start']).strip('{}').split(', ')
#     nodes_end = str(row['node(s) end']).strip('{}').split(', ')
#
#     # 移除空字符串（如果存在）
#     nodes_start = [node for node in nodes_start if node]
#     nodes_end = [node for node in nodes_end if node]
#
#     # 计算每个节点的 AADT 分配值
#     total_nodes = len(nodes_start) + len(nodes_end)
#     if total_nodes > 0:
#         aadt_value = row['AADT (Current)'] / total_nodes
#     else:
#         aadt_value = 0  # 如果没有节点，则分配值为 0
#
#     # 将每个节点及其对应的 AADT 分配值添加到结果列表中
#     for node in nodes_start + nodes_end:
#         result.append([node, aadt_value])
#
# # 将结果转换为 DataFrame
# result_df = pd.DataFrame(result, columns=['Node', 'AADT'])
#
# # 保存到新的 CSV 文件
# output_file = 'AADT_processed.csv'  # 输出文件路径
# result_df.to_csv(output_file, index=False)
#
# print(f"处理完成，结果已保存到 {output_file}")
import pandas as pd

# 读取 CSV 文件
input_file = 'AADT_filtered.csv'  # 替换为你的输入文件路径
df = pd.read_csv(input_file, na_filter=False)  # na_filter=False 防止将空字符串读为 NaN

# 创建一个空的列表来存储结果
result = []

# 遍历每一行
for index, row in df.iterrows():
    # 提取 node start 和 node(s) end 中的节点标号
    # 确保值为字符串类型，并处理可能的空值或非字符串值
    nodes_start = str(row['node start']).strip('{}').split(', ')
    nodes_end = str(row['node(s) end']).strip('{}').split(', ')

    # 移除空字符串（如果存在）
    nodes_start = [node for node in nodes_start if node]
    nodes_end = [node for node in nodes_end if node]

    # 计算每个节点的 AADT 分配值
    total_nodes = len(nodes_start) + len(nodes_end)
    if total_nodes > 0:
        aadt_value = row['AADT (Current)'] / total_nodes
    else:
        aadt_value = 0  # 如果没有节点，则分配值为 0

    # 将每个节点及其对应的 AADT 分配值添加到结果列表中
    for node in nodes_start + nodes_end:
        result.append([node, aadt_value])

# 将结果转换为 DataFrame
result_df = pd.DataFrame(result, columns=['Node', 'AADT'])

# 保存到新的 CSV 文件
output_file = 'AADT_processed.csv'  # 输出文件路径
result_df.to_csv(output_file, index=False)

print(f"处理完成，结果已保存到 {output_file}")