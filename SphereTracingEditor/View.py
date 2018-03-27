import tkinter as tk

class View:
    def __init__(self, width, height, title):
        self.MainWindow = tk.Tk()
        self.MainWindow.geometry(str(width) + 'x' + str(height))
        self.MainWindow.title(title);

        self.InitWidgets()

        self.MainWindow.after(16, self.CustomLoop) # Approximation of vsync
        self.MainWindow.mainloop()


    def InitWidgets(self):
        # Menu bar
        MenuBarHeight = 50

        self.MenuBar = tk.Frame(self.MainWindow, bg='#212121')
        self.MenuBar.pack(fill=tk.X, side=tk.TOP)
        self.MenuBar.configure(height=MenuBarHeight)

        # Graph
        self.Graph = tk.Frame(self.MainWindow, bg='#7c4dff')
        self.Graph.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.Graph.bind('<ButtonPress-1>', self.GraphLeftMousePressed)
        self.Graph.bind('<ButtonRelease-1>', self.GraphLeftMouseReleased)
        self.Graph.bind('<ButtonPress-2>', self.GraphScrollPressed)
        self.Graph.bind('<ButtonRelease-2>', self.GraphScrollReleased)
        self.Graph.bind('<ButtonPress-3>', self.GraphRightMousePressed)
        self.Graph.bind('<ButtonRelease-3>', self.GraphRightMouseReleased)

        # Settings
        SettingsWidth = 250

        self.Settings = tk.Frame(self.Graph)
        self.Settings.pack(side=tk.RIGHT, fill=tk.Y)
        self.Settings.configure(width=SettingsWidth)
        self.Settings.pack_propagate(0)

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


    def GraphLeftMousePressed(self,event):
        print('GraphLeftMouseClicked')

    def GraphLeftMouseReleased(self,event):
        print('GraphLeftMouseReleased')

    def GraphScrollPressed(self,event):
        print('GraphScrollPressed')

    def GraphScrollReleased(self,event):
        print('GraphScrollReleased')

    def GraphRightMousePressed(self,event):
        print('GraphRightMousePressed')

    def GraphRightMouseReleased(self,event):
        print('GraphRightMouseReleased')

    def NodeSettingsBtnClicked(self,event):
        print('NodeSettingsBtnClicked')

    def GlobalSettingsBtnClicked(self,event):
        print('GlobalSettingsBtnClicked')

    def CustomLoop(self):
        # Code here
        self.MainWindow.after(16, self.CustomLoop)
