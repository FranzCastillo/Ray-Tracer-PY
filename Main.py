import pygame
import math as Math

from Shapes.Sphere import Sphere
from Lights.Ambient import Ambient as AmbientLight
from Lights.Directional import Directional as DirectionalLight
from Lights.Point import Point as PointLight
from RayTracer import RayTracer
import Materials.Material as Material
from Shapes.Plane import Plane
from Shapes.Disk import Disk
from Shapes.AABB import AABB
from Shapes.Cylinder import Cylinder

width = 520
height = 520

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE | pygame.SCALED)
screen.set_alpha(None)

rayTracer = RayTracer(screen)
rayTracer.environmentMap = pygame.image.load("Textures/map.jpg")
rayTracer.rtClearColor(0.7373, 0.561, 1)
rayTracer.rtColor(1, 1, 1)

# rayTracer.scene.append(
#     Plane(position=(0, -2, 0), normal=(0, 1, -0.2), material=Material.ceiling())
# )
# rayTracer.scene.append(
#     Plane(position=(0, 5, 0), normal=(0, 1, 0.2), material=Material.floor())
# )
# rayTracer.scene.append(
#     Plane(position=(4, 0, 0), normal=(1, 0, 0.2), material=Material.wall())
# )
# rayTracer.scene.append(
#     Plane(position=(-4, 0, 0), normal=(1, 0, -0.2), material=Material.wall())
# )
# rayTracer.scene.append(
#     Plane(position=(0, 0, 5), normal=(0, 0, 1), material=Material.brick())
# )
#
# rayTracer.scene.append(
#     Cylinder(
#         position=(-2, -1, -7),
#         radius=1,
#         height=1,
#         material=Material.glass()
#     )
# )
#
# rayTracer.scene.append(
#     Cylinder(
#         position=(2, -1, -7),
#         radius=1,
#         height=1,
#         material=Material.glass()
#     )
# )
#
# rayTracer.scene.append(
#     Cylinder(
#         position=(0, 1, -7),
#         radius=1,
#         height=0.5,
#         material=Material.mirror()
#     )
# )

rayTracer.scene.append(
    Cylinder(
        position=(0, 0, -10),
        radius=2,
        height=15,
        rotation_z=70 * Math.pi/180,
        material=Material.hockeyPuck()
    )
)

rayTracer.lights.append(
    AmbientLight(intensity=0.5)
)
rayTracer.lights.append(
    DirectionalLight(direction=(0, -0.2, 1), intensity=1, color=(1, 0, 1))
)
# rayTracer.lights.append(
#     PointLight(position=(0, -3, -9), intensity=1, color=(1, 0, 1))
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
