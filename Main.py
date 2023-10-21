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

width = 500
height = 500

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE | pygame.SCALED)
screen.set_alpha(None)

rayTracer = RayTracer(screen)
rayTracer.environmentMap = pygame.image.load("Textures/museum.jpg")
rayTracer.rtClearColor(0.3373, 0.3529, 0.2627)
rayTracer.rtColor(1, 1, 1)


def room():
    rayTracer.scene.append(
        AABB(
            position=(0, -4, -12),
            size=(20, 2, 20),
            material=Material.floor()
        )
    )
    rayTracer.scene.append(
        AABB(
            position=(-6, 1.5, -14),
            size=(1, 15, 10),
            material=Material.wall()
        )
    )
    rayTracer.scene.append(
        AABB(
            position=(6, 1.5, -14),
            size=(1, 15, 10),
            material=Material.wall()
        )
    )
    rayTracer.scene.append(
        AABB(
            position=(0, 0, -20),
            size=(20, 25, 1),
            material=Material.wall()
        )
    )
    rayTracer.scene.append(
        Cylinder(
            position=(-5.16, -2.8, -17.5999),
            radius=0.03,
            height=15,
            material=Material.hockeyPuck(),
        )
    )
    rayTracer.scene.append(
        Cylinder(
            position=(5.16, -2.8, -17.5999),
            radius=0.03,
            height=15,
            material=Material.hockeyPuck(),
        )
    )

    # FRAMES
    #   RIGHT
    rayTracer.scene.append(
        AABB(
            position=(5.8, 2, -10),
            size=(2, 4, 2),
            material=Material.frame()
        )
    )
    rayTracer.scene.append(
        Disk(
            position=(4.5, 2, -12),
            radius=0.7,
            normal=(-1, 0, -0.05),
            material=Material.frame()
        )
    )
    #   LEFT
    rayTracer.scene.append(
        AABB(
            position=(-6, 3, -12),
            size=(2, 4, 2),
            material=Material.frame()
        )
    )


def pedestal():
    rayTracer.scene.append(
        # MIDDLE
        AABB(
            position=(0, -1.5, -10),
            size=(2, 2, 2),
            material=Material.marble()
        )
    )
    rayTracer.scene.append(
        # BOTTOM
        AABB(
            position=(0, -3, -10),
            size=(2.5, 1, 2.5),
            material=Material.marble()
        )
    )
    rayTracer.scene.append(
        # TOP
        AABB(
            position=(0, -0.2, -10),
            size=(3, 0.8, 3),
            material=Material.marble()
        )
    )
    rayTracer.scene.append(
        Sphere(
            position=(0, 0.6, -9),
            radius=0.5,
            material=Material.earth(),
        )
    )
    rayTracer.scene.append(
        Sphere(
            position=(0, 1.6, -9),
            radius=0.5,
            material=Material.diamond(),
        )
    )
    rayTracer.scene.append(
        Pyramid(
            position=(-1, 0.2, -9),
            base=0.5,
            height=0.5,
            material=Material.diamond(),
        )
    )
    rayTracer.scene.append(
        Pyramid(
            position=(1, 0.2, -9),
            base=0.5,
            height=0.5,
            material=Material.diamond(),
        )
    )


def leftPole():
    rayTracer.scene.append(
        Sphere(
            position=(-3, 0.05, -8),
            radius=0.2,
            material=Material.gold()
        )
    )
    rayTracer.scene.append(
        Pyramid(
            position=(-3, -0.3, -8),
            base=0.3,
            height=0.3,
            material=Material.gold()
        )
    )
    rayTracer.scene.append(
        Cylinder(
            position=(-3, -2.8, -8),
            radius=0.1,
            height=2.5,
            material=Material.gold()
        )
    )
    rayTracer.scene.append(
        Cylinder(
            position=(-3, -2.8, -8),
            radius=0.15,
            height=0.2,
            material=Material.gold()
        )
    )
    rayTracer.scene.append(
        Pyramid(
            position=(-3, -3, -8),
            base=0.5,
            height=0.5,
            material=Material.gold()
        )
    )


def rightPole():
    rayTracer.scene.append(
        Sphere(
            position=(3, 0.05, -8),
            radius=0.2,
            material=Material.gold()
        )
    )
    rayTracer.scene.append(
        Pyramid(
            position=(3, -0.3, -8),
            base=0.3,
            height=0.3,
            material=Material.gold()
        )
    )
    rayTracer.scene.append(
        Cylinder(
            position=(3, -2.8, -8),
            radius=0.1,
            height=2.5,
            material=Material.gold()
        )
    )
    rayTracer.scene.append(
        Cylinder(
            position=(3, -2.8, -8),
            radius=0.15,
            height=0.2,
            material=Material.gold()
        )
    )
    rayTracer.scene.append(
        Pyramid(
            position=(3, -3, -8),
            base=0.5,
            height=0.5,
            material=Material.gold()
        )
    )


def backLeftPole():
    rayTracer.scene.append(
        Sphere(
            position=(-3, 0.05, -12),
            radius=0.2,
            material=Material.gold()
        )
    )
    rayTracer.scene.append(
        Pyramid(
            position=(-3, -0.3, -12),
            base=0.3,
            height=0.3,
            material=Material.gold()
        )
    )
    rayTracer.scene.append(
        Cylinder(
            position=(-3, -2.8, -12),
            radius=0.1,
            height=2.5,
            material=Material.gold()
        )
    )
    rayTracer.scene.append(
        Cylinder(
            position=(-3, -2.8, -12),
            radius=0.15,
            height=0.2,
            material=Material.gold()
        )
    )
    rayTracer.scene.append(
        Pyramid(
            position=(-3, -3, -12),
            base=0.5,
            height=0.5,
            material=Material.gold()
        )
    )


def backRightPole():
    rayTracer.scene.append(
        Sphere(
            position=(3, 0.05, -12),
            radius=0.2,
            material=Material.gold()
        )
    )
    rayTracer.scene.append(
        Pyramid(
            position=(3, -0.3, -12),
            base=0.3,
            height=0.3,
            material=Material.gold()
        )
    )
    rayTracer.scene.append(
        Cylinder(
            position=(3, -2.8, -12),
            radius=0.1,
            height=2.5,
            material=Material.gold()
        )
    )
    rayTracer.scene.append(
        Cylinder(
            position=(3, -2.8, -12),
            radius=0.15,
            height=0.2,
            material=Material.gold()
        )
    )
    rayTracer.scene.append(
        Pyramid(
            position=(3, -3, -12),
            base=0.5,
            height=0.5,
            material=Material.gold()
        )
    )


def spotLights():
    # MIDDLE
    rayTracer.scene.append(
        Cylinder(
            position=(0, 4, -10),
            radius=0.7,
            height=0.5,
            material=Material.earth()
        )
    )
    rayTracer.scene.append(
        Cylinder(
            position=(-0.1, 4, -9),
            radius=0.1,
            height=2,
            material=Material.earth()
        )
    )
    rayTracer.scene.append(
        Cylinder(
            position=(0.3, 5, -11),
            radius=0.1,
            height=2,
            material=Material.earth()
        )
    )
    rayTracer.lights.append(
        PointLight(position=(0, 2, -8), intensity=1, color=(1, 1, 0))
    )

    # LEFT
    rayTracer.scene.append(
        Cylinder(
            position=(2, 6.5, -10),
            radius=0.9,
            height=0.5,
            rotation_z=Math.radians(45),
            material=Material.earth()
        )
    )
    rayTracer.scene.append(
        Cylinder(
            position=(-3.5, 6.5, -15),
            radius=0.1,
            height=3,
            material=Material.earth()
        )
    )

    # RIGHT
    rayTracer.scene.append(
        Cylinder(
            position=(-2.5, 6.5, -10),
            radius=0.9,
            height=0.5,
            rotation_z=Math.radians(-45),
            material=Material.earth()
        )
    )
    rayTracer.scene.append(
        Cylinder(
            position=(3.5, 6.5, -15),
            radius=0.1,
            height=3,
            material=Material.earth()
        )
    )

def lights():
    rayTracer.lights.append(
        PointLight(position=(0, 0, -7), intensity=1, color=(1, 1, 0))
    )
    rayTracer.lights.append(
        PointLight(position=(-2, 0, -7), intensity=1, color=(1, 1, 0))
    )
    rayTracer.lights.append(
        PointLight(position=(2, 0, -7), intensity=1, color=(1, 1, 0))
    )

room()
pedestal()
leftPole()
rightPole()
backLeftPole()
backRightPole()
spotLights()
lights()


# rayTracer.lights.append(
#     PointLight(position=(-3, 1, -7), intensity=1, color=(1, 1, 0))
# )
# rayTracer.lights.append(
#     PointLight(position=(3, 1, -7), intensity=1, color=(1, 1, 0))
# )

rayTracer.lights.append(
    AmbientLight(intensity=0.6)
)
rayTracer.lights.append(
    DirectionalLight(direction=(0, 1, -1), intensity=0.1, color=(1, 1, 0))
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
