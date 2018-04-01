import math

class Vec2:
    def __init__(self, x=0, y=0):
        self.X = x
        self.Y = y

    def Add(self,other):
        if type(other) == Vec2:
            self.X = self.X + other.X
            self.Y = self.Y + other.Y
        elif type(other) == float:
            self.X = self.X + other
            self.Y = self.Y + other
        else:
            print('Bad type in Vec2::Add')

        return self

    def Sub(self,other):
        if type(other) == Vec2:
            self.X = self.X - other.X
            self.Y = self.Y - other.Y
        elif type(other) == float:
            self.X = self.X - other
            self.Y = self.Y - other
        else:
            print('Bad type in Vec2::Sub')

        return self

    def Dot(self,other):
        if type(other) != Vec2:
            print('Bad type in Vec2::Dot')
            return
        return self.X * other.X + self.Y * other.Y

    def Length(self):
        return math.sqrt(self.X * self.X + self.Y * self.Y)

    def __mul__(self,other):
        if(type(other) == float):
            return Vec2(self.X * other, self.Y * other)
        elif type(other) == Vec2:
            return Vec2(self.X * other.X, self.Y * other.Y)
        else:
            print('Bad type in Vec2::__mul__')

    def __add__(self,other):
        if(type(other) == Vec2):
            return Vec2(self.X + other.X, self.Y + other.Y)
        elif type(other) == float:
            return Vec2(self.X + other, self.Y + other)
        else:
            print('Bad type in Vec2::__add__')

    def __sub__(self,other):
        if(type(other) == Vec2):
            return Vec2(self.X - other.X, self.Y - other.Y)
        elif type(other) == float:
            return Vec2(self.X - other, self.Y - other)
        else:
            print('Bad type in Vec2::__sub__')

    def __div__(self,other):
        if(type(other) == Vec2):
            return Vec2(self.X / other.X, self.Y / other.Y)
        elif type(other) == float:
            return Vec2(self.X / other, self.Y / other)
        else:
            print('Bad type in Vec2::__div__')