class Material:
    def __init__(self, diffuse=(1, 1, 1), albedo=(1, 0, 0), spec=0):
        self.diffuse = diffuse
        self.albedo = albedo
        self.spec = spec