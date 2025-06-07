# import pandas as pd
# import numpy as np
# from sklearn.decomposition import PCA
# from sklearn.preprocessing import OneHotEncoder, StandardScaler
#
# # 加载数据
# data = pd.read_csv('Bus_Stops_Processed.csv')
#
# # 选择参与聚类的列，删除 Routes_Ser 特征，添加 Stop_Rider 特征
# columns = ['Y', 'X', 'Rider_Tota', 'Mode', 'Shelter', 'Stop_Rider']
# data = data[columns]
#
# # 检查缺失值
# print("Missing Values:")
# print(data.isnull().sum())
#
# # 如果有缺失值，填充或删除
# data = data.dropna()  # 删除缺失值
#
# # 对类别型数据进行 One-Hot 编码
# encoder = OneHotEncoder(sparse=False, drop='first')  # 使用 drop='first' 避免多重共线性
# encoded_cats = encoder.fit_transform(data[['Mode', 'Shelter']])
#
# # 获取 One-Hot 编码后的列名
# cat_column_names = encoder.get_feature_names_out(['Mode', 'Shelter'])
#
# # 对数值型数据进行标准化
# scaler = StandardScaler()
# scaled_numerics = scaler.fit_transform(data[['Rider_Tota', 'Stop_Rider']])
#
# # 合并数值型和编码后的类别型数据
# processed_data = np.hstack((scaled_numerics, encoded_cats))
#
# # 使用 PCA 分析
# pca = PCA()
# pca.fit(processed_data)
#
# # 获取每个特征的方差贡献
# explained_variance = pca.explained_variance_ratio_
#
# # 将方差贡献映射回原始特征
# # 创建一个字典，存储每个原始特征的权重
# feature_weights = {'Rider_Tota': 0, 'Stop_Rider': 0, 'Mode': 0, 'Shelter': 0}
#
# # 遍历 PCA 的结果，将 One-Hot 编码后的特征的方差贡献合并回原始类别
# for i, col in enumerate(['Rider_Tota', 'Stop_Rider'] + list(cat_column_names)):
#     if col == 'Rider_Tota':
#         feature_weights['Rider_Tota'] += explained_variance[i]
#     elif col == 'Stop_Rider':
#         feature_weights['Stop_Rider'] += explained_variance[i]
#     elif col.startswith('Mode'):
#         feature_weights['Mode'] += explained_variance[i]
#     elif col.startswith('Shelter'):
#         feature_weights['Shelter'] += explained_variance[i]
#
# # 将权重归一化
# total_weight = sum(feature_weights.values())
# for feature in feature_weights:
#     feature_weights[feature] /= total_weight
#
# # 输出权重
# print("\nFeature Weights:")
# print(feature_weights)
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# 加载数据
data = pd.read_csv('Bus_Stops_Processed.csv')

# 选择参与聚类的列，删除 Routes_Ser 特征，添加 Stop_Rider 和 Routes_Ser 特征
columns = ['Y', 'X', 'Rider_Tota', 'Mode', 'Shelter', 'Stop_Rider', 'Routes_Ser']
data = data[columns]

# 检查缺失值
print("Missing Values:")
print(data.isnull().sum())

# 如果有缺失值，填充或删除
data = data.dropna()  # 删除缺失值

# 对类别型数据进行 One-Hot 编码
encoder = OneHotEncoder(sparse=False, drop='first')  # 使用 drop='first' 避免多重共线性
encoded_cats = encoder.fit_transform(data[['Mode', 'Shelter']])

# 获取 One-Hot 编码后的列名
cat_column_names = encoder.get_feature_names_out(['Mode', 'Shelter'])

# 对数值型数据进行标准化
scaler = StandardScaler()
scaled_numerics = scaler.fit_transform(data[['Rider_Tota', 'Stop_Rider', 'Routes_Ser']])

# 合并数值型和编码后的类别型数据
processed_data = np.hstack((scaled_numerics, encoded_cats))

# 使用 PCA 分析
pca = PCA()
pca.fit(processed_data)

# 获取每个特征的方差贡献
explained_variance = pca.explained_variance_ratio_

# 将方差贡献映射回原始特征
# 创建一个字典，存储每个原始特征的权重
feature_weights = {'Rider_Tota': 0, 'Stop_Rider': 0, 'Routes_Ser': 0, 'Mode': 0, 'Shelter': 0}

# 遍历 PCA 的结果，将 One-Hot 编码后的特征的方差贡献合并回原始类别
for i, col in enumerate(['Rider_Tota', 'Stop_Rider', 'Routes_Ser'] + list(cat_column_names)):
    if col == 'Rider_Tota':
        feature_weights['Rider_Tota'] += explained_variance[i]
    elif col == 'Stop_Rider':
        feature_weights['Stop_Rider'] += explained_variance[i]
    elif col == 'Routes_Ser':
        feature_weights['Routes_Ser'] += explained_variance[i]
    elif col.startswith('Mode'):
        feature_weights['Mode'] += explained_variance[i]
    elif col.startswith('Shelter'):
        feature_weights['Shelter'] += explained_variance[i]

# 将权重归一化
total_weight = sum(feature_weights.values())
for feature in feature_weights:
    feature_weights[feature] /= total_weight

# 输出权重
print("\nFeature Weights:")
print(feature_weights)