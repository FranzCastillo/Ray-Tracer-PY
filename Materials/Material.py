import pygame

OPAQUE = 0
REFLECTIVE = 1
TRANSPARENT = 2


class Material:
    def __init__(self, diffuse=(1, 1, 1), spec=1.0, ks=0.0, ior=1.0, type=OPAQUE, texture=None):
        self.diffuse = diffuse
        self.spec = spec
        self.ks = ks
        self.ior = ior
        self.type = type
        self.texture = texture


def frame():
    return Material(diffuse=(0.4375, 0.453, 0.363), spec=64, ks=0.15, type=OPAQUE)


def ribbon():
    return Material(diffuse=(0.789, 0.328, 0.144), spec=64, ks=0.15, type=OPAQUE)


def gold():
    return Material(diffuse=(0.8314, 0.6863, 0.2157), spec=64, ks=0.15, type=OPAQUE)


def marble():
    return Material(diffuse=(0.8, 0.8, 0.8), spec=64, ks=0.15, type=OPAQUE)


def hockeyPuck():
    return Material(diffuse=(0.297, 0.3125, 0.223), spec=128, ks=0.2, type=OPAQUE)


def cube1():
    return Material(diffuse=(0.7373, 0.561, 1), spec=64, ks=0.15, type=OPAQUE,
                    texture=pygame.image.load("Textures/cube1.png"))


def cube2():
    return Material(diffuse=(0.7373, 0.561, 1), spec=64, ks=0.15, type=OPAQUE,
                    texture=pygame.image.load("Textures/cube2.jpg"))


def floor():
    return Material(diffuse=(0.789, 0.328, 0.144), spec=64, ks=0.15, type=REFLECTIVE)


def wall():
    return Material(diffuse=(0.3373, 0.3529, 0.2627))


def ceiling():
    return Material(diffuse=(1, 0.561, 1))


def glass():
    return Material(diffuse=(0.8, 0.8, 0.8), spec=64, ks=0.15, ior=1.5, type=TRANSPARENT)


def diamond():
    return Material(diffuse=(0.6196, 1, 0.9608), spec=128, ks=0.2, ior=2.417, type=TRANSPARENT)


def mirror():
    return Material(diffuse=(0.8, 0.8, 0.8), spec=64, ks=0.2, type=REFLECTIVE)


def blueMirror():
    return Material(diffuse=(0.2, 0.2, 0.8), spec=32, ks=0.15, type=REFLECTIVE)


def disco():
    return Material(diffuse=(0.8, 0.8, 0.8), spec=32, ks=0.15, type=REFLECTIVE,
                    texture=pygame.image.load("Textures/disco.jpg"))


def earth():
    return Material(texture=pygame.image.load("Textures/earth.jpeg"))


def moon():
    return Material(texture=pygame.image.load("Textures/moon.jpg"))


def checkered():
    return Material(spec=64, ks=0.2, type=REFLECTIVE, texture=pygame.image.load("Textures/checkered.jpg"))


def brick():
    return Material(diffuse=(1, 0.3, 0.2), spec=8, ks=0.01)


def grass():
    return Material(diffuse=(0.2, 0.8, 0.2), spec=32, ks=0.1)


def water():
    return Material(diffuse=(0.2, 0.2, 0.8), spec=256, ks=0.5)


def snow():
    return Material(diffuse=(0.9373, 0.8941, 0.8235), spec=2, ks=0.01)


def coalBody():
    return Material(diffuse=(0.1, 0.1, 0.1), spec=256, ks=0.01)


def coalMouth():
    return Material(diffuse=(0.4509, 0.3922, 0.3725), spec=256, ks=0.5)


def carrot():
    return Material(diffuse=(0.9961, 0.3294, 0.2078), spec=256, ks=0.5)


def whiteEye():
    return Material(diffuse=(0.8275, 0.7412, 0.7686), spec=250, ks=0.1)


def coalEye():
    return Material(diffuse=(0.1, 0.1, 0.1), spec=250, ks=0.1)
