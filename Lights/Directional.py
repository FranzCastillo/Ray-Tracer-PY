import Lights.Light as Light
import MyNumPy as np


def reflect(normal, direction):
    dot = np.dot(normal, direction)
    scaled = np.multiplyVectorScalar(normal, dot)
    reflectValue = np.multiplyVectorScalar(scaled, 2)
    reflectValue = np.subtract(reflectValue, direction)
    return np.normalize(reflectValue)


class Directional(Light.Light):
    def __init__(self, direction=(0, 1, 0), intensity=1, color=(1, 1, 1)):
        super().__init__(intensity, color, "DIRECTIONAL")
        self.direction = np.normalize(direction)

    def getDiffuseColor(self, intercept):
        direction = [i * -1 for i in self.direction]

        intensity = np.dot(intercept.normal, direction) * self.intensity
        intensity = max(0, min(1, intensity))
        intensity *= 1 - intercept.obj.material.ks

        return [i * intensity for i in self.color]

    def getSpecularColor(self, intercept, viewPosition):
        direction = [i * -1 for i in self.direction]

        reflectDirection = reflect(intercept.normal, direction)

        viewDirection = np.subtract(viewPosition, intercept.point)
        viewDirection = np.normalize(viewDirection)

        intensity = max(0, min(1, np.dot(reflectDirection, viewDirection))) ** intercept.obj.material.spec
        intensity *= self.intensity
        intensity *= intercept.obj.material.ks

        return [i * intensity for i in self.color]