import numpy as np

a = np.array(range(9)).reshape(3, 3)
b = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
c = np.concatenate([a, b])  # 将两个3*3矩阵拼接成6*3矩阵
d = np.concatenate([a, b], axis=1)  # 将两个3*3矩阵拼接成3*6矩阵
A = np.array([1, 2, 3, 4, 5])
B = np.array([5, 4, 3, 2, 1])
C = np.concatenate([A, B])  # 将两个矩阵接在一起
D, E = np.split(C, [6])  # 按照第6个位置将矩阵分为两个矩阵，第六个数在左边矩阵

temp1 = np.array([6, 6, 6])
temp2 = np.full((3, 1), 100)
X = np.concatenate([temp1.reshape(1, -1), b])  # X,Y结果相同，Y可将不同维度结合，X是将temp转化维度    ***此处split同理***
Y1 = np.vstack([temp1, b])  # 在竖直方向智能堆叠
Z1 = np.hstack([temp2, b])  # 在水平方向智能堆叠
Y2, Y3 = np.vsplit(c, [2])  # 在竖直方向以第二行为分割点智能分割
Z2, Z3, Z4 = np.hsplit(d, [1, 4])  # 在水平方向以第一行和第四行智能分割

print(d)
print(Z2)
print(Z3)
