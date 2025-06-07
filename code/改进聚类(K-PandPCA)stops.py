# import pandas as pd
# import numpy as np
# from sklearn.decomposition import PCA
# from kmodes.kprototypes import KPrototypes
#
# # 加载数据
# data = pd.read_csv('Bus_Stops_for_cluster.csv')
#
# # 选择参与聚类的列
# columns = ['Y', 'X', 'Rider_Tota', 'Routes_Ser', 'Mode', 'Shelter']
# data = data[columns]
#
# # 检查缺失值
# print("Missing Values:")
# print(data.isnull().sum())
#
# # 如果有缺失值，填充或删除
# data = data.dropna()  # 删除缺失值
#
# # 将类别型数据转换为数值型
# data['Mode'] = data['Mode'].astype('category').cat.codes
# data['Shelter'] = data['Shelter'].astype('category').cat.codes
#
# # 特征分析：使用 PCA 评估特征重要性
# # 选择参与聚类的特征
# X = data[['Rider_Tota', 'Routes_Ser', 'Mode', 'Shelter']]
#
# # 标准化数据
# X_normalized = (X - X.mean()) / X.std()
#
# # 使用 PCA 分析
# pca = PCA()
# pca.fit(X_normalized)
#
# # 获取每个特征的方差贡献
# explained_variance = pca.explained_variance_ratio_
#
# # 输出 PCA 结果
# print("\nExplained Variance Ratio:")
# print(explained_variance)
#
# # 将方差贡献归一化为权重
# weights = explained_variance / explained_variance.sum()
# print("\nWeights:", weights)
#
# # 选择参与聚类的列（排除 Y 和 X）
# data_cluster = data[['Rider_Total', 'Routes_Ser', 'Mode', 'Shelter']]
#
# # 数值型列的索引（从0开始）
# numeric_indices = [0]  # Rider_Total
# # 类别型列的索引
# categorical_indices = [1, 2, 3]  # Routes_Ser, Mode, Shelter
#
# # 初始化 K-Prototypes
# kproto = KPrototypes(n_clusters=5, init='Cao', verbose=2)
#
# # 拟合模型（传入权重）
# clusters = kproto.fit_predict(data_cluster, categorical=categorical_indices, weight=weights)
#
# # 将聚类结果添加到原始数据中
# data['Cluster'] = clusters
#
# # 输出聚类结果
# print("\nClustered Data:")
# print(data.head())
#
# # 保存聚类结果
# data.to_csv('Bus_Stop_Clustered.csv', index=False)
# print("\nClustering results saved to 'Bus_Stop_Clustered.csv'.")
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from kmodes.kprototypes import KPrototypes
import matplotlib.pyplot as plt
import seaborn as sns

# 加载数据
data = pd.read_csv('Bus_Stops_for_cluster.csv')

# 选择参与聚类的列
columns = ['Y', 'X', 'Rider_Tota', 'Routes_Ser', 'Mode', 'Shelter']
data = data[columns]

# 检查缺失值
print("Missing Values:")
print(data.isnull().sum())

# 如果有缺失值，填充或删除
data = data.dropna()  # 删除缺失值

# 将类别型数据转换为数值型
data['Mode'] = data['Mode'].astype('category').cat.codes
data['Shelter'] = data['Shelter'].astype('category').cat.codes

# 特征分析：使用 PCA 评估特征重要性
# 选择参与聚类的特征
X = data[['Rider_Tota', 'Routes_Ser', 'Mode', 'Shelter']]

# 标准化数据
X_normalized = (X - X.mean()) / X.std()

# 使用 PCA 分析
pca = PCA()
pca.fit(X_normalized)

# 获取每个特征的方差贡献
explained_variance = pca.explained_variance_ratio_

# 输出 PCA 结果
print("\nExplained Variance Ratio:")
print(explained_variance)

# 将方差贡献归一化为权重
weights = explained_variance / explained_variance.sum()
print("\nWeights:", weights)

# 选择参与聚类的列（排除 Y 和 X）
data_cluster = data[['Rider_Total', 'Routes_Ser', 'Mode', 'Shelter']]

# 数值型列的索引（从0开始）
numeric_indices = [0]  # Rider_Total
# 类别型列的索引
categorical_indices = [1, 2, 3]  # Routes_Ser, Mode, Shelter

# 初始化 K-Prototypes
kproto = KPrototypes(n_clusters=5, init='Cao', verbose=2)

# 拟合模型（传入权重）
clusters = kproto.fit_predict(data_cluster, categorical=categorical_indices, gamma=1.0)

# 将聚类结果添加到原始数据中
data['Cluster'] = clusters

# 输出聚类结果
print("\nClustered Data:")
print(data.head())

# 保存聚类结果
data.to_csv('Bus_Stop_Clustered.csv', index=False)
print("\nClustering results saved to 'Bus_Stop_Clustered.csv'.")

# 可视化聚类结果
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Y', y='X', hue='Cluster', data=data, palette='viridis')
plt.title('K-Prototype Clustering')
plt.xlabel('Y')
plt.ylabel('X')
plt.show()