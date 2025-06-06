import pandas as pd
import numpy as np

# 从CSV文件读取数据
data = pd.read_csv('sensitivity.csv')  # 假设数据存储在data.csv文件中

# 提取y0, y1, y2列
y0 = data['y0']
y1 = data['y1']
y2 = data['y2']

# 计算均方误差
mse_y1_y0 = np.mean((y1 - y0) ** 2)
mse_y2_y0 = np.mean((y2 - y0) ** 2)

# 输出结果
print(f"MSE(y1, y0): {mse_y1_y0}")
print(f"MSE(y2, y0): {mse_y2_y0}")