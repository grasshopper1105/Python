temp = range(15)
odd = list(filter(lambda x: x % 2, temp))
result = list(map(lambda x: x ** 0.5, temp))


def floating(x):
    a = '%.2f' % x
    for _ in a:
        res = float(a)
    return res


result2 = list(map(floating, result))

print(odd)
print(result2)
