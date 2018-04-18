import tkinter as tk
from CustomMath import Vec2
import GraphConnections

class GraphPin:

    Size = Vec2(10,10)

    def __init__(self, owner, index, widget, pos):
        self.Widget = widget
        self.Owner = owner
        self.Pos = pos
        self.Index = index

        self.InitWidgets()
        self.InitEvents()


    def InitWidgets(self):
        self.PinImg = tk.Frame(self.Widget, bg='blue')
        self.PinImg.place_configure(x=self.Pos.X,y=self.Pos.Y - GraphPin.Size.Y/2)
        self.PinImg.configure(width=GraphPin.Size.X,height=GraphPin.Size.Y)
        self.PinImg.Owner = self

    def InitEvents(self):
        self.PinImg.bind('<ButtonPress-1>', lambda event: self.Owner.NodePinLeftMousePressed(self))
        self.PinImg.bind('<ButtonRelease-1>', lambda event: self.Owner.NodePinLeftMouseReleased(self))

    def GetPos(self, graph):
        return Vec2(self.PinImg.winfo_rootx() - graph.winfo_rootx(), self.PinImg.winfo_rooty() - graph.winfo_rooty())

    def SetConnection(self, connection):
        print('GraphPin::SetConnection not implemented')

    def RemoveConnection(self, connection):
        print('GraphPin::RemoveConnection not implemented')

    def DrawConnection(self):
        print('GraphPin::DrawConnection not implemented')

    def ClearConnection(self):
        print('GraphPin::ClearConnection not implemented')

    def RemoveAllConnections(self):
        print('GraphPin::RemoveAllConnections not implemented')

    def IsAlreadyConnection(self, otherPin):
        print('GraphPin::IsAlreadyConnection not implemented')

    def IsConnected(self):
        print('GraphPin::IsConnected not implemented')

    def IsOutputPin(self):
        print('GraphPin::IsOutputPin not implemented')

class GraphInputPin(GraphPin):
    def __init__(self, owner, index, widget, pos = Vec2()):
        super().__init__(owner, index, widget, pos)

        # Allow only one connection
        self.Connection = None

    def GetConnectedPin(self):
        if self.Connection:
            return self.Connection.GetOther(self)
        return None

    def SetConnection(self, connection):
        if not(isinstance(connection, GraphConnections.BezierConnection)):
            print('Bad parametr in GraphPins::SetConnection')
            return

        # Clear connection at both ends if there is one
        if self.Connection != None:
            self.Connection.Remove()

        self.Connection = connection


    def RemoveConnection(self, connection):
        self.Connection = None
            

    def DrawConnection(self):
        if self.Connection:
            self.Connection.Draw()
            
    def ClearConnection(self):
        if self.Connection:
            self.Connection.Clear()

    def RemoveAllConnections(self):
        if self.Connection:
            self.Connection.Remove()

    def IsAlreadyConnection(self, otherPin):
        return self.Connection.CheckConnection(self, otherPin)

    def IsConnected(self):
        if self.Connection:
            return True
        else:
            return False

    def IsOutputPin(self):
        return False


class GraphOutputPin(GraphPin):
    def __init__(self, owner, index, widget, pos = Vec2()):
        super().__init__(owner, index, widget, pos)

        # Allow multiple connections
        self.Connections = []

    def GetConnectedPins(self):
        Result = []
        for connection in self.Connections:
            Other = connection.GetOther(self)
            if Other:
                Result.append(Other)
        return Result

    def SetConnection(self, connection):
        if not(isinstance(connection, GraphConnections.BezierConnection)):
            print('Bad parametr in GraphPins::SetConnection')
            return

        self.Connections.append(connection)


    def RemoveConnection(self, connection):
        try:
            self.Connections.remove(connection)
        except ValueError:
            pass


    def DrawConnection(self):
        for connection in self.Connections:
            connection.Draw()

    def ClearConnection(self):
        for connection in self.Connections:
            connection.Clear()

    def RemoveAllConnections(self):
        for connection in self.Connections:
            connection.Remove()

    def IsAlreadyConnection(self, otherPin):
        for connection in self.Connections:
            if connection.CheckConnection(self, otherPin):
                return True
        return False

    def IsConnected(self):
        return len(self.Connections) > 0

    def IsOutputPin(self):
        return True
 