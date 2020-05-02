import json, math
from line import *
# {"label":"4 a","duration":0,"version":"6.2","audio":null,"startPosition":{"x":0,"y":0},"
#riders":[{"startPosition":{"x":0,"y":0},"startVelocity":{"x":0.4,"y":0}}],"layers":[{"id":0,"name":"Base Layer","visible":true}],
#"lines":[{"id":1,"type":1,"x1":-32.31791622146133,"y1":21.875897824843804,"x2":55.36955450614016,"y2":15.527483654519699,"flipped":false,"leftExtended":false,"rightExtended":false,"multiplier":3}]}
class Track:
        def __init__(self):
                self.linesTemp = []
                self.data = {"label":"EXAMPLE",
                        "creator":"EXAMPLE",
                        "description":"EXAMPLE",
                        "duration":0,
                        "version":"6.2",
                        "startPosition":{"x":0,"y":0},
                        "riders":[{"startPosition":{"x":-50,"y":471},"startVelocity":{"x":0.4,"y":0}}],
                        "layers":[{"id":0,"name":"Base Layer","visible":True}],
                        "lines":[]}

        def setSpawn(self,x,y):
                self.data["startPosition"]["x"] = x
                self.data["startPosition"]["y"] = y

        def addLine(self,line):
                self.linesTemp.append(line)

        def translate(self,x_shift,y_shift):
                # NOT USED - Doesn't work
                done = 0
                needed = len(self.lines)
                templines = []
                for num,line in enumerate(self.lines):
                        #self.lines.remove(line)
                        current = list(line.getLine(num).values())
                        print(current)
                        current[2],current[4] = current[2]+x_shift, current[4]+x_shift
                        current[3],current[5] = current[3]+y_shift, current[5]+y_shift
                        current = list(current)
                        print(current)
                        #print(current)
                        templines.append(Line(*current))
                        done += 1
                        
                        if done == needed:
                                break
                self.lines = templines

        def saveTrack(self,name):
                with open(name+".json", "w+") as file:
                        for num,line in enumerate(self.linesTemp):
                                self.data['lines'].append(line.getLine(num))
                        json.dump(self.data,file)


