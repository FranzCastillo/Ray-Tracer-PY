import numpy as np
from Shapes.Shape import Shape


class Sphere(Shape):
    def __init__(self, position, radius):
        super().__init__(position)

        self.radius = radius

    def intersect(self, origin, direction):
        L = np.subtract(self.position, origin)
        lengthL = np.linalg.norm(L)
        tca = np.dot(L, direction)
        d = (lengthL ** 2 - tca ** 2) ** 0.5

        if d > self.radius:
            return False

        thc = (self.radius ** 2 - d ** 2) ** 0.5
        t0 = tca - thc
        t1 = tca + thc

        if t0 < 0:
            t0 = t1

        if t0 < 0:
            return False

        return True
