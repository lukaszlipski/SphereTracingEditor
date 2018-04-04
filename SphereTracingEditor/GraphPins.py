import tkinter as tk
from CustomMath import Vec2
import GraphConnections

class GraphPin:

    Size = Vec2(10,10)

    def __init__(self, owner, index, widget, pos=Vec2()):
        self.Widget = widget
        self.Owner = owner
        self.Pos = pos
        self.Index = index
        self.Connection = None

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
        if not(isinstance(connection, GraphConnections.BezierConnection)):
            print('Bad parametr in GraphPins::SetConnection')
            return
        self.Connection = connection

