import random, math, os, sys,json
from track import *
from line import *
import cv2, os
from PIL import Image
MAXRGBFORBLACK = 40
# VIDEOS ARE SOMETIMES ROTATED WRONG/FLIPPED - NEED TO FIX
print("Welcome to LRAnimate!")
#print("WARNING! Ideally only input .mov files as .mp4 files end up with the wrong orientation and mirrored!")
filename = input("Please type the name of your video file: ")
width_scaling = int(input("please enter the pixel width your would like x to be (recommended 100): "))
distance = int(input("Please enter distance between frames (recomend 1000 but up to you): "))

def getLines(img,width,height):
		start = 0
		end = 0
		ret = []
		ls = False
		for x in range(width):
			if ls == True:
				ret.append((start,end))
				ls = False
			for y in range(height):
				if img.getpixel((x,y))[0] < MAXRGBFORBLACK and img.getpixel((x,y))[1] < MAXRGBFORBLACK and img.getpixel((x,y))[2] < MAXRGBFORBLACK:
					if ls == False:
						ls = True
						start = x,y
						end = x,y
					else:
						end = x,y
						
				elif img.getpixel((x,y))[0] > MAXRGBFORBLACK and img.getpixel((x,y))[1] > MAXRGBFORBLACK and img.getpixel((x,y))[2] > MAXRGBFORBLACK and ls == True:
					ret.append((start,end))
					ls = False

		return ret







frame = ""
track = Track()
c = 0
PIXELWIDTH = 1
OFFSET = 0
vidcap = cv2.VideoCapture(filename)
success,img = vidcap.read()
#print((os.path(filename)))

frame = img
	
frame = Image.fromarray(frame)
if width_scaling == 0:
	width_scaling = frame.width
width = frame.width
SCALE = width_scaling/width
width_s = width*SCALE
height = frame.height
height_s = height*SCALE



count = 0
while success:
	#cv2.imwrite("%d.jpg" % count, image)	 # save frame as JPEG file	  
	frame = img
	
	frame = Image.fromarray(frame)
	#print(frame.getpixel((1,2)))

	width = frame.width
	SCALE = width_scaling/width
	width_s = width*SCALE
	height = frame.height
	height_s = height*SCALE
	#print(width,height)
	PIXELWIDTH = SCALE/width
	#print(width, height)
	#l = getLines(frame, width, height)
	
	if count == 0:
		OFFSET += width_s+distance
	lines = getLines(frame,width,height)
#	for x,row in enumerate(frame):
#		for y,pixel in enumerate(row):
#			if pixel[0] < MAXRGBFORBLACK and pixel[1] < MAXRGBFORBLACK and pixel[2] < MAXRGBFORBLACK:
#				#print(x,y)
#				x1 = x*SCALE + OFFSET - PIXELWIDTH/2
#				y1 = y*SCALE + PIXELWIDTH/2
#				x2 = x*SCALE + OFFSET - PIXELWIDTH/2
#				y2 = y*SCALE - PIXELWIDTH/2
#				#track.addLine(Line(2,c,x1,y1,x2,y2,False,False,False))
	
	#track.addLine(Line(2,c,x1,y1,x2,y2,False,False,False))
	for n,ln in enumerate(lines):
		x1 = ln[0][0]*SCALE + OFFSET
		y1 = ln[0][1]*SCALE
		x2 = ln[1][0]*SCALE + OFFSET
		y2 = ln[1][1]*SCALE
		track.addLine(Line(2,n,x1,y1,x2,y2))
		c += 1
	c += 1
	OFFSET += width_s+distance
	print(f"Frame {count}  Total Lines: {c}")




	success,img = vidcap.read()
	#print('Read a new frame: ', success)
	count += 1

# pixel
# 1,2,3 = red,green,blue
#print(frames[0][20][30])




track.addLine(Line(0,c, -50, height_s, 0, height_s, False,False,False))
track.addLine(Line(0,c+1, 0, height_s, OFFSET, height_s, False,False,False))
#track.addLine(Line(1,c+2, -50, height, 10, height, False,False,False,2))

track.data["startPosition"] = {"x":-50,"y":height-5}
track.data["riders"][0]["startPosition"] = {"x":-50,"y":height_s-5}
track.data["riders"][0]["startVelocity"] = {"x":width_s+distance,"y":0}
track.saveTrack(filename)

print(f"Track Saved as {filename}.json")