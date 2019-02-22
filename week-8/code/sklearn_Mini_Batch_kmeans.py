from sklearn.cluster import MiniBatchKMeans
import numpy as np
import matplotlib.pyplot as plt

# 载入数据
data = np.genfromtxt('data1.txt', delimiter=' ')
# 设置k值
k = 4
# 训练模型
model = MiniBatchKMeans(n_clusters=k)
