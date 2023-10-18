import MyNumPy as np
from Shapes.Shape import Shape
from Shapes.Intercept import Intercept
from math import sqrt, cos, sin

class Cylinder(Shape):
    def __init__(self, position, radius, height, material, rotation_z=0.0):
        super().__init__(position, material)
        self.radius = radius
        self.height = height
        self.rotation_z = rotation_z  # Angle in radians

    # https://chat.openai.com/share/7178c177-45e5-445e-a119-e88abcb2e2f4
    # https://chat.openai.com/share/13c0a1b8-40fb-4510-bd97-0fff68617fc5
    def intersect(self, origin, direction):
        cos_theta = cos(-self.rotation_z)
        sin_theta = sin(-self.rotation_z)
        rotated_origin = np.add(
            np.multiplyVectorScalar(origin, cos_theta),
            np.multiplyVectorScalar(np.cross((0, 0, 1), origin), sin_theta)
        )
        rotated_direction = np.add(
            np.multiplyVectorScalar(direction, cos_theta),
            np.multiplyVectorScalar(np.cross((0, 0, 1), direction), sin_theta)
        )

        L = np.subtract(rotated_origin, self.position)
        a = rotated_direction[0] * rotated_direction[0] + rotated_direction[2] * rotated_direction[2]
        b = 2 * (L[0] * rotated_direction[0] + L[2] * rotated_direction[2])
        c = L[0] * L[0] + L[2] * L[2] - self.radius * self.radius

        discriminant = b * b - 4 * a * c

        if discriminant < 0:
            return None

        t1 = (-b - sqrt(discriminant)) / (2 * a)
        t2 = (-b + sqrt(discriminant)) / (2 * a)

        if t1 > t2:
            t1, t2 = t2, t1

        y1 = L[1] + t1 * rotated_direction[1]
        y2 = L[1] + t2 * rotated_direction[1]

        if (y1 < 0 and y2 < 0) or (y1 > self.height and y2 > self.height):
            return None

        t = t1 if 0 <= y1 <= self.height else t2
        point = np.add(rotated_origin, np.multiplyVectorScalar(rotated_direction, t))

        if 0 <= y1 <= self.height:
            normal = np.normalize(np.subtract(point, np.add(self.position, (0, 0, 0))))
        else:
            normal = np.normalize(np.subtract(point, np.add(self.position, (0, self.height, 0))))

        # Apply the rotation around the z-axis to the normal vector
        rotated_normal = np.add(
            np.multiplyVectorScalar(normal, cos_theta),
            np.multiplyVectorScalar(np.cross((0, 0, 1), normal), -sin_theta)
        )

        return Intercept(distance=t, point=point, normal=rotated_normal, obj=self, textureCoordinates=None)

    def normal(self, point):
        if point[1] <= 0:
            return np.normalize(np.subtract(point, np.add(self.position, (0, 0, 0))))
        elif point[1] >= self.height:
            return np.normalize(np.subtract(point, np.add(self.position, (0, self.height, 0))))
        else:
            return np.normalize(np.subtract(point, np.add(self.position, (0, point[1], 0))))
