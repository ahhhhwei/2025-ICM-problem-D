import pandas as pd

# 读取 CSV 文件
file_path = 'MDOT_SHA_Annual_Average_Daily_Traffic_Baltimore.csv'  # 替换为您的 CSV 文件路径
df = pd.read_csv(file_path)

# 确保 'AADT' 列存在
if 'AADT' in df.columns:
    # 计算第一四分位数
    q1 = df['AADT'].quantile(0.001)
    print(f"AADT 列的第一四分位数（下1/4值）为: {q1}")
else:
    print("CSV 文件中不存在 'AADT' 列。")