class Calc:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self):
        self.sum = self.x + self.y
        return self.sum

    def mult(self):
        self.mult = self.x * self.y
        return self.mult


a = Calc(5, 10)
print(a.mult())
print(a.sum())
