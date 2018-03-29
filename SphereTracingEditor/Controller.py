import View
from CustomMath import Vec2

class Controller:

    def __init__(self):
        self.Window = View.View(self, 1024,720, 'Sphere Tracing Editor')
        self.MovingNodes = False
        self.SelectedNodes = []
        self.LastMousePos = Vec2(0,0)

        self.Window.Run()


    def GraphLeftMousePressed(self):
        CurrentMousePos = self.Window.GetMousePos()
        self.Window.CreateNode(CurrentMousePos.X, CurrentMousePos.Y)


    def NodeLeftMousePressed(self, node):
        self.SelectedNodes = []
        self.SelectNode(node)
        self.MovingNodes = True
        self.LastMousePos = self.Window.GetMousePos()
      
        
    def NodeLeftMouseReleased(self, node):
        self.SelectedNodes = []
        self.MovingNodes = False


    def SelectNode(self, node):
        try:
            self.SelectedNodes.index(node)
        except ValueError:
            self.SelectedNodes.append(node)
        return 


    def Update(self):
        CurrentMousePos = self.Window.GetMousePos()
        MousePosDelta = self.LastMousePos.Sub(CurrentMousePos)
        self.LastMousePos = CurrentMousePos

        if self.MovingNodes:
            for node in self.SelectedNodes:
                node.ChangePos(MousePosDelta)
