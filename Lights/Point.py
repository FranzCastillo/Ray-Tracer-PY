import Lights.Light as Light
import numpy as np

from Lights.Directional import reflect


class Point(Light.Light):
    def __init__(self, position=(0, 0, 0), intensity=1, color=(1, 1, 1)):
        super().__init__(intensity, color, "POINT")
        self.position = position

    def getDiffuseColor(self, intercept):
        direction = np.subtract(self.position, intercept.point)
        radius = np.linalg.norm(direction)
        direction = direction / radius

        intensity = np.dot(intercept.normal, direction) * self.intensity
        intensity *= 1 - intercept.obj.material.ks

        if radius != 0:
            intensity /= radius ** 2
        intensity = max(0, min(1, intensity))

        return [i * intensity for i in self.color]

    def getSpecularColor(self, intercept, viewPosition):
        direction = np.subtract(self.position, intercept.point)
        radius = np.linalg.norm(direction)
        direction = direction / radius

        reflectDirection = reflect(intercept.normal, direction)

        viewDirection = np.subtract(viewPosition, intercept.point)
        viewDirection = viewDirection / np.linalg.norm(viewDirection)

        intensity = max(0, min(1, np.dot(reflectDirection, viewDirection))) ** intercept.obj.material.spec
        intensity *= self.intensity
        intensity *= intercept.obj.material.ks

        if radius != 0:
            intensity /= radius ** 2
        intensity = max(0, min(1, intensity))

        return [i * intensity for i in self.color]
