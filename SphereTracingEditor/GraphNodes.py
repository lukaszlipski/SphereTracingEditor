from CustomMath import Vec2
import GraphPins
import tkinter as tk

class GraphNode:

    def __init__(self, view, x=0, y=0):

        self.SideExtend = 10
        self.LabelExtend = 20
        self.ImageSize = 80

        self.Pos = Vec2(x,y)
        self.Owner = view

        self.InputPins = []
        self.OutputPins = []

        self.PinOffset = 15

        Width = self.ImageSize
        Height = self.LabelExtend + self.ImageSize

        if self.CanHaveInputs:
            Width = Width + self.SideExtend

        if self.CanHaveOuputs:
            Width = Width + self.SideExtend

        self.Size = Vec2( Width , Height )

        self.InitWidgets();
        

    def InitWidgets(self):

        self.MainWidget = tk.Frame(self.Owner.Graph, bg='red')
        self.MainWidget.place_configure(x=self.Pos.X,y=self.Pos.Y)
        self.MainWidget.configure(width=self.Size.X,height=self.Size.Y)
        self.MainWidget.pack_propagate(0)

        # Set owner
        self.MainWidget.Owner = self

        # Label with name
        self.NameLabel = tk.Label(self.MainWidget, text=self.Name)
        self.NameLabel.pack(fill=tk.X)
        self.NameLabel.bind('<ButtonPress-1>', lambda event: self.Owner.NodeLeftMousePressed(self))
        self.NameLabel.bind('<ButtonRelease-1>', lambda event: self.Owner.NodeLeftMouseReleased(self))

        # Node
        self.Node = tk.Frame(self.MainWidget, bg='blue')
        self.Node.pack(fill=tk.BOTH, expand=True)

        # Inputs
        if self.CanHaveInputs:
            self.InputsWidget = tk.Frame(self.Node, bg='pink')
            self.InputsWidget.pack(side=tk.LEFT, fill=tk.Y, expand=False)
            self.InputsWidget.configure(width=self.SideExtend)

            for i in range(0,self.InputsNum):
                CurrentHeight = self.ImageSize/2 - (self.InputsNum/2 * self.PinOffset) + (i * self.PinOffset) + GraphPins.GraphPin.Size.Y/2
                self.InputPins.append(GraphPins.GraphInputPin(self, i, self.InputsWidget, Vec2(0,CurrentHeight)))

        # Image
        self.Image = tk.Frame(self.Node, bg='black')
        self.Image.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.Image.configure(width=self.ImageSize, height=self.ImageSize)

        # Outputs
        if self.CanHaveOuputs:
            self.OutputsWidget = tk.Frame(self.Node, bg='pink')
            self.OutputsWidget.pack(side=tk.RIGHT, fill=tk.Y, expand=False)
            self.OutputsWidget.configure(width=self.SideExtend)

            for i in range(0,self.OutputsNum):
                CurrentHeight = self.ImageSize/2 - (self.OutputsNum/2 * self.PinOffset) + (i * self.PinOffset) + GraphPins.GraphPin.Size.Y/2
                self.OutputPins.append(GraphPins.GraphOutputPin(self, i, self.OutputsWidget, Vec2(0,CurrentHeight)))

            

    def ChangePos(self, offset):
        self.Pos.Sub(offset)
        self.MainWidget.place_configure(x=self.Pos.X, y=self.Pos.Y)

    def NodePinLeftMousePressed(self, pin):
        self.Owner.NodePinLeftMousePressed(self, pin)

    def NodePinLeftMouseReleased(self, pin):
        self.Owner.NodePinLeftMouseReleased(self, pin)

    def IsValid(self):
        if self.CanHaveInputs:
            for input in self.InputPins:
                if not input.IsConnected():
                    return False
        return True


    def Delete(self):
        for input in self.InputPins:
            input.RemoveAllConnections()

        for output in self.OutputPins:
            output.RemoveAllConnections()

        self.MainWidget.destroy()

    def GetNodeSize(self):
        SizeX = self.ImageSize
        if self.CanHaveInputs:
            SizeX = SizeX + self.SideExtend
        if self.CanHaveOuputs:
            SizeX = SizeX + self.SideExtend

        SizeY = self.ImageSize
        SizeY = SizeY + self.LabelExtend
        return Vec2(SizeX,SizeY)

    @staticmethod
    def GetChildren():
        return GraphNode.__subclasses__()


class Sphere(GraphNode):
    def __init__(self, view, x = 0, y = 0):

        self.Name = 'Sphere'
        self.InputsNum = 2
        self.OutputsNum = 1
        self.CanHaveInputs = False;
        self.CanHaveOuputs = True;

        super().__init__(view, x, y)
 
        
class Box(GraphNode):
    def __init__(self, view, x = 0, y = 0):

        self.Name = 'Box'
        self.InputsNum = 2
        self.OutputsNum = 1
        self.CanHaveInputs = False;
        self.CanHaveOuputs = True;

        super().__init__(view, x, y)


class Intersect(GraphNode):
    def __init__(self, view, x = 0, y = 0):

        self.Name = 'Intersect'
        self.InputsNum = 2
        self.OutputsNum = 1
        self.CanHaveInputs = True;
        self.CanHaveOuputs = True;

        super().__init__(view, x, y)


class Union(GraphNode):
    def __init__(self, view, x = 0, y = 0):

        self.Name = 'Union'
        self.InputsNum = 2
        self.OutputsNum = 1
        self.CanHaveInputs = True;
        self.CanHaveOuputs = True;

        super().__init__(view, x, y)


class Subtract(GraphNode):
    def __init__(self, view, x = 0, y = 0):

        self.Name = 'Subtract'
        self.InputsNum = 2
        self.OutputsNum = 1
        self.CanHaveInputs = True;
        self.CanHaveOuputs = True;

        super().__init__(view, x, y)