import pygame

from Shapes.Sphere import Sphere
from Lights.Ambient import Ambient as AmbientLight
from Lights.Directional import Directional as DirectionalLight
from Lights.Point import Point as PointLight
from RayTracer import RayTracer
import Materials.Material as Material

width = 512
height = 512

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE | pygame.SCALED)
screen.set_alpha(None)

rayTracer = RayTracer(screen)
rayTracer.environmentMap = pygame.image.load("Textures/map.jpg")
rayTracer.rtClearColor(0.25, 0.25, 0.25)
rayTracer.rtColor(1, 1, 1)

rayTracer.scene.append(
    Sphere(position=(0, -1.5, -6), radius=1, material=Material.earth())
)
rayTracer.scene.append(
    Sphere(position=(0, 1.5, -6), radius=1, material=Material.moon())
)
rayTracer.scene.append(
    Sphere(position=(-2, 0, -6), radius=1, material=Material.mirror())
)
rayTracer.scene.append(
    Sphere(position=(2, 0, -6), radius=1, material=Material.disco())
)
rayTracer.scene.append(
    Sphere(position=(-0.3, 0, -3), radius=0.3, material=Material.glass())
)
rayTracer.scene.append(
    Sphere(position=(0.3, 0, -3), radius=0.3, material=Material.diamond())
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
