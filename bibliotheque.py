from collections import namedtuple

Point2D = namedtuple("Point2D", "x, y")
Point3D = namedtuple("Point3D", "x y z")

def ajout_point1d(point1, point2):
  x = point1.x + point2.x
  return Point1D(x)

def norme1d(p1):
    return (p1.x ** 2) ** 0.5 

#def ajout_point2d(p_1, p_2):
    coord = tuple(x + y for x, y in zip(p_1, p_2))
    return Point2D._make(coord)

def ajout_point2d(p_1, p_2):
    xfinal = p_1.x + p_2.x
    yfinal = p_1.y + p_2.y
    return Point2D._make(xfinal, yfinal)

def ajout_point3d(p_1, p_2):
    return Point3D._make((p1 + p2 for p1, p2 in zip(p_1, p_2) ))


class Point1D:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f"Point: {self.x}"









