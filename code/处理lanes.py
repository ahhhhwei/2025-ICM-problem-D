import pandas as pd
import ast  # 用于将字符串转换为列表

# 读取 CSV 文件
file_path = 'modified_edges.csv'  # 替换为您的 CSV 文件路径
df = pd.read_csv(file_path)

# 处理 lanes 列：如果出现列表，则取列表中的最大数值作为lanes的唯一值
# 假设 lanes 列中的值是以字符串形式存储的列表，例如 "[2, 3]"
def extract_max_value(value):
    try:
        # 尝试将字符串转换为列表
        value_list = ast.literal_eval(value)
        # 如果转换成功且是列表，返回最大值
        if isinstance(value_list, list):
            return max(value_list)
    except (ValueError, SyntaxError):
        pass
    # 如果不是列表或转换失败，直接返回原始值
    return value

# 应用函数处理 lanes 列
df['lanes'] = df['lanes'].apply(extract_max_value)

# 保存处理后的数据到新的 CSV 文件
output_file = 'modified_edges_new.csv'
df.to_csv(output_file, index=False)
print(f"处理后的数据已保存到 {output_file} 文件中。")