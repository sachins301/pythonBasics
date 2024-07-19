# Week 9 00P Properties

class Numbers:

    MULTIPLIER = 0

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def add(self):
        return self._x + self._y

    def multiply(self, a):
        return self.MULTIPLIER * a

    @property
    def values(self):
        return self._x, self._y

    @values.setter
    def values(self, xy_tuple):
        self._x, self._y = xy_tuple

    @values.deleter
    def values(self):
        del self._x
        del self._y


num = Numbers(4,5)
num.MULTIPLIER = 2
val = num.values
print(num.values)
# accessing the setter
num.values = (6, 7)
# accessing the getter
print(num.values)
