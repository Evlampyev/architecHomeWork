class Flash:
    Location: Point3D
    Angle: Angl3D
    Color: Color
    Power: float

    def __init__(self, location, angle, color, power):
        self.Location = location
        self.Angle = angle
        self.Color = color
        self.Power = power

    def Rotate(self, Angel3D):
        pass

    def Move(self, Point3D):
        pass
