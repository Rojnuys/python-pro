import math


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return 0


class Point(Shape):
    pass


class Circle(Shape):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2

    def __contains__(self, other):
        if not isinstance(other, Point):
            raise ValueError("This operation is available only for Point")
        return (other.x - self.x) ** 2 + (other.y - self.y) ** 2 <= self.radius ** 2


class Rectangle(Shape):

    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def square(self):
        return self.width * self.height


class Parallelogram(Rectangle):

    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width)
        self.angle = angle

    def square(self):
        return self.height * math.sin(math.radians(self.angle)) * self.width

    def print_angle(self):
        print(self.angle)

    def __str__(self):
        result = super().__str__()
        return result + f'\nParallelogram: {self.width}, {self.height}, {self.angle}'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Triangle(Shape):

    def __init__(self, x, y, a, b, c):
        super().__init__(x, y)
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("The sum of the length of the two sides of a triangle must be greater than the length of "
                             "the third side.")
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def semi_perimeter(self):
        return self.perimeter() / 2

    def square(self):
        return math.sqrt(
            self.semi_perimeter() *
            (self.semi_perimeter() - self.a) *
            (self.semi_perimeter() - self.b) *
            (self.semi_perimeter() - self.c)
        )


class Scene:
    def __init__(self):
        self._figures = []

    def add_figure(self, figure):
        self._figures.append(figure)

    def total_square(self):
        return sum(f.square() for f in self._figures)

    def __str__(self):
        pass
