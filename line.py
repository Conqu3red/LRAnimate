class Line:
        def __init__(self,ltype,identity,x1,y1,x2,y2,flipped=False,leftExtended=False,rightExtended=False,multiplier=0):
                self.id = identity
                self.type = ltype # 1,2,3 blue,red,green
                self.x1 = x1
                self.y1 = y1
                self.x2 = x2
                self.y2 = y2
                if flipped:
                        self.flipped = flipped
                if leftExtended:
                        self.leftExtended = leftExtended
                if rightExtended:
                        self.rightExtended = rightExtended
                if self.type == 1:
                        self.multiplier = multiplier

        def getLine(self,identifier):
                self.id = identifier
                return vars(self)
