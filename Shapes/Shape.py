class Shape:
    def __init__(self, position):
        self.position = position

    def intersect(self, origin, direction):
        raise NotImplementedError()

    def normal(self, point):
        raise NotImplementedError()