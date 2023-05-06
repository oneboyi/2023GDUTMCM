'''
Author: oneboyi
Date: 2023-05-06 15:53:56
LastEditors: oneboyi
LastEditTime: 2023-05-07 00:22:11
FilePath: \workspace\BoxPlot.py
Description: 
Copyright 2023 OBKoro1, All Rights Reserved. 
2023-05-06 15:53:56
'''
import pandas as pd
import matplotlib.pyplot as plt

# 从CSV文件中读取数据
data = pd.read_csv('workspace\data.csv')

# 创建箱线图
fig, ax = plt.subplots()
ax.boxplot(data)

# 添加标题和标签
ax.set_title('Boxplot of Data')
ax.set_xlabel('Values')

# 显示图形
plt.show()