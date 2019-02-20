import matplotlib.pyplot as plt
import numpy as np
import operator

#已知分类数据
x1 = np.array([3,2,1])
y1 = np.array([104,100,81])
x2 = np.array([101,99,98])
y2 = np.array([10,5,2])
scatter1 = plt.scatter(x1,y1,c = 'r')
scatter2 = plt.scatter(x2,y2,c = 'b')
#未知数据
x = np.array([18])
y = np.array([90])
scatter3 = plt.scatter(x,y,c = 'k')
plt.legend(handles=[scatter1,scatter2,scatter3],labels=['labelA','labelB','x'],loc='best')
plt.show()
