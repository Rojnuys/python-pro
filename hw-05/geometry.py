class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle():
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("The radius must be positive")
        self._radius = value

    def contains(self, point):
        return (point.x - self.x) ** 2 + (point.y - self.y) ** 2 <= self.radius ** 2
