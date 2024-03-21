import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def __str__(self):
    """
    this will be called
    :param self:
    :return:
    """
    return f"a=({self.x}, {self.y})"

a = Point(2, 3)
b = Point(7, 9)


print(f"a=({a.x}, {a.y})")
print(f"b=({b.x}, {b.y})")

#creating list of random 5 points
points = [] #initialize empty list
for _ in range(5):
   # x = random.randint(-100, 100)
    #y = random.randint(-100, 100)
    #random_point = Point(x, y)
    #points.append(random_point)

    #or in a single line like this
    points.append(Point(random.randint(-100, 100),
                        random.randint(-100, 100)))

for point in points:
    print(f"p=({point.x}, {point.y})")

    #try print the first point
print(points[0])