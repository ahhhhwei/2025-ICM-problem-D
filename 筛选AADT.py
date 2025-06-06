import pandas as pd

# 读取 CSV 文件
file_path = 'MDOT_SHA_Annual_Average_Daily_Traffic_Baltimore.csv'  # 替换为你的 CSV 文件路径
df = pd.read_csv(file_path)  # 如果文件分隔符不是逗号，可以指定 sep 参数，例如 sep='\t'[^4^]

# 删除第1列和第2列均为空值的行
df_cleaned = df.dropna(subset=[df.columns[0], df.columns[1]], how='all')

# 将处理后的数据存入新的 CSV 文件
output_path = 'AADT_filtered.csv'  # 输出文件路径
df_cleaned.to_csv(output_path, index=False)  # index=False 表示不将索引写入文件[^5^]

print(f"处理后的数据已保存到 {output_path}")