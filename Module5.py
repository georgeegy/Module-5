class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2}, {3})".format(self.x, self.y, self.width, self.height)

    def shift(self, dx, dy):
        self.x += dx
        self.y += dy

    def offset(self, dx, dy):
        return self.x + dx, self.y + dy, self.width, self.height


r1 = Rectangle(10, 20, 30, 40)

print(str(r1))

r1.shift(-10, -20)

print(str(r1))

r2 = r1.offset(100, 100)

print(r1)
print(r2)
