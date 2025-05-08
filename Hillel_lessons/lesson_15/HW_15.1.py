#Arten Guguyev
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, (int,float)):
            return self.get_square() == other
        elif isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Rectangle):
            res_square = self.get_square() + other.get_square()
            return Rectangle(2, round(res_square / 2, 1))
        elif isinstance(other, (float, int)):
            res_square = self.get_square() + other
            return Rectangle(2, round(res_square / 2, 1))
        return NotImplemented


    def __iadd__(self, other):
        return Rectangle.__add__(self, other)

    def __radd__(self, other):
        return Rectangle.__add__(self, other)

    def __mul__(self, n):
        res_square = self.get_square() * n
        return Rectangle(n, self.get_square())

    def __imul__(self, other):
        return Rectangle.__mul__(self, other)

    def __rmul__(self, other):
        return Rectangle.__mul__(self, other)

    def __str__(self):
        return f'Rectangle with side {self.width}, {self.height} and square = {self.get_square()}'


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
