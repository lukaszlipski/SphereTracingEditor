from CustomMath import Vec2
import tkinter as tk
import math
import GraphPins

class BezierConnection:
    def __init__(self, canvas, start=Vec2(), end=Vec2()):

        if type(canvas) != tk.Canvas:
            print('Bad parameter for GraphConnection::Draw')
            return 

        self.Start = start
        self.End = end
        self.Canvas = canvas

        self.SamplesNum = 20
        self.LineWidth = 3
               


    def SetStart(self, start):
        self.Start = start

    def SetEnd(self, end):
        self.End = end

  
    def BezierCurve(self,p1,p2,p3,p4,t):
        k1 = math.pow((1-t),3)
        k2 = 3*math.pow(1-t,2) * t
        k3 = 3*(1-t) * math.pow(t,2)
        k4 = math.pow(t,3)

        return p1 * k1 + p2 * k2 + p3 * k3 + p4 * k4 


    def Draw(self):
        
        StartPos = 0
        EndPos = 0

        if isinstance(self.Start, Vec2):
            StartPos = self.Start
        elif isinstance(self.Start, GraphPins.GraphPin):
            StartPos = self.Start.GetPos(self.Canvas)
        else:
            return

        if isinstance(self.End, Vec2):
            EndPos = self.End
        elif isinstance(self.End, GraphPins.GraphPin):
            EndPos = self.End.GetPos(self.Canvas)
        else:
            return

        MiddlePoint = (StartPos + EndPos) * 0.5
        
        Offset1 = Vec2(0,1) * ((MiddlePoint - StartPos).Dot(Vec2(0,1)))
        Offset2 = Vec2(0,1) * ((MiddlePoint - EndPos).Dot(Vec2(0,1)))

        Point1 = MiddlePoint - Offset1
        Point2 = MiddlePoint - Offset2
        
        for t in range(1, self.SamplesNum+1):
            pointA = self.BezierCurve(StartPos, Point1, Point2, EndPos, (t-1)/self.SamplesNum)
            pointB = self.BezierCurve(StartPos, Point1, Point2, EndPos, t/self.SamplesNum)
            self.Canvas.create_line(pointA.X,pointA.Y,pointB.X,pointB.Y, width = self.LineWidth, tag = 'Connection' + str(id(self)) )
            

    def Clear(self):
        self.Canvas.delete( 'Connection' + str(id(self)) )


    def Remove(self):
        if isinstance(self.Start, GraphPins.GraphPin):
            self.Start.RemoveConnection(self)
        if isinstance(self.End, GraphPins.GraphPin):
            self.End.RemoveConnection(self)
        self.Clear()

    def CheckConnection(self, nodeA, nodeB):
        Result = False
        if nodeA == self.Start and nodeB == self.End:
            Result = True
        if nodeB == self.Start and nodeA == self.End:
            Result = True
        return Result

