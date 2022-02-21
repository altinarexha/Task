class Angle:

    def __init__(self, value):
        self.value = value % 360

    def __str__(self):
        return '{} degrees'.format(self.value)

    def __add__(self, other):
        return Angle(self.value + other.value)

    def __sub__(self, other):
        return Angle(self.value - other.value)

    def __mul__(self, other):
        return Angle(self.value * other)

    def __eq__(self, other):
        return self.value == other.value

    def __ge__(self, other):
        return self.value <= other.value

    def __le__(self, other):
        return self.value >= other.value

add = Angle(270) + Angle(270)
sub = Angle(90) - Angle(180)
mul = Angle(30) * 3
print(add)
print(sub)
print(mul)