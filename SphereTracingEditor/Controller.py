import View
from CustomMath import Vec2
import GraphConnections
import GraphPins

class Controller:

    def __init__(self):
        self.Window = View.View(self, 1024,720, 'Sphere Tracing Editor')
        self.MovingNodes = False
        self.MovingCanvas = False
        self.SelectedNodes = []
        self.LastMousePos = Vec2(0,0)
        self.NewConnection = None

        self.Window.Run()


    def GraphRightMousePressed(self):
        CurrentMousePos = self.Window.GetMousePos()
        self.Window.CreateNode(CurrentMousePos.X, CurrentMousePos.Y)

    def NodeLeftMousePressed(self, node):
        self.SelectedNodes = []
        self.SelectNode(node)
        self.MovingNodes = True
        self.LastMousePos = self.Window.GetMousePos()
      
    def GraphLeftMousePressed(self):
        self.SelectedNodes = []

    def NodeLeftMouseReleased(self, node):
        self.MovingNodes = False

    def NodeInputLeftMousePressed(self, node):
        print('NodeInputLeftMousePressed')

    def NodeInputLeftMouseReleased(self, node):
        print('NodeInputLeftMouseReleased')

    def NodeOutputLeftMousePressed(self, node):
        print('NodeOutputLeftMousePressed')

    def NodeOutputLeftMouseReleased(self, node):
        print('NodeOutputLeftMouseReleased')

    def GraphScrollPressed(self):
        self.MovingCanvas = True

    def GraphScrollReleased(self):
        self.MovingCanvas = False

    def NodePinLeftMousePressed(self, node, pin):
        # Create connection
        self.NewConnection = GraphConnections.BezierConnection(self.Window.Graph, pin, self.Window.GetMousePos())
        pin.SetConnection(self.NewConnection)
        self.NewConnection.SetStart(pin)
      
    def DeleteBtnPressed(self):
        for node in self.SelectedNodes:
            node.Delete()
            self.SelectedNodes.remove(node)

    def NodePinLeftMouseReleased(self, node, oldPin):

        NewPin = self.Window.GetNodeUnderCursor()

        # No pin under cursor
        if NewPin == None:
            self.NewConnection.Remove()
            self.NewConnection.Clear()
            self.NewConnection = None
            return

        # End pin same as start pin
        if NewPin == oldPin:
            oldPin.RemoveAllConnections()
            self.NewConnection.Remove()
            self.NewConnection.Clear()
            self.NewConnection = None
            return

        # Release at different pin
        if isinstance(NewPin, GraphPins.GraphPin):
            
            if oldPin.IsAlreadyConnection(NewPin):
                self.NewConnection.Remove()
            else:
                NewPin.SetConnection(self.NewConnection)
                self.NewConnection.SetEnd(NewPin)

            self.NewConnection.Clear()
            self.NewConnection = None
        


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

        if self.NewConnection:
            self.NewConnection.SetEnd(CurrentMousePos)
            self.NewConnection.Clear()
            self.NewConnection.Draw()

        if self.MovingNodes:
            for node in self.SelectedNodes:
                node.ChangePos(MousePosDelta)

        if self.MovingCanvas:
            for node in self.Window.Nodes:
                node.ChangePos(MousePosDelta)
