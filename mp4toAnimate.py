import random, math, os, sys,json
from track import *
from line import *
import skvideo.io
videodata = skvideo.io.vread("a.mov")  
print(videodata.shape)