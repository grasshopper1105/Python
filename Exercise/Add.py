a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = [1, 2, 3, 4, 5]
d = []
e = [1]
f = [1, 2]
g = 1

print(a)
a.append(f)  # 将f作为一个元素添加到a
print(a)
b.extend(f)  # 将f的元素添加到b后面
print(b)
c.insert(0, f)  # 将f作为一个元素插入位置x
print(c)
c.insert(0, True)
print(c)
c.insert(0, 'True')
print(c)
