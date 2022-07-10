a = (1, 2, 3, 4, 5, 6, 1)
b = a[:3]
c = a[3:]
d = ('手语识别1.0',)
e = '手语识别1.0',
f = ()

A = 'GrassHoppeR'
print(a)
print(b + d + c)
print(b + e + c)
print(b + f + c)

g = a.count(1)  # 记录（）内值的出现次数
print('time is :', g)

B = A.capitalize()  # 首字母大写
C = A.upper()  # 全大写
D = A.lower()  # 全小写
E = A.center(40, '~')  # 居中
F = A.swapcase()  # 大小写互换
print(B, '\t', C, '\t', D, '\t', F, '\n', E)
