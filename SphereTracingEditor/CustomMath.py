
class Vec2:
    def __init__(self, x=0, y=0):
        self.X = x
        self.Y = y

    def Add(self,other):
        self.X = self.X + other.X
        self.Y = self.Y + other.Y
        return self

    def Sub(self,other):
        self.X = self.X - other.X
        self.Y = self.Y - other.Y
        return self