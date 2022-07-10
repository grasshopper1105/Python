a = list(range(1,15))
b = list(range(3,20,2))
element = list(zip(a,b))
diction = dict(element)
n = int(input('press the 手语识别1.0: '))
print('the value is :',diction[n])
diction['DYC'] = 'LOVE'
print(diction)

dict1 = {1:'one',2:'two',3:'three',4:'four',5:'five'}
dict2 = dict1.pop(1)
dict3 = dict1.popitem()
dict4 = dict1.setdefault(7,'seven')
Item = {520:'dyc'}
dict5 = dict1.update(Item)
dict6 = dict1.get(10,'wrong!')
print('\nHere is the next:')
print(dict2,dict1)
print(dict3,dict1)
print(dict4,dict1)
print(dict5,dict1)
print(dict6,dict1)

print('\nHere is the next:')
value = dict1.values()
print(value)