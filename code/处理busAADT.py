import pandas as pd

# 读取CSV文件
df = pd.read_csv('MDOT_SHA_Annual_Average_Daily_Traffic_Baltimore_2.csv')

# # 删除第3列为空值的行
# df = df.dropna(subset=[df.columns[2]])
# 删除'AADT Bus'列为空值的行
df = df.dropna(subset=['AADT Bus'])

# 将处理后的数据保存到新的CSV文件
df.to_csv('AADT_Bus.csv', index=False)