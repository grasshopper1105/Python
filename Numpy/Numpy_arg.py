import numpy as np

a = np.random.random(100)
np.random.shuffle(a)  # 将a中数据打乱 无返回值
p1 = np.argmax(a)  # a中最大值位置                                      ***argmin同理***
p2 = np.argsort(a)  # p2第一个元素表示a中最小值的位置，以此类推
p3 = np.argpartition(a, 0.5)  # 以0.5为分割，左边为小于0.5的数的位置（未排序）

temp = np.random.randint(1, 10, (3, 3))
s1 = np.sort(temp, axis=1)  # 沿着列的方向，按照行排序
s2 = np.sort(temp, axis=0)  # 沿着行的方向，按照列排序
s3 = np.partition(a, 0.5)  # 以0.5为分割，左边为小于0.5的数,右边为大于0.5的（未排序）
