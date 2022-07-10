def Hanoi(n, x, y, z):
    if n == 1:
        print(x, '-->', z)
    else:
        Hanoi(n - 1, x, z, y)
        print(x, '-->', z)
        Hanoi(n - 1, y, x, z)


num = int(input('press the layer:'))
Hanoi(num, 'X', 'Y', 'Z')
