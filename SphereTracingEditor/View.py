import tkinter as tk
import GraphNodes
import Controller
from CustomMath import Vec2
import GraphConnections

class View:
    def __init__(self, controller, width, height, title):
        self.Controller = controller

        self.MainWindow = tk.Tk()
        self.MainWindow.geometry(str(width) + 'x' + str(height))
        self.MainWindow.title(title);
        
        self.Nodes = []

        self.InitWidgets()
        self.InitEvents()


    def Run(self):
        self.MainWindow.after(16, self.CustomLoop) # Approximation of vsync
        self.MainWindow.mainloop()


    def InitWidgets(self):
        # Menu bar
        MenuBarHeight = 50

        self.MenuBar = tk.Frame(self.MainWindow, bg='#212121')
        self.MenuBar.pack(fill=tk.X, side=tk.TOP)
        self.MenuBar.configure(height=MenuBarHeight)

        # Editor
        self.Editor = tk.Frame(self.MainWindow)
        self.Editor.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)

        # Settings
        SettingsWidth = 250

        self.Settings = tk.Frame(self.Editor)
        self.Settings.pack(side=tk.RIGHT, fill=tk.Y)
        self.Settings.configure(width=SettingsWidth)
        self.Settings.pack_propagate(0)

        # Graph
        self.Graph = tk.Canvas(self.Editor, bg='#7c4dff')
        self.Graph.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # Settings menu
        SettingsMenuHeight = 30

        self.SettingsMenu = tk.Frame(self.Settings, bg='#b3e5fc')
        self.SettingsMenu.pack(side=tk.TOP, fill=tk.X)
        self.SettingsMenu.configure(height=SettingsMenuHeight)

        # Settings properties
        self.SettingsProperties = tk.Frame(self.Settings, bg='#757575')
        self.SettingsProperties.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # Settings buttons
        self.NodeSettingsBtn = tk.Button(self.SettingsMenu, text='Node')
        self.NodeSettingsBtn.grid(row=0,column=0, padx=5, pady=5)
        self.NodeSettingsBtn.bind('<Button-1>', self.NodeSettingsBtnClicked)

        self.GlobalSettingsBtn = tk.Button(self.SettingsMenu, text='Global')
        self.GlobalSettingsBtn.grid(row=0,column=1, padx=5)
        self.GlobalSettingsBtn.bind('<Button-1>', self.GlobalSettingsBtnClicked)


    def InitEvents(self):
        self.Graph.bind('<ButtonPress-1>', self.GraphLeftMousePressed)
        self.Graph.bind('<ButtonRelease-1>', self.GraphLeftMouseReleased)
        self.Graph.bind('<ButtonPress-2>', self.GraphScrollPressed)
        self.Graph.bind('<ButtonRelease-2>', self.GraphScrollReleased)
        self.Graph.bind('<ButtonPress-3>', self.GraphRightMousePressed)
        self.Graph.bind('<ButtonRelease-3>', self.GraphRightMouseReleased)


    def GetMousePos(self):
        x = self.Graph.winfo_pointerx() - self.Graph.winfo_rootx()
        y = self.Graph.winfo_pointery() - self.Graph.winfo_rooty()
        return Vec2(x,y)


    def CreateNode(self, x=0, y=0):
        self.Nodes.append(GraphNodes.GraphNode(self, x, y))

    def NodeLeftMousePressed(self, node):
        self.Controller.NodeLeftMousePressed(node)

    def NodeLeftMouseReleased(self, node):
        self.Controller.NodeLeftMouseReleased(node)

    def NodeInputLeftMousePressed(self, node):
        self.Controller.NodeInputLeftMousePressed(node)

    def NodeInputLeftMouseReleased(self, node):
        self.Controller.NodeInputLeftMouseReleased(node)

    def NodeOutputLeftMousePressed(self, node):
        self.Controller.NodeOutputLeftMousePressed(node)

    def NodeOutputLeftMouseReleased(self, node):
        self.Controller.NodeOutputLeftMouseReleased(node)

    def GraphLeftMousePressed(self,event):
        print('GraphLeftMousePressed')

    def GraphLeftMouseReleased(self,event):
        print('GraphLeftMouseReleased')

    def GraphScrollPressed(self,event):
        print('GraphScrollPressed')

    def GraphScrollReleased(self,event):
        print('GraphScrollReleased')

    def GraphRightMousePressed(self,event):
        self.Controller.GraphLeftMousePressed()

    def GraphRightMouseReleased(self,event):
        print('GraphRightMouseReleased')

    def NodeSettingsBtnClicked(self,event):
        print('NodeSettingsBtnClicked')

    def GlobalSettingsBtnClicked(self,event):
        print('GlobalSettingsBtnClicked')

    def CustomLoop(self):
        # Code here
        self.Controller.Update()
        self.MainWindow.after(16, self.CustomLoop)
