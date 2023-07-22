import Point3D as Point3D


class Poligon:
    Points: Point3D
    pass


class Texture:
    pass


class PoligonalModel:
    Poligons: Poligon
    Texture: Texture

    def __init__(self, poligons, texture):
        self.Polygons = poligons
        self.Textures = texture
