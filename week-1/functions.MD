#### Model Representation 

To describe the supervised learning problem slightly more formally, our goal is, given a training set, to learn a function h : X → Y so that h(x) is a “good” predictor for the corresponding value of y. For historical reasons, this function h is called a hypothesis. Seen pictorially, the process is therefore like this:


在给定训练集的情况下，学习函数h：X——>Y,使得h(x) 是y的相应值的好预测器。由于历史原因，这个函数h被称为假设。从图中可以看出这个过程是这样的：

 ![image](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/H6qTdZmYEeaagxL7xdFKxA_2f0f671110e8f7446bb2b5b2f75a8874_Screenshot-2016-10-23-20.14.58.png?expiry=1548288000000&hmac=1u_L5kz-i97I8jflA1_IXeDEEqDqPGStKp5XQPkBJVY)

> 图中输入住房面积x，经函数h，输出房子的估价y

#### Cost function （代价函数）
我们可以使用成本函数来衡量我们的假设函数的准确性。 这需要假设的所有结果与来自x和实际输出y的输入的平均差异（实际上是平均值的更高版本，即使平方差公式）
$$a + b$$

