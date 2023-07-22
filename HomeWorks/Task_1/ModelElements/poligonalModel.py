class PoligonalModel:
    def __init__(poligons: Poligon, texture: Texture):
        self.Polygons = poligons
        self.Textures = texture


class Poligon:
    Points: Point3D
    pass


class Texture:
    pass
