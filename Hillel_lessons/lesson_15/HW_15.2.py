class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        if isinstance(other, Fraction):
            numerator = self.numerator * other.denominator + other.numerator * self.denominator
            return Fraction(numerator, self.denominator * other.denominator)
        elif isinstance(other, (int, float)):
            numerator = self.numerator + (other * self.denominator)
            return Fraction(numerator, self.denominator)
        return NotImplemented

    def __iadd__(self, other):
        return Fraction.__add__(self, other)

    def __radd__(self, other):
        return Fraction.__add__(self, other)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        elif isinstance(other, (int, float)):
            return Fraction(self.numerator * other, self.denominator)
        return NotImplemented

    def __imul__(self, other):
        return Fraction.__mul__(self, other)

    def __rmul__(self, other):
        return Fraction.__mul__(self, other)

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        elif isinstance(other, (int, float)):
            return Fraction(self.numerator, self.denominator * other)
        return NotImplemented

    def __itruediv__(self, other):
        return Fraction.__truediv__(self, other)

    def __rtruediv__(self, other):
        return Fraction.__truediv__(self, other)

    def __sub__(self, other):
        if isinstance(other, Fraction):
            numerator = self.numerator * other.denominator - other.numerator * self.denominator
            return Fraction(numerator, self.denominator * other.denominator)
        elif isinstance(other, (int, float)):
            numerator = self.numerator - (other * self.denominator)
            return Fraction(numerator, self.denominator)
        return NotImplemented

    def __isub__(self, other):
        return Fraction.__sub__(self, other)

    def __rsub__(self, other):
        return Fraction.__sub__(self, other)

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator == other.numerator * self.denominator
        elif isinstance(other, (int, float)):
            return self.numerator / self.denominator == other
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator > other.numerator * self.denominator
        elif isinstance(other, (int, float)):
            return self.numerator / self.denominator > other
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator < other.numerator * self.denominator
        elif isinstance(other, (int, float)):
            return self.numerator / self.denominator < other
        return NotImplemented

    def __str__(self):
        return f"Fraction: {self.numerator}, {self.denominator}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
