from HomeWorks.Task_1.ModelElements.poligonalModel import PoligonalModel
from HomeWorks.Task_1.ModelElements.flash import Flash
from HomeWorks.Task_1.ModelElements.scene import Scene
from HomeWorks.Task_1.ModelElements.camera import Camera
from interface import IModelChagedObserver


class ModelStore:
    Models: PoligonalModel()
    Scenes: Scene()
    Flashes: Flash()
    Cameras: Camera()
    changeObservers: IModelChagedObserver()

    def __init__(self, models, scenes, flashes, cameras, change_Observers):
        self.Models = models
        self.Scenes = scenes
        self.Flashes = flashes
        self.Cameras = cameras
        self.changeObservers = change_Observers

    def GetScena(count: int):
        scene = Scene()
        return scene

    def NotifyChange(IModelChanger):
        pass
