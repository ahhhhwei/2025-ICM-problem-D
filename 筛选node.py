import pandas as pd

# 读取数据
data = pd.read_csv('nodes_drive.csv', low_memory=False)  # 替换为实际文件路径

# 定义筛选条件
lat_min, lat_max = 39.18, 39.33
lon_min, lon_max = -76.71, -76.45

# 筛选数据
filtered_data = data[(data['y'] >= lat_min) & (data['y'] <= lat_max) &
                     (data['x'] >= lon_min) & (data['x'] <= lon_max)]

# 将筛选后的数据保存到新的CSV文件
filtered_data.to_csv('nodes_drive_filtered.csv', index=False)  # 保存时不包含索引[^24^][^25^][^28^]