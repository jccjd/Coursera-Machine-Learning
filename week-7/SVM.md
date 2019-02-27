### SVM
最早是由 Vladimir N.Vapnik 和 Alexey Ya. Chervonenkis 在1963年提出

目前的版本（soft margin)是由Corinna Cortes 和 VaPnik 在1993年提出，并在1995年发表

深度学习（2012）出现之前，svm被认为机器学习中近十几年来最成功，表现最好的算法

![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-7/image/SVM1.PNG?raw=true)

svm寻找区分两类的超平面（hyper plane)使边际（margin）最大

![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-7/image/SVM1.PNG?raw=true)


### 向量内积

x = {x1,x2,x3....xn}

y = {y1,y2,y3....yn}

向量内积：

![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-7/image/向量内积1.PNG?raw=true)


![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-7/image/向量内积2.PNG?raw=true)

几何表示：

![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-7/image/向量内积5.PNG?raw=true)


范数：

![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-7/image/向量内积3.PNG?raw=true)

当||x|| =/ 0 ，||y||=/0 时，可以求余弦相似度：

![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-7/image/向量内积4.PNG?raw=true)


### 线性不可分的情况

![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-7/image/线性不可分1.PNG?raw=true)

如果出现这种情况发生线性不可分需要进行改进，松弛变量与惩罚函数
    
    yi(wi*xi + b) >1 -εi,εi>0
    约束条件没有体现错误分类的点要尽量究竟分类边界
    
    min(||w||^2 / 2) + C * sum(εi)
    使得分错的点越少越好，距离分类边界越近越好
线性不可分情况下的对偶问题

![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-7/image/线性不可分1.PNG?raw=true)

> s.t.,C>аi>0, i =1,
### SVM低维映射

![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-7/image/SVM4.PNG?raw=true)

非线性情况把低维空间的非线性问题映射到高维空间，变成求解线性问题

![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-7/image/SVM5.PNG?raw=true)

演示：
https://v.qq.com/x/page/k05170ntgzc.html

















