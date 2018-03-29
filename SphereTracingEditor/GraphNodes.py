from CustomMath import Vec2
import tkinter as tk

class GraphNode:

    def __init__(self, view, x=0, y=0):
        self.Pos = Vec2(x,y)
        self.Size = Vec2(75,100)
        self.Owner = view
        self.InitWidgets();
        

    def InitWidgets(self):
        self.MainWidget = tk.Frame(self.Owner.Graph, bg='red')
        self.MainWidget.place_configure(x=self.Pos.X,y=self.Pos.Y)
        self.MainWidget.configure(width=self.Size.X,height=self.Size.Y)
        self.MainWidget.bind('<ButtonPress-1>', lambda event: self.Owner.NodeLeftMousePressed(self))
        self.MainWidget.bind('<ButtonRelease-1>', lambda event: self.Owner.NodeLeftMouseReleased(self))


    def ChangePos(self, offset):
        self.Pos.Sub(offset)
        self.MainWidget.place_configure(x=self.Pos.X, y=self.Pos.Y)
