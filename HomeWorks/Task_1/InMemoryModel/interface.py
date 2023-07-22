import zope.inteface
from zope.interface import implements



class IModelChagedObserver(zope.interface.Interface):

    def ApplyUpdateModel(self):
        pass


class IModelChanger(zope.interface.Interface):
    def NotifyChange(self):
        pass


class ModelChagedObserver(object):
    implements(IModelChagedObserver)


class ModelChanger(object):
    implements(IModelChanger)
