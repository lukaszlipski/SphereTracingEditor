from CustomMath import Vec2
import GraphPins
import tkinter as tk

class GraphNode(tk.Frame):

    def __init__(self, view, x=0, y=0):

        self.SideExtend = 10
        self.LabelExtend = 20
        self.ImageSize = 80

        self.Pos = Vec2(x,y)
        self.Owner = view
        self.Name = 'Not specified'

        self.CanHaveInputs = True;
        self.CanHaveOuputs = True;

        self.InputsNum = 1
        self.OutputsNum = 4

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
            self.Inputs = tk.Frame(self.Node, bg='pink')
            self.Inputs.pack(side=tk.LEFT, fill=tk.Y, expand=False)
            self.Inputs.configure(width=self.SideExtend)

            for i in range(0,self.InputsNum):
                CurrentHeight = self.ImageSize/2 - (self.InputsNum/2 * self.PinOffset) + (i * self.PinOffset) + GraphPins.GraphPin.Size.Y/2
                GraphPins.GraphPin(self, self.Inputs, Vec2(0,CurrentHeight))

        # Image
        self.Image = tk.Frame(self.Node, bg='red')
        self.Image.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.Image.configure(width=self.ImageSize, height=self.ImageSize)

        # Outputs
        if self.CanHaveOuputs:
            self.Outputs = tk.Frame(self.Node, bg='pink')
            self.Outputs.pack(side=tk.RIGHT, fill=tk.Y, expand=False)
            self.Outputs.configure(width=self.SideExtend)

            for i in range(0,self.OutputsNum):
                CurrentHeight = self.ImageSize/2 - (self.OutputsNum/2 * self.PinOffset) + (i * self.PinOffset) + GraphPins.GraphPin.Size.Y/2
                GraphPins.GraphPin(self, self.Outputs, Vec2(0,CurrentHeight))

            


    def ChangePos(self, offset):
        self.Pos.Sub(offset)
        self.MainWidget.place_configure(x=self.Pos.X, y=self.Pos.Y)

    def NodePinLeftMousePressed(self, pin):
        print('NodePinLeftMousePressed')

    def NodePinLeftMouseReleased(self, pin):
        print('NodePinLeftMouseReleased')
