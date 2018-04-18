
class ModelConnection:
    def __init__(self, inputIndex, outputIndex, node):
        self.InputIndex = inputIndex
        self.OutputIndex = outputIndex
        self.Node = node

class ModelNodes:
    def __init__(self):
        self.Children = []

    def AddChild(self, child, inputIndex, outputIndex):
        self.Children.append(ModelConnection(inputIndex, outputIndex, child))

    @staticmethod
    def GetChildren():
        return ModelNodes.__subclasses__()

class Sphere(ModelNodes):
    def __init__(self):
        super().__init__()
 
        
class Box(ModelNodes):
    def __init__(self):
        super().__init__()


class Intersect(ModelNodes):
    def __init__(self):
        super().__init__()


class Union(ModelNodes):
    def __init__(self):
        super().__init__()


class Subtract(ModelNodes):
    def __init__(self):
        super().__init__()


