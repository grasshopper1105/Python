import numpy as np

temp = np.random.randint(1, 16, (4, 4))
x = [0, 1, 2]
y = [1, 2, 0]
Y = [True, True, False, True]
b = temp[x, y]  # 返回 （0,1）（1,2）（2,0）三个点的值
B = temp[1:3, Y]  # 返回第一行和第二行中除去第三列的元素

temp2 = np.random.randint(0, 2, 10)
p1 = np.count_nonzero(temp2)  # 返回数组中不为0的数的个数
p2 = np.any((temp2 == 0) & (temp2 > 1))  # 只要有一个为0且其大于1就为 True     *** | 或运算   ~ 非运算 同理 ***
p2 = np.all(temp2 == 0)  # 只有全为0才为 True
