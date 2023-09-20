import MyNumPy as np
from Shapes.Shape import Shape
from Shapes.Intercept import Intercept


class Sphere(Shape):
    def __init__(self, position, radius, material):
        super().__init__(position, material)
        self.radius = radius

    def intersect(self, origin, direction):
        L = np.subtract(self.position, origin)
        lengthL = np.linalg_norm(L)
        tca = np.dot(L, direction)
        d = (lengthL ** 2 - tca ** 2) ** 0.5

        if d > self.radius:
            return None

        thc = (self.radius ** 2 - d ** 2) ** 0.5
        t0 = tca - thc
        t1 = tca + thc

        if t0 < 0:
            t0 = t1

        if t0 < 0:
            return None

        point = np.add(origin, np.multiplyVectorScalar(direction, t0))
        normal = np.subtract(point, self.position)
        normal = np.normalize(normal)

        return Intercept(distance=t0,
                         point=point,
                         normal=normal,
                         obj=self)
