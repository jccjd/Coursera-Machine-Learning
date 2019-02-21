import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#载入数据
data = np.genfromtxt('data1.txt',delimiter=' ')

# #设置k值
k = 4
# #训练模型
model = KMeans(n_clusters=k)
model.fit(data)
#分类坐标中心坐标
centers = model.cluster_centers_
print(centers)
#预测结果
result = model.predict(data)
print(result)
