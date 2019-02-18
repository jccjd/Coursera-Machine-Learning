import numpy as np
import matplotlib.pyplot as plt
#输入数据
X = np.array([[1,3,3],
              [1,4,3]
              [1,1,1]
              [1,0,2]])
#标签
Y = np.array([[1],
              [1],
              [-1],
              [-1]])
#权值初始化，3行1列，取值范围-1 到 1
W = (np.random.rand([3,1]) - 0.5) * 2

print(W)
#学习率设置
lr = 0.11
#神经网络输出
O = 0
def update():
    global X,Y,W,lr
    O = np.sign(np.dot(X,W)) #shap:(3,1)
    W_C = lr * (X.T.dot(Y - O)) / int(X.shape[0])
    W = W + W_C
