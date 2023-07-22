from ModelElements import poligonModel
from Scene
from Flash import
from PoligonModel import
from


class ModelStore:
    Models: PoligonModel
    Scenes: Scene
    Flashes: Flash
    Cameras: Camera
    changeObservers: IModelChangeObserver

    def __init__(self, models, scenes , flashes, cameras, change_Observers):
        self.Models = models
        self.Scenes = scenes
        self.Flashes = flashes
        self.Cameras = cameras
        self.changeObservers = change_Observers

    def GetScena(count: int):
        scene = Scene()
        return scene

    def NotifyChange(IModelChanger):
