import Lights.Light as Light
import numpy as np


def reflect(normal, direction):
    reflectValue = (2 * np.dot(normal, direction) * normal - direction)
    return reflectValue / np.linalg.norm(reflectValue)


class Directional(Light.Light):
    def __init__(self, direction=(0, 1, 0), intensity=1, color=(1, 1, 1)):
        super().__init__(intensity, color, "DIRECTIONAL")
        self.direction = direction / np.linalg.norm(direction)

    def getDiffuseColor(self, intercept):
        direction = [i * -1 for i in self.direction]

        intensity = np.dot(intercept.normal, direction) * self.intensity
        intensity = max(0, min(1, intensity))

        return [i * intensity for i in self.color]

    def getSpecularColor(self, intercept, viewPosition):
        direction = [i * -1 for i in self.direction]

        reflectDirection = reflect(intercept.normal, direction)

        viewDirection = np.subtract(viewPosition, intercept.point)
        viewDirection = viewDirection / np.linalg.norm(viewDirection)

        intensity = max(0, min(1, np.dot(reflectDirection, viewDirection))) ** intercept.obj.material.spec
        intensity *= self.intensity

        return [i * intensity for i in self.color]