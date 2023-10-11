import MyNumPy as np
from Shapes.Shape import Shape
from Shapes.Intercept import Intercept
from math import sqrt

# https://chat.openai.com/share/7178c177-45e5-445e-a119-e88abcb2e2f4
class Cylinder(Shape):
    def __init__(self, position, radius, height, material):
        super().__init__(position, material)
        self.radius = radius
        self.height = height

    def intersect(self, origin, direction):
        L = np.subtract(origin, self.position)
        a = direction[0] * direction[0] + direction[2] * direction[2]
        b = 2 * (L[0] * direction[0] + L[2] * direction[2])
        c = L[0] * L[0] + L[2] * L[2] - self.radius * self.radius

        discriminant = b * b - 4 * a * c

        if discriminant < 0:
            return None

        t1 = (-b - sqrt(discriminant)) / (2 * a)
        t2 = (-b + sqrt(discriminant)) / (2 * a)

        if t1 > t2:
            t1, t2 = t2, t1

        y1 = L[1] + t1 * direction[1]
        y2 = L[1] + t2 * direction[1]

        if (y1 < 0 and y2 < 0) or (y1 > self.height and y2 > self.height):
            return None

        t = t1 if 0 <= y1 <= self.height else t2
        point = np.add(origin, np.multiplyVectorScalar(direction, t))

        if 0 <= y1 <= self.height:
            normal = np.normalize(np.subtract(point, np.add(self.position, (0, 0, 0))))
        else:
            normal = np.normalize(np.subtract(point, np.add(self.position, (0, self.height, 0))))

        return Intercept(distance=t, point=point, normal=normal, obj=self, textureCoordinates=None)

    def normal(self, point):
        if point[1] <= 0:
            return np.normalize(np.subtract(point, np.add(self.position, (0, 0, 0))))
        elif point[1] >= self.height:
            return np.normalize(np.subtract(point, np.add(self.position, (0, self.height, 0))))
        else:
            return np.normalize(np.subtract(point, np.add(self.position, (0, point[1], 0))))
