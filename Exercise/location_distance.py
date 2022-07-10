def distance(location):
    goal = list(map(lambda x: (x[0] ** 2 + x[1] ** 2) ** (0.5), location))
    return goal


x = [1, 3, 6, 5, 8, 7, 44, 2, 3]
y = [52, 3, 6, 2, 2, 1, 4, 5, 6]
location = list(zip(x, y))
D = distance(location)
print(D)
