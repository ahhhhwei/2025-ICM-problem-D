import pandas as pd

# 读取CSV文件
df = pd.read_csv('clustered_bus_stops.csv')

# 筛选出Cluster列数值为4的数据行
filtered_df = df[df['Cluster'] == 4]

# 将筛选后的数据保存为新的CSV文件
filtered_df.to_csv('filtered_bus_stops.csv', index=False)

print("筛选后的数据已保存到 'filtered_bus_stops.csv'.")