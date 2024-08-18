from shapes import Point, Rectangle, Circle, Parallelogram, Triangle, Scene

r = Rectangle(0, 0, 10, 20)
r1 = Rectangle(10, 0, -10, 20)
r2 = Rectangle(0, 20, 100, 20)

c = Circle(10, 0, 10)
c1 = Circle(100, 100, 5)

p = Parallelogram(1, 2, 18, 23, 38)
p.x
p1 = Parallelogram(1, 2, 20, 30, 45)
str(p1)

t = Triangle(20, 5, 10, 20, 27)
t1 = Triangle(0, 8, 12, 6, 8)
t2 = Triangle(100, 45, 30, 13, 26)

scene = Scene()
scene.add_figure(r)
scene.add_figure(r1)
scene.add_figure(r2)
scene.add_figure(c)
scene.add_figure(c1)
scene.add_figure(t)
scene.add_figure(t1)
scene.add_figure(t2)

print(f"Scene's total square: {scene.total_square()}")

circle = Circle(10, -5, 20)
print(f"Circle(10, -5, 20): Point(15, -15) - {Point(15, -15) in circle}; Point(31, -5): {Point(31, -5) in circle}")