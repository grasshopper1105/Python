import random

secret = random.randint(1, 10)

temp = input('猜我想的是什么？\n')
while not temp.isdecimal():
    print('press a number！')
    temp = input('猜我想的是什么？\n')

guess = int(temp)
time = 0
while time != 3:
    if guess > secret:
        print('大了大了！')
        print('不行啊!我想的数字不是' + temp + '哦')
        time = time + 1
        temp = input('猜我想的是什么？\n')
        guess = int(temp)
    elif guess < secret:
        print('小了宝贝~')
        print('我想的数字不是' + temp + '哦')
        time = time + 1
        temp = input('猜我想的是什么？\n')
        guess = int(temp)
    else:
        print('你猜对了！我想的就是' + temp)
        break
if time == 3:
    print('很遗憾，机会用完了~')
print('游戏结束😘')
