import pygame

from Shapes.Sphere import Sphere
from Lights.Ambient import Ambient as AmbientLight
from Lights.Directional import Directional as DirectionalLight
from Lights.Point import Point as PointLight
from RayTracer import RayTracer
import Materials.Material as Material
from Shapes.Plane import Plane
from Shapes.Disk import Disk
from Shapes.AABB import AABB

width = 720
height = 720

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE | pygame.SCALED)
screen.set_alpha(None)

rayTracer = RayTracer(screen)
# rayTracer.environmentMap = pygame.image.load("Textures/map.jpg")
rayTracer.rtClearColor(0.7373, 0.561, 1)
rayTracer.rtColor(1, 1, 1)

rayTracer.scene.append(
    Plane(position=(0, -2, 0), normal=(0, 1, -0.2), material=Material.floor())
)
rayTracer.scene.append(
    Plane(position=(0, 5, 0), normal=(0, 1, 0.2), material=Material.ceiling())
)
rayTracer.scene.append(
    Plane(position=(4, 0, 0), normal=(1, 0, 0.2), material=Material.wall())
)
rayTracer.scene.append(
    Plane(position=(-4, 0, 0), normal=(1, 0, -0.2), material=Material.wall())
)
rayTracer.scene.append(
    Plane(position=(0, 0, 5), normal=(0, 0, 1), material=Material.brick())
)


rayTracer.scene.append(
    Disk(position=(-2, 0, -5), normal=(1, 0, 0.2), radius=1, material=Material.mirror())
)
rayTracer.scene.append(
    Disk(position=(2, 0, -5), normal=(1, 0, -0.2), radius=1, material=Material.mirror())
)
rayTracer.scene.append(
    Disk(position=(0, 0, -7), normal=(0, 0, 1), radius=1, material=Material.mirror())
)

rayTracer.scene.append(
    AABB(position=(-1, 0, -6), size=(1, 1, 1), material=Material.cube1())
)
rayTracer.scene.append(
    AABB(position=(1, 0, -6), size=(1, 1, 1), material=Material.cube2())
)
rayTracer.scene.append(
    AABB(position=(0, -1.5, -6), size=(1, 1, 1), material=Material.diamond())
)




rayTracer.lights.append(
    AmbientLight(intensity=0.7)
)
# rayTracer.lights.append(
#     DirectionalLight(direction=(-1, -1, -1), intensity=0.7)
# )
# rayTracer.lights.append(
#     PointLight(position=(0, 0, -4.5), intensity=1, color=(1, 0, 1))
# )

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
