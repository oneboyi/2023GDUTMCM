# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, f1_score

# 读取数据
data = pd.read_csv('data.csv')

# 从DataFrame中提取水流量数据作为特征
Xtrain = data['region_7'].values.reshape(-1, 1)
Xtest = data['region_8'].values.reshape(-1, 1)
# 定义孤立森林模型
model = IsolationForest(n_estimators=100, contamination=0.05)

# 拟合模型
model.fit(Xtrain)

# 预测异常值
y_pred = model.predict(Xtest)

# 输出异常值
outliers = Xtest[np.where(y_pred == -1)]

print('异常值：', outliers)
accuracy = accuracy_score(y_true=np.ones(len(Xtest)), y_pred=y_pred)
print('预测准确率：', accuracy)
f1score = f1_score(y_true=np.ones(len(Xtest)), y_pred=y_pred)
print('F1分数：', f1score)

'''
# 绘制散点图
plt.scatter(np.arange(len(Xtest)), Xtest, c=y_pred, cmap='viridis')

# 添加标签和标题
plt.xlabel('Day')
plt.ylabel('WaterFlow')
plt.title('Result')

# 显示图形
plt.show()
'''
