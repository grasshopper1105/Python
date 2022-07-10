dict1 = {}
dict2 = dict1.fromkeys(range(1,10,2),'*')

for keys in dict2.keys():
    print(keys)

for values in dict2.values():
    print(values)

for items in dict2.items():
    print(items)