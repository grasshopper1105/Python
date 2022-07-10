a = [1, 3, 9, 2654, 45, 15, 12, 1, 5]
b = (1, 3, 9, 2654, 45, 15, 12, 1, 5)
c = '2654214564651'

A = str(a)
B = list(b)
C = tuple(c)
print(A, '\t', B, '\t', C)

D = sorted(a, reverse=True)
E = list(reversed(D))
F = max(a)
G = list(enumerate(a))  # 枚举法 （序号，数值）
H = list(zip(a, D, E))
print(D, '\t', E)
print(G)
print(F)
print(H)
