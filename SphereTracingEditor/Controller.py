import View
from CustomMath import Vec2
import GraphConnections
import GraphPins

class Controller:

    def __init__(self):
        self.Window = View.View(self, 1024,720, 'Sphere Tracing Editor')
        self.MovingNodes = False
        self.SelectedNodes = []
        self.LastMousePos = Vec2(0,0)
        self.Connection = None

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

    def NodeInputLeftMousePressed(self, node):
        print('NodeInputLeftMousePressed')

    def NodeInputLeftMouseReleased(self, node):
        print('NodeInputLeftMouseReleased')

    def NodeOutputLeftMousePressed(self, node):
        print('NodeOutputLeftMousePressed')

    def NodeOutputLeftMouseReleased(self, node):
        print('NodeOutputLeftMouseReleased')

    def NodePinLeftMousePressed(self, node, pin):
        # Clear connection
        self.ClearConnection(pin.Connection)
        
        # Create connection
        self.Connection = GraphConnections.BezierConnection(self.Window.Graph, pin, self.Window.GetMousePos())


    def NodePinLeftMouseReleased(self, node, pin):
        Widget = self.Window.GetNodeUnderCursor()
        if Widget == None or Widget == pin:
            self.Connection.Clear()
            self.Connection = None
            return 

        # Release at another pin
        if isinstance(Widget, GraphPins.GraphPin):
            self.ClearConnection(Widget.Connection)
            self.Connection.SetEnd(Widget)
            pin.SetConnection(self.Connection)
            Widget.SetConnection(self.Connection)
            self.Window.Connections.append(self.Connection)
        else:
            self.Connection.Clear()

        self.Connection = None


    def ClearConnection(self, connection):
        try:
            if connection:
                connection.Clear()
            self.Window.Connections.remove(connection)
            StartPin = connection.Start
            EndPin = connection.End
            StartPin = None
            EndPin = None
            connection = None
        except ValueError:
            pass


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

        if self.Connection:
            self.Connection.SetEnd(CurrentMousePos)
            self.Connection.Clear()
            self.Connection.Draw()

        if self.MovingNodes:
            for node in self.SelectedNodes:
                node.ChangePos(MousePosDelta)
