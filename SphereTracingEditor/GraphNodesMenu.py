import tkinter as tk
import GraphNodes

class GraphNodesMenu:
    def __init__(self, owner, pos):
        self.Owner = owner
        self.Pos = pos
        self.InitWidgets()
        self.InitEvents()

    def InitWidgets(self):
        self.MainMenu = tk.Frame(self.Owner.Graph, bg='blue')
        self.MainMenu.pack()
        self.MainMenu.configure(width=100,height=200)
        self.MainMenu.place_configure(x=self.Pos.X,y=self.Pos.Y)

        # Text box
        self.Filter = tk.StringVar()
        self.Filter.trace('w', lambda name,index,sv: self.Update())
        self.TextBox = tk.Entry(self.MainMenu,textvariable=self.Filter)
        self.TextBox.pack(fill=tk.X)

        # Nodes
        self.Nodes = tk.Listbox(self.MainMenu)
        self.Nodes.pack(side=tk.LEFT)
        self.Scrollbar = tk.Scrollbar(self.MainMenu)
        self.Scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.Nodes.config(yscrollcommand=self.Scrollbar.set)
        self.Scrollbar.config(command=self.Nodes.yview)

        self.Update()
        

    def InitEvents(self):
        self.Nodes.bind('<<ListboxSelect>>', lambda event: self.Owner.NodesMenuSelected(self.Nodes.selection_get()))


    def Update(self):
        self.Nodes.delete(0,tk.END)
        for i in GraphNodes.GraphNode.GetChildren():
            if i.__name__.lower().find(self.Filter.get().lower()) != -1:
                self.Nodes.insert(tk.END, i.__name__)


    def Delete(self):
        self.MainMenu.destroy()
