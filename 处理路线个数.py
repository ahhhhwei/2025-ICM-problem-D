import pandas as pd

# 加载数据
data = pd.read_csv('Bus_Stops_for_cluster.csv')

# 选择参与处理的列
columns = ['Y', 'X', 'Rider_Tota','Stop_Rider' ,'Routes_Ser', 'Mode', 'Shelter']
data = data[columns]

# # 检查缺失值
# print("Missing Values:")
# print(data.isnull().sum())
#
# # 如果有缺失值，填充或删除
# data = data.dropna()  # 删除缺失值

# 处理 Routes_Ser 列
# 根据逗号拆开并统计个数
data['Routes_Ser_Count'] = data['Routes_Ser'].apply(lambda x: len(x.split(',')))

# 用个数替换原来的 Routes_Ser 列
data['Routes_Ser'] = data['Routes_Ser_Count']

# 保存处理后的数据到新的 CSV 文件
data.to_csv('Bus_Stops_Processed.csv', index=False)
print("\nProcessed data saved to 'Bus_Stops_Processed.csv'.")