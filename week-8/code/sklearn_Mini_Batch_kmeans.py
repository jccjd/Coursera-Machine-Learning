from sklearn.cluster import MiniBatchKMeans
import numpy as np
import matplotlib.pyplot as plt

# 载入数据
data = np.genfromtxt('data1.txt', delimiter=' ')
# 设置k值
k = 4
# 训练模型
model = MiniBatchKMeans(n_clusters=k)
model.fit(data)
#分类中心点坐标
centers = model.cluster_centers_
print(centers)
#预测结果
result = model.predict(data)


#画图
mark = ['or','ob','og','oy']
for i,d in enumerate(data):
    plt.plot(d[0],d[1],mark[result[i]])

#画出各个分类的中心
mark = ['*y','*g','*b','*r']
for i, centers in enumerate(centers):
    plt.plot(centers[0],centers[1],mark[i],markersize = 20)
plt.show()
