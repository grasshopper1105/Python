import numpy as np

x = np.zeros((2, 3), dtype=int)
y = np.ones(10)
z = np.full((2, 4), 520)
a = np.arange(0, 2, 0.4)  # 最后一项为步长
b = np.linspace(2, 20, 10)  # 最后一项为数据个数
c = np.random.randint(0, 11, (3, 3))  # 生成随机整数
d = np.random.random((3, 3))  # 生成0-1的随机数
e = np.random.normal(3, 3, size=(3, 3))  # 生成0-1之间满足正态分布的数（均值为0，方差为1） normal(均值，方差 ,size)
f = np.arange(18).reshape(3, 6)  # 重新修改矩阵规格
F = f.reshape(9, -1)  # 只需要10行，列数由系统分配，则将列数写成 -1
g = x[1, 2]  # 访问第二行，第二列，起始为x[0,0]
h = f[:2, :3]  # 取f的前两行和前三列作为一个矩阵
i = f[::-1, ::-1]  # 反转整个矩阵 -1表示步长，从最右边往左取
k = F.reshape(1, 18)  # 此时是二维数组!!

# 切片后的子矩阵数据改变，相应的原矩阵的值也会改变；同理原矩阵改变，子矩阵也会改变
j = d[:, :].copy()  # 此时子矩阵与原矩阵互不影响

np.random.seed(100)  # 写此行后随机数不变
print()
