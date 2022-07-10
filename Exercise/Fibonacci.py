def Fibonacci(n):
    if n < 0:
        return -1
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


goal = int(input('press a number :\t'))
sum = Fibonacci(goal)
if sum != -1:
    print('the result is %d' % sum)
else:
    print('Wrong!')
