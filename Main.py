import pygame

from Shapes.Sphere import Sphere
from Lights.Ambient import Ambient as AmbientLight
from Lights.Directional import Directional as DirectionalLight
from RayTracer import RayTracer
import Materials.Material as Material

width = 365
height = 365

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
screen.set_alpha(None)

rayTracer = RayTracer(screen)
rayTracer.rtClearColor(0, 0, 0)
rayTracer.rtColor(1, 1, 1)

# BODY
rayTracer.scene.append(
    Sphere(position=(0, 0, -2), radius=0.5, material=Material.snow())
)

rayTracer.lights.append(
    AmbientLight(intensity=0.4)
)
rayTracer.lights.append(
    DirectionalLight(direction=(1, 0, -2), intensity=0.6, color=(1, 0, 1))
)
rayTracer.lights.append(
    DirectionalLight(direction=(-1, 0, -2), intensity=0.6, color=(0, 1, 1))
)

rayTracer.rtClear()
rayTracer.rtRender()

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

pygame.quit()
