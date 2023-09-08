import pygame
from pygame.locals import *

from Shapes.Sphere import Sphere
from Lights.Ambient import Ambient as AmbientLight
from Lights.Directional import Directional as DirectionalLight
from RayTracer import RayTracer
import Materials.Material as Material

width = 200
height = 200

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
screen.set_alpha(None)

rayTracer = RayTracer(screen)
rayTracer.rtClearColor(0, 0, 0)
rayTracer.rtColor(1, 1, 1)

rayTracer.scene.append(
    Sphere(position=(-2, 0, -5), radius=0.5, material=Material.brick())
)
rayTracer.scene.append(
    Sphere(position=(0, 0, -5), radius=0.5, material=Material.grass())
)
rayTracer.scene.append(
    Sphere(position=(2, 0, -5), radius=0.5, material=Material.water())
)

rayTracer.lights.append(
    AmbientLight(intensity=0.1)
)
rayTracer.lights.append(
    DirectionalLight(direction=(-1, -1, -1), intensity=0.7)
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
