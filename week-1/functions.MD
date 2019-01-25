#### Model Representation 

To describe the supervised learning problem slightly more formally, our goal is, given a training set, to learn a function h : X → Y so that h(x) is a “good” predictor for the corresponding value of y. For historical reasons, this function h is called a hypothesis. Seen pictorially, the process is therefore like this:


在给定训练集的情况下，学习函数h：X——>Y,使得h(x) 是y的相应值的好预测器。由于历史原因，这个函数h被称为假设。从图中可以看出这个过程是这样的：

 ![image](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/H6qTdZmYEeaagxL7xdFKxA_2f0f671110e8f7446bb2b5b2f75a8874_Screenshot-2016-10-23-20.14.58.png?expiry=1548288000000&hmac=1u_L5kz-i97I8jflA1_IXeDEEqDqPGStKp5XQPkBJVY)

> 图中输入住房面积x，经函数h，输出房子的估价y

#### Cost function （代价函数）
我们可以使用成本函数来衡量我们的假设函数的准确性。 这需要假设的所有结果与来自x和实际输出y的输入的平均差异（实际上是平均值的更高版本，即使平方差公式）

 ![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-1/tu/costfunction.PNG?raw=true)
 
 代价函数是线性回归中的一个应用，在线性回归中，要解决的一个问题就是最小化问题，
 假设直线方程 如何使得函数更加拟合于训练集
 那么就需要costFunction来找到最小误差的方程
 > hθ(X) = 1(θ0) + x(θ1)
 ![image](https://camo.githubusercontent.com/32d1402d812f48fa3a9078f8acec0fa1e41c6396/68747470733a2f2f696d672e68616c66726f73742e636f6d2f426c6f672f41727469636c65496d6167652f36385f305f312e706e67)
#### Gradient Descent(梯度下降)
梯度下降的主要思想：
1. 初始化θ0和θ1，θ0 = 0，θ1 = 0;
2. 不断的改变θ0和θ1的值 ，不断减少f（θ0，θ1）直到最小值或局部最小
![image](https://camo.githubusercontent.com/d39774347bf60dbac8f776d61207031f9e8bc7bd/68747470733a2f2f696d672e68616c66726f73742e636f6d2f426c6f672f41727469636c65496d6167652f36385f315f302e706e67)
 


