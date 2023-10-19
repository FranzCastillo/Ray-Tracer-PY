import MyNumPy as np
from Shapes.Shape import Shape
from Shapes.Intercept import Intercept


class Pyramid(Shape):
    def __init__(self, position, base, height, material):
        super().__init__(position, material)
        self.base = base
        self.height = height

    def intersect(self, origin, direction):
        # Calculate the vertices of the pyramid
        half_base = self.base / 2
        vertices = [np.add(self.position, [half_base, 0, half_base]),
                    np.add(self.position, [-half_base, 0, half_base]),
                    np.add(self.position, [-half_base, 0, -half_base]),
                    np.add(self.position, [half_base, 0, -half_base]),
                    np.add(self.position, [0, self.height, 0])]

        # Check intersection with each face of the pyramid
        faces = [[vertices[0], vertices[1], vertices[4]],
                 [vertices[1], vertices[2], vertices[4]],
                 [vertices[2], vertices[3], vertices[4]],
                 [vertices[3], vertices[0], vertices[4]],
                 [vertices[0], vertices[1], vertices[2], vertices[3]]]

        closest_intercept = None

        for face in faces:
            # Calculate normal of the face
            normal = np.cross(np.subtract(face[1], face[0]), np.subtract(face[2], face[0]))
            normal = np.normalize(normal)

            # Calculate intersection with the plane of the face
            denominator = np.dot(direction, normal)

            if abs(denominator) > 0.0001:
                t = np.dot(np.subtract(face[0], origin), normal) / denominator

                if t >= 0:
                    point = np.add(origin, np.multiplyVectorScalar(direction, t))

                    # Check if the point is inside the face
                    inside = True

                    for i in range(len(face)):
                        edge = np.subtract(face[(i + 1) % len(face)], face[i])
                        point_to_vertex = np.subtract(point, face[i])
                        if np.dot(normal, np.cross(edge, point_to_vertex)) < 0:
                            inside = False
                            break

                    if inside and (closest_intercept is None or t < closest_intercept.distance):
                        closest_intercept = Intercept(distance=t,
                                                      point=point,
                                                      normal=normal,
                                                      obj=self,
                                                      textureCoordinates=None)

        return closest_intercept

    def normal(self, point):
        # Calculate the vertices of the pyramid
        half_base = self.base / 2
        vertices = [np.add(self.position, [half_base, 0, half_base]),
                    np.add(self.position, [-half_base, 0, half_base]),
                    np.add(self.position, [-half_base, 0, -half_base]),
                    np.add(self.position, [half_base, 0, -half_base]),
                    np.add(self.position, [0, self.height, 0])]

        # Check which face the point is on and return the normal of that face
        faces = [[vertices[0], vertices[1], vertices[4]],
                 [vertices[1], vertices[2], vertices[4]],
                 [vertices[2], vertices[3], vertices[4]],
                 [vertices[3], vertices[0], vertices[4]],
                 [vertices[0], vertices[1], vertices[2], vertices[3]]]

        for face in faces:
            normal = np.cross(np.subtract(face[1], face[0]), np.subtract(face[2], face[0]))
            normal = np.normalize(normal)

            if abs(np.dot(np.subtract(point, face[0]), normal)) <= 0.0001:
                return normal

        return None
