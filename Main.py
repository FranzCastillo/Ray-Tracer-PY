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
from Shapes.Pyramid import Pyramid

width = 265
height = 265

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE | pygame.SCALED)
screen.set_alpha(None)

rayTracer = RayTracer(screen)
# rayTracer.environmentMap = pygame.image.load("Textures/map.jpg")
rayTracer.rtClearColor(0.3373, 0.3529, 0.2627)
rayTracer.rtColor(1, 1, 1)

# ROOM
rayTracer.scene.append(
    AABB(
        position=(0, -8, -10),
        size=(10, 10, 11),
        material=Material.floor()
    )
)

rayTracer.scene.append(
    Pyramid(
        position=(0, 0, -10),
        base=1,
        height=1,
        material=Material.glass()
    )
)

# # LEFT POLE
# rayTracer.scene.append(
#     Cylinder(
#         position=(-3, -2.8, -8),
#         radius=0.1,
#         height=2.5,
#         material=Material.gold()
#     )
# )
# rayTracer.scene.append(
#     Cylinder(
#         position=(-3, -2.8, -8),
#         radius=0.2,
#         height=0.2,
#         material=Material.gold()
#     )
# )

# RIGHT POLE
# rayTracer.scene.append(
#     Cylinder(
#         position=(3, -2.8, -8),
#         radius=0.1,
#         height=2.5,
#         material=Material.gold()
#     )
# )

# # PEDESTAL
# rayTracer.scene.append(
#     # MIDDLE
#     AABB(
#         position=(0, -1.5, -10),
#         size=(2, 2, 2),
#         material=Material.marble()
#     )
# )
# rayTracer.scene.append(
#     # BOTTOM
#     AABB(
#         position=(0, -3, -10),
#         size=(2.5, 1, 2.5),
#         material=Material.marble()
#     )
# )
# rayTracer.scene.append(
#     # TOP
#     AABB(
#         position=(0, -0.2, -10),
#         size=(3, 0.8, 3),
#         material=Material.marble()
#     )
# )
# rayTracer.lights.append(
#     PointLight(position=(0, 1, -7), intensity=1, color=(1, 1, 0))
# )
# rayTracer.lights.append(
#     PointLight(position=(-3, 1, -7), intensity=1, color=(1, 1, 0))
# )
# rayTracer.lights.append(
#     PointLight(position=(3, 1, -7), intensity=1, color=(1, 1, 0))
# )

rayTracer.lights.append(
    AmbientLight(intensity=0.5)
)
rayTracer.lights.append(
    DirectionalLight(direction=(1, -1, -1), intensity=0.1, color=(1, 1, 0))
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
