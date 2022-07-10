a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = a[1:5]
c = slice(5)
d = slice(1, 4)
e = slice(0, 5, 2)
print(b, '\t', c, '\t', a[c], '\t', a[d], '\t', a, '\t', a[e])

b = a[:]
c = a
d = a[slice(8)]
print(b, '\t', c, '\t', d)
a.sort(reverse=1)
print(b, '\t', c, '\t', d)
