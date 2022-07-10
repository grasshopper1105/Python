import numpy as np

a = np.arange(1, 10).reshape(3, 3)
A = np.arange(1, 11).reshape(2, 5)
b = np.full((3, 3), 5)
B = np.arange(1, 5).reshape(2, 2)
c = a * b  # a和b对应元素相乘
d = a.dot(b)  # a和b作矩阵乘法
e = a.T  # a的转置
f = np.linalg.inv(B)  # 求a的逆矩阵
F = np.linalg.pinv(A)  # 求A的伪逆矩阵（A*F=E，F不能*A）

x = np.arange(3)
f = x + a  # x与a中每一行相加     *** x * a 同理***
X = np.tile(x, [3, 1])  # x在行上堆叠三次，列上堆叠一次

SUM1 = np.sum(a)  # 求和  ***np.max np.min 同理***
SUM2 = np.sum(a, axis=0)  # 沿着行计算 = 只保留列
SUM3 = np.sum(a, axis=1)  # 沿着列计算 = 只保留行

P1 = np.prod(a)  # a中元素相乘
P2 = np.mean(a)  # a中元素平均值
P3 = np.median(a)  # a中元素的中位数
P4 = np.var(a)  # 求方差
P5 = np.std(a)  # 标准差

temp = np.percentile(a, q=50)  # 找出位于矩阵中值处在50%的数

for percent in [0, 25, 50, 75, 100]:
    print(np.percentile(a, q=percent))  # 分别打印值出位于矩阵 最小 25% 50% 75% 最大 的数
