# import matplotlib.pyplot as plt
#
# years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
# aadt_values = [183202, 191785, 195812, 200511, 199312, 200703, 161571, 17380, 17481]
# aawdt_values = [191676, 200590, 207231, 213544, 211382, 223511, 18912, 20330, 21570]
#
# plt.figure(figsize=(10, 6))
# plt.plot(years, aadt_values, label='AADT', marker='o')
# plt.plot(years, aawdt_values, label='AAWDT', marker='x')
# plt.xlabel('Year')
# plt.ylabel('Traffic Volume')
# plt.title('Traffic Volume Trends for BALTO BELTWAY')
# plt.legend()
# plt.grid(True)
# plt.show()
# from matplotlib import pyplot as plt
#
# functional_classes = ['Principal Arterial', 'Minor Arterial', 'Major Collector']
# aadt_values = [183202, 4412, 2632]  # 示例数据
# plt.bar(functional_classes, aadt_values, color=['blue', 'green', 'orange'])
# plt.xlabel('Functional Class')
# plt.ylabel('AADT')
# plt.title('AADT by Functional Class')
# plt.show()
from matplotlib import pyplot as plt
from sympy.physics.units import years

#none
# import geopandas as gpd
# from matplotlib import pyplot as plt
#
# # 假设有一个包含道路几何信息的GeoDataFrame
# gdf = gpd.read_file('path_to_road_shapefile.shp')
# gdf['AADT'] = [183202, 4412, 2632, ...]  # 示例数据
# gdf.plot(column='AADT', cmap='viridis', legend=True)
# plt.title('Traffic Volume Distribution')
# plt.show()

import pandas as pd

data = {
    'Road Name': ['BALTO BELTWAY', 'BELLONA AVE', 'BELAIR RD'],
    'AADT': [183202, 4412, 2632],
    'AAWDT': [191676, 4722, 2822]
}
df = pd.DataFrame(data)
df.to_csv('traffic_volume_report.csv', index=False)