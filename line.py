class Line:
        def __init__(self,ltype,identity,x1,y1,x2,y2,flipped,leftExtended,rightExtended,multiplier=0):
                self.type = ltype
                self.id = identity
                self.x1 = x1
                self.y1 = y1
                self.x2 = x2
                self.y2 = y2
                self.flipped = flipped
                self.leftExtended = leftExtended
                self.rightExtended = rightExtended
                if self.id == 1:
                        self.multiplier = multiplier

        def getLine(self,identifier):
                self.id = identifier
                return vars(self)
