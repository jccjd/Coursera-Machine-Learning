import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn import preprocessing
from sklearn.preprocessing import PolynomialFeatures


scale = False

data = np.genfromtxt('data2.txt',delimiter=',')

x_data = data[:,:-1]
y_data = data[:,-1,np.newaxis]
def plot():
    x0 = []
    x1 = []
    y0 = []
    y1 = []
    for i in range(len(x_data)):
        if y_data[i] ==0:
            x0.append(x_data[i,0])
            y0.append(x_data[i,1])
        else:
            x1.append(x_data[i,0])
            y1.append(x_data[i,1])
        scatter0 = plt.scatter(x0,y0,c = 'b',marker='o')
        scatter1 = plt.scatter(x1,y1,c = 'r',marker='x')
        plt.legend(handles=[scatter0,scatter1],labels=['label0','label1'],loc = 'best')

plot()
# plt.show()
#定义多项式回归，degree的值可以调节多项式的特征
poly_reg = PolynomialFeatures(degree=3)
x_poly = poly_reg.fit_transform(x_data)

def sigmoid(x):
    return 1.0/(1+np.exp(-x))
def cost(xMat,yMat,ws):
    left = np.multiply(yMat,np.log(sigmoid(xMat * ws)))
    right = np.multiply(1 - yMat,np.log(1 - sigmoid(xMat * ws)))
    return np.sum(left + right) / -(len(xMat))
def gradAscent(xArr,yArr):

    if scale == True:
        xArr = preprocessing.scale(xArr)
    xMat = np.mat(xArr)
    yMat = np.mat(yArr)
    ls = 0.03
    epochs = 50000
    costList = []
    #计算数据列数，有几个列就有几个权值
    m,n = np.shape(xMat)
    ws = np.mat(np.ones((n,1)))

    for i in range(epochs + 1):
         h = sigmoid(xMat * ws)
         #计算误差
         ws_grad = xMat.T*(h - yMat)/m
         ws = ws - ls * ws_grad

         if i%50 == 0:
             costList.append(cost(xMat,yMat,ws))

    return ws,costList

ws,cosList = gradAscent(x_poly,y_data)
# print(ws)

