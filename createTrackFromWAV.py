import random, math, os, sys,json
from track import *
from line import *
from tkinter import *
from tkinter.filedialog import *
tk=Tk()
tracks_dir = askdirectory(title='Please select the location of your LRA tracks folder')
wav_location = askopenfilename(title='Select a .wav file', filetypes = (("wav files","*.wav"),("all files","*.*")))
tk.destroy()
os.chdir(tracks_dir)
"""
IMPORTANT
json format (per line)
[l_type, id, x1, y1, x2, y2, 0, false]
l_type - line type (0=normal, 1=red, 2=green)
id - unique line identefier
x, y - coords of line points [line joins from point (x1,y1) to (x2,y2)]

Co-ordinate grid:
            y-
            |
            |
            |
            |
x- ---------+--------- x+   x axis
            |
            |
            |
            |
            y+
          y axis



Speeds - red
line len | speed (p/f)
100         5.95
200         8.62
300        10.57
400        12.25
500        13.73
1000       19.51
"""
import soundfile as sf
data, samplerate = sf.read(wav_location)
print(samplerate)
channels = 2
try:
	print(len(data[0]))
except:
	channels = 1
	pass
#print(channels)
track_name = input("Please enter a track name: ")
name = input("Please enter a save name: ")
#number_of_lines = int(input("Enter the number of lines to be Created: "))
#minlength = int(input("Enter minimum line length: "))
#length = int(input("Enter maximum line length: "))
#height = int(int(input("Enter maximum line height: "))/2)
try:
    # Create target Directory
    os.mkdir(track_name)
except FileExistsError:
    pass
#print(data[0])
os.chdir(track_name)
if channels == 1:
	x1,y1,x2,y2 = 0,0,0,(data[0])*200
elif channels == 2:
	x1,y1,x2,y2 = 0,0,0,(data[0][0])*200

track = Track()
c = 0
for a,line in enumerate(data):
	prevx,prevy = x2,y2
	x1,y1,x2,y2 = 0,0,0,0
	x1 += prevx
	x2 += c
	y1 += prevy
	if channels == 1:
		y2 += line*200
	elif channels == 2:
		y2 += ((line[0]+line[1])/2)*200

	#print(randnum)
	track.addLine(Line(2,c,x1,y1,x2,y2,0,False))
	c += 1
track.addLine(Line(0,len(data),0,0,len(data),0,0,False))
speedup_distance = 0.44
#start_speed = 0.44
#while speedup_distance < bitrate:
#	speedup

track.addLine(Line(1,len(data)+1,-6700,0,0,0,0,False))
track.setSpawn(-6700,-5)
#toWrite = toWrite[:-1]

track.saveTrack(name)
print("Done!")
#read = open(name, "r").read()

#print("File contents: \n\n" + str(read))