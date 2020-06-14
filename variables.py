from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import*
from math import*
import numpy as np
import pygame

width=600
hight=600
p=1
ytransfer = 1.05
randx = 0
randi = 0
xtransfer = 0
name = "Z"
bedgep = .95
redgep = .15
ledgep = -.15
sright = False
sleft = False
sbottom = False
flagt = False
flagl = True
flagr = True
keys={'w':False,'d':False,'a':False,'f':False,'u':False,'j':False,"up":False,"down":False,"enter":False,"escape":False,'p':False}
started=False
options=False
credits=False
sound=True
paused=False
fin=False
objList =[]
score = 30000

