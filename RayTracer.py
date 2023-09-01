from math import tan, pi

import numpy as np


class RayTracer(object):
    def __init__(self, screen):
        self.screen = screen
        _, _, self.width, self.height = screen.get_rect()

        self.scene = []

        self.cameraPosition = [0, 0, 0]

        self.rtViewPort(0, 0, self.width, self.height)
        self.rtProjection()

        self.clearColor = (0, 0, 0)
        self.currentColor = (1, 1, 1)
        self.rtClear()

        self.vpX = 0
        self.vpY = 0
        self.vpWidth = 0
        self.vpHeight = 0
        self.nearPlane = 0
        self.topEdge = 0
        self.rightEdge = 0

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
        y = self.height - y
        if (0 <= x < self.width) and (0 <= y < self.height):
            if color is None:
                color = self.currentColor
            else:
                color = (color[0] * 255, color[1] * 255, color[2] * 255)

            self.screen.set_at((x, y), color)

    def rtCastRay(self, origin, direction):
        for obj in self.scene:
            if obj.intersect(origin, direction):
                return True

        return False

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

                    if self.rtCastRay(self.cameraPosition, direction):
                        self.rtPoint(x, y)
