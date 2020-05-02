import random, math, os, sys,json
from track import *
from line import *
import cv2
MAXRGBFORBLACK = 40
frames = []
vidcap = cv2.VideoCapture('test.mov')
success,image = vidcap.read()
count = 0
while success:
	#cv2.imwrite("%d.jpg" % count, image)	 # save frame as JPEG file	  
	frames.append(image)
	success,image = vidcap.read()
	print('Read a new frame: ', success)
	count += 1
# frames[frame][x][y]
# pixel
# 1,2,3 = red,green,blue
#print(frames[0][20][30])
track = Track()
c = 0
PIXELWIDTH = 1
OFFSET = 0
width = len(frames[0])
height = len(frames[0][0])
print(width, height)
for n,frame in enumerate(frames):
	for x,row in enumerate(frame):
		for y,pixel in enumerate(row):
			if pixel[0] < MAXRGBFORBLACK and pixel[1] < MAXRGBFORBLACK and pixel[2] < MAXRGBFORBLACK:
				#print(x,y)
				x1 = x + OFFSET - PIXELWIDTH/2
				y1 = y + PIXELWIDTH/2
				x2 = x + OFFSET - PIXELWIDTH/2
				y2 = y - PIXELWIDTH/2
				track.addLine(Line(2,c,x1,y1,x2,y2,False,False,False))
				c += 1
	OFFSET += width+1000
	print(f"Completed Frame {n}")
	STARTSPEED = 0.4

	# multiplier 2 : x1.45
	# multiplier 4 : x


def getLines(img):
		start = 0
		end = 0
		ret = []
		ls = False
		for x in range(self.image.width):
			if ls == True:
				ret.append((start,end))
				ls = False
			for y in range(self.image.height):
				if self.data[x,y] == 0:
					if ls == False:
						ls = True
						start = x,y
						end = x,y
					else:
						end = x,y
						
				elif self.data[x,y] == 255 and ls == True:
					ret.append((start,end))
					ls = False

		return ret



track.addLine(Line(0,c, -50, height, 0, height, False,False,False))
track.addLine(Line(0,c+1, 0, height, OFFSET, height, False,False,False))
#track.addLine(Line(1,c+2, -50, height, 10, height, False,False,False,2))

track.data["startPosition"] = {"x":-50,"y":height-5}
track.data["riders"][0]["startPosition"] = {"x":-50,"y":height-5}
track.data["riders"][0]["startVelocity"] = {"x":width+1000,"y":0}
track.saveTrack("test")