class CorrectInput:
    def __init__(self, *args):
        param = []
        for arg in args:
            param.append(arg)
        self.param = param

    def allFigureParametresInputCorrect(self):
        result = True
        for arg in self.param:
            if arg <= 0:
                result = False
        return result

    def triangleParametresInputCorrect(self):
        result = True
        if self.param[0] + self.param[1] <= self.param[2] or self.param[1] + self.param[2] <= self.param[0] \
                or self.param[2] + self.param[0] <= self.param[1]:
            result = False
        return result


        return True
