import numpy as np 
from numpy import genfromtxt
import matplotlib.pyplot as plt

#载入数据
data = np.genfromtxt('data3.txt',delimiter = ',')
x_data = data[:,0,newaxis]
y_data = data[:,1,newaxis]
plt.scatter(x_data,y_data)
plt.show()

