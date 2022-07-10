a = [1, 2, 3, 56, 9, 8, 45, 2, 1, 3]
b = a.index(3)  # 索引第一个3出现的位置
print('the position is :', b)
print('the number is :', a[b])

for i in range(0, 10):
    c = a[b] + a[i]
    print(i, ':', c)

a.remove(1)  # 删掉第一个出现的 1
print('now the list is :', a)
del a[2]  # 删掉第3个数
print('now the list is :', a)
name1 = a.pop()  # 默认去掉最后一个数
print('now the list is :', a, '\tnumeber is :', name1)
name2 = a.pop(4)  # 去掉第五个数
print('now the list is :', a, '\tnumeber is :', name2)
