import Lights.Light as Light


class Directional(Light.Light):
    def __init__(self, direction=(0, -1, 0), intensity=1, color=(1, 1, 1)):
        super().__init__(intensity, color, "DIRECTIONAL")
        self.direction = direction

