import random, math, os, sys,json
from track import *
from line import *
import cv2
MAXRGBFORBLACK = 40
frame = ""
track = Track()
c = 0
PIXELWIDTH = 1
OFFSET = 0
vidcap = cv2.VideoCapture('test.mov')
success,image = vidcap.read()
count = 0
while success:
	#cv2.imwrite("%d.jpg" % count, image)	 # save frame as JPEG file	  
	frame = image
	width = len(frame)
	SCALE = 100/width
	width = width*SCALE
	height = len(frame[0])
	height = height*SCALE
	#print(width,height)
	PIXELWIDTH = SCALE/width
	#print(width, height)
	if count == 0:
		OFFSET += width+1000
	for x,row in enumerate(frame):
		for y,pixel in enumerate(row):
			if pixel[0] < MAXRGBFORBLACK and pixel[1] < MAXRGBFORBLACK and pixel[2] < MAXRGBFORBLACK:
				#print(x,y)
				x1 = x*SCALE + OFFSET - PIXELWIDTH/2
				y1 = y*SCALE + PIXELWIDTH/2
				x2 = x*SCALE + OFFSET - PIXELWIDTH/2
				y2 = y*SCALE - PIXELWIDTH/2
				track.addLine(Line(2,c,x1,y1,x2,y2,False,False,False))
				c += 1
	OFFSET += width+1000
	print(f"Completed Frame {count}")





	success,image = vidcap.read()
	#print('Read a new frame: ', success)
	count += 1

# pixel
# 1,2,3 = red,green,blue
#print(frames[0][20][30])




track.addLine(Line(0,c, -50, height, 0, height, False,False,False))
track.addLine(Line(0,c+1, 0, height, OFFSET, height, False,False,False))
#track.addLine(Line(1,c+2, -50, height, 10, height, False,False,False,2))

track.data["startPosition"] = {"x":-50,"y":height-5}
track.data["riders"][0]["startPosition"] = {"x":-50,"y":height-5}
track.data["riders"][0]["startVelocity"] = {"x":width+1000,"y":0}
track.saveTrack("test")