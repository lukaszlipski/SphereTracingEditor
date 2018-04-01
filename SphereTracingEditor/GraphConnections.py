from CustomMath import Vec2
import tkinter as tk
import math

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
        
        MiddlePoint = (self.Start + self.End) * 0.5

        Offset1 = Vec2(0,1) * ((MiddlePoint - self.Start).Dot(Vec2(0,1)))
        Offset2 = Vec2(0,1) * ((MiddlePoint - self.End).Dot(Vec2(0,1)))

        Point1 = MiddlePoint - Offset1
        Point2 = MiddlePoint - Offset2
        
        for t in range(1, self.SamplesNum):
            pointA = self.BezierCurve(self.Start, Point1, Point2, self.End, (t-1)/self.SamplesNum)
            pointB = self.BezierCurve(self.Start, Point1, Point2, self.End, t/self.SamplesNum)
            self.Canvas.create_line(pointA.X,pointA.Y,pointB.X,pointB.Y, width = self.LineWidth, tag = 'Connection' + str(id(self)) )
            

    def Clear(self):
        self.Canvas.delete( 'Connection' + str(id(self)) )
