import pygame

from Shapes.Sphere import Sphere
from Lights.Ambient import Ambient as AmbientLight
from Lights.Directional import Directional as DirectionalLight
from Lights.Point import Point as PointLight
from RayTracer import RayTracer
import Materials.Material as Material

width = 365
height = 365

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
screen.set_alpha(None)

rayTracer = RayTracer(screen)
# rayTracer.environmentMap = pygame.image.load("Textures/map.jpg")
rayTracer.rtClearColor(0.25, 0.25, 0.25)
rayTracer.rtColor(1, 1, 1)

rayTracer.scene.append(
    Sphere(position=(1, 1, -5), radius=0.5, material=Material.grass())
)
rayTracer.scene.append(
    Sphere(position=(0, 0, -7), radius=2, material=Material.checkered())
)
rayTracer.scene.append(
    Sphere(position=(0.5, -1, -5), radius=0.3, material=Material.water())
)
rayTracer.scene.append(
    Sphere(position=(-1.5, -1, -5), radius=0.5, material=Material.earth())
)

rayTracer.lights.append(
    AmbientLight(intensity=0.4)
)
rayTracer.lights.append(
    DirectionalLight(direction=(-1, -1, -1), intensity=0.7)
)
rayTracer.lights.append(
    PointLight(position=(0, 0, -4.5), intensity=1, color=(1, 0, 1))
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
