from math import tan, pi

import numpy as np


class RayTracer(object):
    def __init__(self, screen):
        self.vpX = 0
        self.vpY = 0
        self.vpWidth = 0
        self.vpHeight = 0
        self.nearPlane = 0
        self.topEdge = 0
        self.rightEdge = 0
        self.clearColor = None
        self.currentColor = None

        self.screen = screen
        _, _, self.width, self.height = screen.get_rect()

        self.scene = []
        self.lights = []

        self.cameraPosition = [0, 0, 0]

        self.rtViewPort(0, 0, self.width, self.height)
        self.rtProjection()

        self.rtClearColor(0, 0, 0)
        self.rtColor(1, 1, 1)
        self.rtClear()

    def rtViewPort(self, x, y, width, height):
        self.vpX = x
        self.vpY = y
        self.vpWidth = width
        self.vpHeight = height

    def rtProjection(self, fov=60, near=0.1):
        aspectRatio = self.vpWidth / self.vpHeight
        self.nearPlane = near
        self.topEdge = near * tan(fov * pi / 360)
        self.rightEdge = self.topEdge * aspectRatio

    def rtClearColor(self, r, g, b):
        self.clearColor = (r * 255, g * 255, b * 255)

    def rtColor(self, r, g, b):
        self.currentColor = (r * 255, g * 255, b * 255)

    def rtClear(self):
        self.screen.fill(self.clearColor)

    def rtPoint(self, x, y, color=None):
        y = self.width - y
        if (0 <= x < self.width) and (0 <= y < self.height):
            if color is None:
                color = self.currentColor
            else:
                color = (color[0] * 255, color[1] * 255, color[2] * 255)

            self.screen.set_at((x, y), color)

    def rtCastRay(self, origin, direction):
        hit = None

        for obj in self.scene:
            intercept = obj.intersect(origin, direction)
            if intercept is not None:
                hit = intercept

        return hit

    def rtRender(self):
        for x in range(self.vpX, self.vpX + self.vpWidth + 1):
            for y in range(self.vpY, self.vpY + self.vpHeight + 1):
                if (0 <= x < self.width) and (0 <= y < self.height):
                    pX = 2 * ((x + 0.5 - self.vpX) / self.vpWidth) - 1
                    pY = 2 * ((y + 0.5 - self.vpY) / self.vpHeight) - 1

                    pX *= self.rightEdge
                    pY *= self.topEdge

                    direction = (pX, pY, -self.nearPlane)
                    direction = direction / np.linalg.norm(direction)

                    intercept = self.rtCastRay(self.cameraPosition, direction)
                    if intercept is not None:
                        objMaterial = intercept.obj.material
                        pixelColor = list(objMaterial.diffuse)

                        ambientLight = [0, 0, 0]
                        directionalLight = [0, 0, 0]

                        for light in self.lights:
                            if light.type == "AMBIENT":
                                ambientLight[0] += light.intensity * light.color[0]
                                ambientLight[1] += light.intensity * light.color[1]
                                ambientLight[2] += light.intensity * light.color[2]
                            elif light.type == "DIRECTIONAL":
                                lightDir = np.array(light.direction) * -1
                                lightDir = lightDir / np.linalg.norm(lightDir)
                                intensity = np.dot(intercept.normal, lightDir)
                                intensity = max(0, min(1, intensity))

                                directionalLight[0] += light.intensity * light.color[0] * intensity
                                directionalLight[1] += light.intensity * light.color[1] * intensity
                                directionalLight[2] += light.intensity * light.color[2] * intensity

                        pixelColor[0] *= ambientLight[0] + directionalLight[0]
                        pixelColor[1] *= ambientLight[1] + directionalLight[1]
                        pixelColor[2] *= ambientLight[2] + directionalLight[2]

                        pixelColor[0] = min(1, pixelColor[0])
                        pixelColor[1] = min(1, pixelColor[1])
                        pixelColor[2] = min(1, pixelColor[2])

                        self.rtPoint(x, y, pixelColor)

