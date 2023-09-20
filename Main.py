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
rayTracer.rtClearColor(0.1686, 0.2431, 0.4078)
rayTracer.rtColor(1, 1, 1)

# BODY
rayTracer.scene.append(
    Sphere(position=(0, -1.5, -5), radius=1, material=Material.snow())
)
rayTracer.scene.append(
    Sphere(position=(0, 0, -5), radius=0.75, material=Material.snow())
)
rayTracer.scene.append(
    Sphere(position=(0, 1.1, -5), radius=0.5, material=Material.snow())
)

# # BUTTONS
# rayTracer.scene.append(
#     Sphere(position=(0, -1.15, -4), radius=0.17, material=Material.coalBody())
# )
# rayTracer.scene.append(
#     Sphere(position=(0, -0.55, -4.44), radius=0.13, material=Material.coalBody())
# )
# rayTracer.scene.append(
#     Sphere(position=(0, 0.11, -4.2), radius=0.11, material=Material.coalBody())
# )
#
# # MOUTH
# mouthRadius = 0.042
# topMouth = [0.24, 0.85]
# bottomMouth = [0.09, 0.75]
# depthMouth = -4.6
#
# rayTracer.scene.append(
#     Sphere(position=(-topMouth[0], topMouth[1], depthMouth), radius=mouthRadius, material=Material.coalMouth())
# )
# rayTracer.scene.append(
#     Sphere(position=(-bottomMouth[0], bottomMouth[1], depthMouth), radius=mouthRadius, material=Material.coalMouth())
# )
# rayTracer.scene.append(
#     Sphere(position=(bottomMouth[0], bottomMouth[1], depthMouth), radius=mouthRadius, material=Material.coalMouth())
# )
# rayTracer.scene.append(
#     Sphere(position=(topMouth[0], topMouth[1], depthMouth), radius=mouthRadius, material=Material.coalMouth())
# )
#
# # NOSE
# rayTracer.scene.append(
#     Sphere(position=(0, 0.94, -4.5), radius=0.11, material=Material.carrot())
# )
#
# # EYES
# eyePosition = [0.145, 1.11]
# eyeRadius = 0.05
# eyeDepth = -4.55
# irisPosition = [0.144, 1.12]
# irisRadius = 0.025
# irisDepth = -4.52
#
# # WHITE PART
# rayTracer.scene.append(
#     Sphere(position=(-eyePosition[0], eyePosition[1] + 0.03, eyeDepth), radius=eyeRadius, material=Material.whiteEye())
# )
# rayTracer.scene.append(
#     Sphere(position=(eyePosition[0], eyePosition[1], eyeDepth), radius=eyeRadius, material=Material.whiteEye())
# )
#
# # IRIS
# rayTracer.scene.append(
#     Sphere(position=(-irisPosition[0], irisPosition[1] + 0.03, irisDepth), radius=irisRadius, material=Material.coalEye())
# )
# rayTracer.scene.append(
#     Sphere(position=(irisPosition[0], irisPosition[1], irisDepth), radius=irisRadius, material=Material.coalEye())
# )
#
rayTracer.lights.append(
    AmbientLight(intensity=0.8)
)
rayTracer.lights.append(
    DirectionalLight(direction=(-0.8, -1.5, -2), intensity=0.2, color=(0.9373, 0.8941, 0.8235))
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
