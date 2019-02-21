import numpy as np
import matplotlib.pyplot as plt

#载入数据
data = np.genfromtxt('data1.txt',delimiter=' ')
plt.scatter(data[:,0],data[:,1])
plt.show()
print(data.shape)

#训练模型

