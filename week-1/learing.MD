#### What is Machine Learning?
Two definitions of Machine Learning are offered. Arthur Samuel described it as: "the field of study that gives computers the ability to learn without being explicitly programmed." This is an older, informal definition.

Tom Mitchell provides a more modern definition: "A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E."

##### Example: playing checkers.
- E = the experience of playing many games of checkers
（训练经验）

- T = the task of playing checkers.
（任务）

- P = the probability that the program will win the next game.（预测正确的概率）

> In general, any machine learning problem can be assigned to one of two broad classifications:
Supervised learning and Unsupervised learning.

#### Supervised Learning

In supervised learning, we are given a data set and already know what our correct output should look like, having the idea that there is a relationship between the input and the output.

Supervised learning problems are categorized into "regression" and "classification" problems. In a regression problem, we are trying to predict results within a continuous output, meaning that we are trying to map input variables to some continuous function. In a classification problem, we are instead trying to predict results in a discrete output. In other words, we are trying to map input variables into discrete categories.

##### Example 1:

- Given data about the size of houses on the real estate market, try to predict their price. Price as a function of size is a continuous output, so this is a regression problem.

- We could turn this example into a classification problem by instead making our output about whether the house "sells for more or less than the asking price." Here we are classifying the houses based on price into two discrete categories.

##### Example 2:

- (a) Regression - Given a picture of a person, we have to predict their age on the basis of the given picture
- (b) Classification - Given a patient with a tumor, we have to predict whether the tumor is malignant or benign.


#### Unsupervised Learning
Unsupervised learning allows us to approach problems with little or no idea what our results should look like. We can derive structure from data where we don't necessarily know the effect of the variables.
We can derive this structure by clustering the data based on relationships among the variables in the data.
With unsupervised learning there is no feedback based on the prediction results.

##### Example:

- Clustering: Take a collection of 1,000,000 different genes, and find a way to automatically group these genes into groups that are somehow similar or related by different variables, such as lifespan, location, roles, and so on.

- Non-clustering: The "Cocktail Party Algorithm", allows you to find structure in a chaotic environment. (i.e. identifying individual voices and music from a mesh of sounds at a cocktail party).

#### The difference between the two
> F(x)->y,x(A),y(b),

##### 我们不难看到，回归问题与分类问题本质上都是要建立映射关系：
1. 而两者的区别则在于：对于回归问题，其输出空间B是一个度量空间，即所谓“定量”。也就是说，回归问题的输出空间定义了一个度量  去衡量输出值与真实值之间的“误差大小”。例如：预测一瓶700毫升的可乐的价格（真实价格为5元）为6元时，误差为1；预测其为7元时，误差为2。这两个预测结果是不一样的，是有度量定义来衡量这种“不一样”的。（于是有了均方误差这类误差函数）。
2. 对于分类问题，其输出空间B不是度量空间，即所谓“定性”。也就是说，在分类问题中，只有分类“正确”与“错误”之分，至于错误时是将Class 5分到Class 6,还是Class 7，并没有区别，都是在error counter上+1。而非很多回答所提到的“连续即回归，离散即分类”。事实上，在实际操作中，我们确实常常将回归问题和分类问题互相转化（分类问题回归化：逻辑回归；回归问题分类化：年龄预测问题——>年龄段分类问题），但这都是为了处理实际问题时的方便之举，背后损失的是数学上的严谨性。


