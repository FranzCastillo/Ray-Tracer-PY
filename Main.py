import pygame
from pygame.locals import *

from Shapes.Sphere import Sphere
from Lights.Ambient import Ambient as AmbientLight
from Lights.Directional import Directional as DirectionalLight
from RayTracer import RayTracer
from Materials.Material import Material

width = 512
height = 512

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
screen.set_alpha(None)

rayTracer = RayTracer(screen)
rayTracer.rtClearColor(0, 0, 0)
rayTracer.rtColor(1, 1, 1)

brickMaterial = Material(diffuse=(1, 0.3, 0.2), albedo=(0.3, 0.3, 0.3), spec=50)

rayTracer.scene.append(
    Sphere(position=(0, 0, -5), radius=1, material=brickMaterial),
)
rayTracer.lights.append(
    AmbientLight(intensity=0.1)
)
rayTracer.lights.append(
    DirectionalLight(direction=(0, -1, -1), intensity=0.7)
)

isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

    rayTracer.rtClear()
    rayTracer.rtRender()
    pygame.display.flip()

pygame.quit()
