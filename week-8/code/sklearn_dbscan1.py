import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
#载入数据
data = np.genfromtxt('data1.txt',delimiter=' ')
model = DBSCAN(eps=1,min_samples=4)
model.fit(data)

result = model.fit_predict(data)
print(result)