import pandas as pd
from kmodes.kprototypes import KPrototypes
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import rgb2hex

# 读取CSV文件
df = pd.read_csv('Bus_Stops_Processed.csv')

# 选择用于聚类的特征，包括新添加的 Stops_Rider 和 Routes_Ser 特征，以及 X 和 Y
features = ['X', 'Y', 'Rider_Tota', 'Mode', 'Shelter', 'Stop_Rider', 'Routes_Ser']  # normal1
data = df[features]

# 定义数值型和分类型特征的列索引
num_cols = [0, 1, 2, 5, 6]  # X, Y, Rider_Tota, Stop_Rider, Routes_Ser
cat_cols = [3, 4]  # Mode, Shelter

# 特征权重
feature_weights = {
    'X': 0.8,  # 假设 X 的权重为 0.1
    'Y': 0.8,  # 假设 Y 的权重为 0.1
    'Rider_Tota': 0.6283046502237618,
    'Stop_Rider': 0.2177798023494044,
    'Routes_Ser': 0.11650853719240595,
    'Mode': 0.03646997590482444,
    'Shelter': 0.0009370343296034162
}

# 对数值型特征进行加权处理
for col in num_cols:
    feature_name = features[col]
    data[feature_name] = data[feature_name] * feature_weights[feature_name]

# 初始化K-Prototype模型
kproto = KPrototypes(n_clusters=5, init='Cao', random_state=42)

# 进行聚类
clusters = kproto.fit_predict(data, categorical=cat_cols)

# 将聚类结果添加到原始数据中
df['Cluster'] = clusters

# 计算每个簇的大小
cluster_sizes = df['Cluster'].value_counts().sort_index()

# 将簇的大小归一化
df['Cluster_Importance'] = df['Cluster'].map(cluster_sizes) / cluster_sizes.max()

# 保存到新的CSV文件
df.to_csv('clustered_bus_stops.csv', index=False)

# 可视化聚类结果
# 根据类别重要性给点上色
# 使用红色、橙色、黄色、绿色、灰色等颜色
palette = sns.color_palette("Reds", n_colors=5)  # 生成红色系颜色
palette_hex = [rgb2hex(color) for color in palette]  # 将RGB颜色转换为十六进制

# 定义颜色映射
color_map = {
    0: palette_hex[4],  # 红色
    1: palette_hex[3],  # 橙色
    2: palette_hex[2],  # 黄色
    3: palette_hex[1],  # 绿色
    4: palette_hex[0],  # 灰色
    # 5: palette_hex[0]   # 蓝色
}
# 将簇编号映射到颜色
df['Color'] = df['Cluster'].map(color_map)

# 可视化
plt.figure(figsize=(10, 6))
sns.scatterplot(x='X', y='Y', hue='Cluster', data=df, palette=color_map, size='Cluster', sizes=(50, 50), legend='full')
plt.title('K-Prototype Clustering')
plt.xlabel('X')
plt.ylabel('Y')

# # 在图的左上角标注每个簇的特征重要性
# for i, size in enumerate(cluster_sizes):
#     plt.text(0.05, 0.95 - i * 0.05, f'Cluster {i}: Importance = {size:.2f}', transform=plt.gca().transAxes, fontsize=10, color=color_map[i])

plt.show()
# import pandas as pd
# from kmodes.kprototypes import KPrototypes
# import matplotlib.pyplot as plt
# import seaborn as sns
# from matplotlib.colors import rgb2hex
#
# # 读取CSV文件
# df = pd.read_csv('Bus_Stops_Processed.csv')
#
# # 选择用于聚类的特征，包括新添加的 Stops_Rider 和 Routes_Ser 特征，以及 X 和 Y
# features = ['X', 'Y', 'Rider_Tota', 'Mode', 'Shelter', 'Stop_Rider', 'Routes_Ser']  # normal1
# data = df[features]
#
# # 定义数值型和分类型特征的列索引
# num_cols = [0, 1, 2, 5, 6]  # X, Y, Rider_Tota, Stop_Rider, Routes_Ser
# cat_cols = [3, 4]  # Mode, Shelter
#
# # 初始化K-Prototype模型
# kproto = KPrototypes(n_clusters=5, init='Cao', random_state=42)
#
# # 进行聚类
# clusters = kproto.fit_predict(data, categorical=cat_cols)
#
# # 将聚类结果添加到原始数据中
# df['Cluster'] = clusters
#
# # 计算每个簇的大小
# cluster_sizes = df['Cluster'].value_counts().sort_index()
#
# # 将簇的大小归一化
# df['Cluster_Importance'] = df['Cluster'].map(cluster_sizes) / cluster_sizes.max()
#
# # 保存到新的CSV文件
# df.to_csv('clustered_bus_stops.csv', index=False)
#
# # 可视化聚类结果
# # 根据类别重要性给点上色
# # 使用红色、橙色、黄色、绿色、灰色等颜色
# palette = sns.color_palette("Reds", n_colors=5)  # 生成红色系颜色
# palette_hex = [rgb2hex(color) for color in palette]  # 将RGB颜色转换为十六进制
#
# # 定义颜色映射
# color_map = {
#     0: palette_hex[4],  # 红色
#     1: palette_hex[3],  # 橙色
#     2: palette_hex[2],  # 黄色
#     3: palette_hex[1],  # 绿色
#     4: palette_hex[0],  # 灰色
#     # 5: palette_hex[0]   # 蓝色
# }
# # 将簇编号映射到颜色
# df['Color'] = df['Cluster'].map(color_map)
#
# # 可视化
# plt.figure(figsize=(10, 6))
# sns.scatterplot(x='X', y='Y', hue='Cluster', data=df, palette=color_map, size='Cluster', sizes=(50, 50), legend='full')
# plt.title('K-Prototype Clustering')
# plt.xlabel('X')
# plt.ylabel('Y')
#
# # # 在图的左上角标注每个簇的特征重要性
# # for i, size in enumerate(cluster_sizes):
# #     plt.text(0.05, 0.95 - i * 0.05, f'Cluster {i}: Importance = {size:.2f}', transform=plt.gca().transAxes, fontsize=10, color=color_map[i])
#
# plt.show()