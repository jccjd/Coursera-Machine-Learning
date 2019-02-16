import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.datasets import make_gaussian_quantiles
from sklearn.preprocessing import PolynomialFeatures

#生成2维正态分布，生成的数据按分位数分为两类，500个样本2个特征
#可以生成两类或多类数据
x_data, y_data = make_gaussian_quantiles(n_samples=500,n_features=2,n_classes=2)
plt.scatter(x_data[:,0],x_data[:,1],c = y_data)
plt.show()
logistic = linear_model.LogisticRegression()
logistic.fit(x_data,y_data)