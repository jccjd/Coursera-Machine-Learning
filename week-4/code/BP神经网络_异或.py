import numpy as np
#输入数据
X = np.array([[1,0,0],
              [1,0,1]
              [1,1,0]
              [1,1,1]])
#标签
Y = np.array([-1,1,1,-1])
#权值初始化，取值范围-1到1
V = np.random.random((3,4))*2 -1
W = np.random.random((4,1))*2 -1

print(V)
print(W)
#学习率设置
lr = 0.11
def sigmoid(x):
    return 1/(1 + np.exp(-x))
def dsigmoid(x):
    return x(1-x)
def update():
    global X,Y,W,V,lr
    L1 = sigmoid(np.dot(X,V)) #隐藏层输出（4,4）
    L2 = sigmoid(np.dot(L1,W))#输出层输出（4,1）

    L2_delta = (Y.T - L2)*dsigmoid(L2)
    L1_delta = L2_delta.dot(W.T)*dsigmoid(L1)

    W_C = lr * L1.T.dot(L2_delta)
    V_C = lr * X.T.dot(L1_delta)

    W = W + W_C
    V = V + V_C

