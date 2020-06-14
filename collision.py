from variables import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import*
from math import*
import numpy as np
import pygame
from random import randint

# convert from windows cordinates to secreen cordenate so that we can use mouse cordinate in the code
def W_2_s (x,y):
    global width,hight
    xa=-1-x
    y*=-1
    ya=1-y
    xa=ceil(abs(xa/2)*width)
    ya=ceil(abs(ya/2)*hight)
    alist=[xa,ya]
    return alist


def collision():
    xvar = []
    yvar = []
    x=0
    y=0
    global name,randx,sright,sleft,sbottom,redgep,ledgep,bedgep
    right = redgep
    left = ledgep
    bottom = bedgep
    ## o shape
    if name == 'O':
        ##bottom
        xvar = (GLubyte * 1)(0)
        x,y = W_2_s(right-.05, bottom+.01)
        glReadPixels(x,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
        if xvar[0]!=51:
            sbottom = True
        else:
            xvar = (GLubyte * 1)(0)
            x, y = W_2_s(left + .05, bottom+.01)
            glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0] != 51:
                sbottom = True
            else:
                sbottom = False
        ##right
        yvar = (GLubyte * 1)(0)
        x, y = W_2_s(right+.01, bottom+.1)
        glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
        if yvar[0] != 51:
            sright = True
        else:
            sright = False

        ## left
        yvar = (GLubyte * 1)(0)
        x,y = W_2_s(left-.01, bottom + .1)
        glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
        if yvar[0] != 51:
            sleft = True
        else:
            sleft = False

            ##shapes##
    ## i shape
    if name =='I':
        ##bottom
        if randx == 0 or randx == 2:
            xvar = (GLubyte * 1)(0)
            x,y = W_2_s(right - .05, bottom)
            glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0]!=51:
                sbottom = True
        else:
            xvar = (GLubyte * 1)(0)
            x,y = W_2_s(right - 0.15, bottom)
            glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0] != 51:
                sbottom = True
            else:
                xvar = (GLubyte * 1)(0)
                x,y = W_2_s(right - 0.05, bottom)
                glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                if xvar[0] != 51:
                    sbottom = True
                else:
                    xvar = (GLubyte * 1)(0)
                    x,y= W_2_s(left + 0.05, bottom)
                    glReadPixels(x,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                    if xvar[0] != 51:
                        sbottom = True
                    else:
                        xvar = (GLubyte * 1)(0)
                        x,y = W_2_s(left + 0.15, bottom)
                        glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                        if xvar[0] != 51:
                            sbottom = True
        ##right
        if randx == 0 or randx == 2:
            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(right, bottom + 0.05)
            glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0]!=51:
                sright = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(right, bottom + 0.15)
                glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sright = True
                else:
                    yvar = (GLubyte * 1)(0)
                    x,y = W_2_s(right, bottom + 0.25)
                    glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                    if yvar[0] != 51:
                        sright = True
                    else:
                        yvar = (GLubyte * 1)(0)
                        x,y = W_2_s(right, bottom + 0.35)
                        glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                        if yvar[0] != 51:
                            sright = True
        else:
            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(right, bottom + 0.05)
            glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sright = True
        ##left
        if randx == 0 or randx == 2:
            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(left, bottom + 0.05)
            glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sleft = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(left, bottom + 0.15)
                glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    left = True
                else:
                    yvar = (GLubyte * 1)(0)
                    x,y = W_2_s(left, bottom + 0.25)
                    glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                    if yvar[0] != 51:
                        sleft = True
                    else:
                        yvar = (GLubyte * 1)(0)
                        x,y = W_2_s(left, bottom + 0.35)
                        glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                        if yvar[0] != 51:
                            sleft = True
        else:
            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(left, bottom + 0.05)
            glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sleft = True
    ## T shape
    if name =='T':
        ##bottom
        if randx == 0:
            xvar = (GLubyte * 1)(0)
            x,y = W_2_s(right -.15,bottom)
            glReadPixels(x,y+2 , 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0]!=51:
                sbottom = True
            else:
                xvar = (GLubyte * 1)(0)
                x,y = W_2_s(right - .05, bottom+.1)
                glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                if xvar[0] != 51:
                    sbottom = True
                else:
                    xvar = (GLubyte * 1)(0)
                    x,y = W_2_s(left + .05, bottom + .1)
                    glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                    if xvar[0] != 51:
                        sbottom = True
        elif randx == 1:
            xvar = (GLubyte * 1)(0)
            x,y = W_2_s(left + .05, bottom)
            glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0] != 51:
                sbottom = True
            else:
                xvar = (GLubyte * 1)(0)
                x,y =W_2_s(right - .05, bottom + .1)
                glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                if xvar[0] != 51:
                    sbottom = True
        elif randx == 2:
            xvar = (GLubyte * 1)(0)
            x,y = W_2_s(left + .05, bottom)
            glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0] != 51:
                sbottom = True
            else:
                xvar = (GLubyte * 1)(0)
                x,y = W_2_s(left + .15, bottom)
                glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                if xvar[0] != 51:
                    sbottom = True
                else:
                    xvar = (GLubyte * 1)(0)
                    x,y = W_2_s(left + .25, bottom)
                    glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                    if xvar[0] != 51:
                        sbottom = True
        elif randx == 3:
            xvar = (GLubyte * 1)(0)
            x,y = W_2_s(left + .05, bottom + .1)
            glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0] != 51:
                sbottom = True
            else:
                xvar = (GLubyte * 1)(0)
                x,y = W_2_s(right - .05, bottom)
                glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                if xvar[0] != 51:
                    sbottom = True
        ##right and left
        if randx == 0:
            yvar = (GLubyte * 1)(0)
            x,y =W_2_s(right, bottom+0.15)
            glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sright = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(right - .1, bottom + 0.05)
                glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sright = True

            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(left, bottom + 0.15)
            glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sleft = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(left + .1, bottom + 0.05)
                glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sleft = True
        elif randx == 1:
            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(right, bottom + 0.15)
            glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sright = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(right - .1, bottom + 0.05)
                glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sright = True
                else:
                    yvar = (GLubyte * 1)(0)
                    x,y = W_2_s(right - .1, bottom + 0.25)
                    glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                    if yvar[0] != 51:
                        sright = True

            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(left, bottom + 0.15)
            glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sleft = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(left, bottom + 0.05)
                glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sleft = True
                else:
                    yvar = (GLubyte * 1)(0)
                    x,y = W_2_s(left, bottom + 0.25)
                    glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                    if yvar[0] != 51:
                        sleft = True
        elif randx == 2:
            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(right, bottom + 0.05)
            glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sright = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(right - .1, bottom + 0.15)
                glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sright = True

            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(left, bottom + 0.05)
            glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sleft = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(left + .1, bottom + 0.15)
                glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sleft = True
        else:
            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(right, bottom + 0.05)
            glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sright = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(right, bottom + 0.15)
                glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sright = True
                else:
                    yvar = (GLubyte * 1)(0)
                    x,y = W_2_s(right, bottom + 0.25)
                    glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                    if yvar[0] != 51:
                        sright = True

            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(left+.1, bottom + 0.05)
            glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sleft = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(left, bottom + 0.15)
                glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sleft = True
                else:
                    yvar = (GLubyte * 1)(0)
                    x,y =W_2_s(left+.1, bottom + 0.25)
                    glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                    if yvar[0] != 51:
                        sleft = True
    ## z shape
    if name =='Z':
        ##bottom
        if randx == 0 or randx == 2:
            xvar = (GLubyte * 1)(0)
            x,y = W_2_s(right-0.05, bottom)
            glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0] != 51:
                sbottom = True
            else:
                xvar = (GLubyte * 1)(0)
                x,y = W_2_s(right -.15, bottom)
                glReadPixels(x,y+2 , 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                if xvar[0] != 51:
                    sbottom = True
                else:
                    xvar = (GLubyte * 1)(0)
                    x,y = W_2_s(left +.05,bottom+.1)
                    glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                    if xvar[0] != 51:
                        sbottom = True
        else:
            xvar = (GLubyte * 1)(0)
            x,y = W_2_s(left + 0.05, bottom)
            glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0] != 51:
                sbottom = True
            else:
                xvar = (GLubyte * 1)(0)
                x,y = W_2_s(right - .05, bottom + 0.1)
                glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                if xvar[0] != 51:
                    sbottom = True

        ## right and left
        if randx == 0 or randx == 2:
            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(right, bottom+ .05)
            glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sright = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(x+2,y)
                glReadPixels(right -.1, bottom+ .15, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sright = True

            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(left , bottom +.15)
            glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sleft = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(left + .1, bottom + .05)
                glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sleft = True
        else:
            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(right, bottom + .15)
            glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sright = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(right , bottom + .25)
                glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sright = True
                else:
                    yvar = (GLubyte * 1)(0)
                    x,y = W_2_s(right - .1, bottom + .05)
                    glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                    if yvar[0] != 51:
                        sright = True

            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(left, bottom + .15)
            glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sleft = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(left , bottom + .05)
                glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sleft = True
                else:
                    yvar = (GLubyte * 1)(0)
                    x,y = W_2_s(left + .1, bottom + .25)
                    glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                    if yvar[0] != 51:
                        sleft = True

    ## L shape
    if name =='L':
        ##bottom
        if randx == 0:
            xvar = (GLubyte * 1)(0)
            x,y = W_2_s(right-0.05, bottom)
            glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0] != 51:
                sbottom = True
            else:
                xvar = (GLubyte * 1)(0)
                x, y = W_2_s(right - 0.15, bottom + .1)
                glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                if xvar[0] != 51:
                    sbottom = True
                else:
                    xvar = (GLubyte * 1)(0)
                    x, y = W_2_s(right - 0.25, bottom+.1)
                    glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                    if xvar[0] != 51:
                        sbottom = True
        elif randx == 1:
            xvar = (GLubyte * 1)(0)
            x,y = W_2_s(right-0.15, bottom)
            glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0] != 51:
                sbottom = True
            else:
                xvar = (GLubyte * 1)(0)
                x,y = W_2_s(right - 0.05, bottom + .2)
                glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                if xvar[0] != 51:
                    sbottom = True
        elif randx == 2:
            xvar = (GLubyte * 1)(0)
            x,y = W_2_s(right-0.05, bottom)
            glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0] != 51:
                sbottom = True
            else:
                xvar = (GLubyte * 1)(0)
                x, y = W_2_s(right - 0.15, bottom)
                glReadPixels(x,y+2 , 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                if xvar[0] != 51:
                    sbottom = True
                else:
                    xvar = (GLubyte * 1)(0)
                    x, y = W_2_s(right - 0.25, bottom)
                    glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                    if xvar[0] != 51:
                        sbottom = True
        else:
            xvar = (GLubyte * 1)(0)
            x,y = W_2_s(right-0.05, bottom)
            glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
            if xvar[0] != 51:
                sbottom = True
            else:
                xvar = (GLubyte * 1)(0)
                x, y = W_2_s(right - 0.15, bottom)
                glReadPixels(x,y+2, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, xvar)
                if xvar[0] != 51:
                    sbottom = True

        ## right and left
        if randx == 0:
            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(right, bottom + .05)
            glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sright = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(right, bottom + .15)
                glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sright = True

            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(left, bottom + .15)
            glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sleft = True
            else:
                yvar = (GLubyte * 1)(0)
                x,y = W_2_s(left -.2, bottom + .05)
                glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sleft = True
        elif randx == 1:
            yvar = (GLubyte * 1)(0)
            x, y = W_2_s(right, bottom + .25)
            glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sright = True
            else:
                yvar = (GLubyte * 1)(0)
                x, y = W_2_s(right-.1, bottom + .05)
                glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sright = True
                else:
                    yvar = (GLubyte * 1)(0)
                    x, y = W_2_s(right-.1, bottom + .15)
                    glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                    if yvar[0] != 51:
                        sright = True

            yvar = (GLubyte * 1)(0)
            x, y = W_2_s(left, bottom + .15)
            glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sleft = True
            else:
                yvar = (GLubyte * 1)(0)
                x, y = W_2_s(left, bottom + .05)
                glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sleft = True
                else:
                    yvar = (GLubyte * 1)(0)
                    x, y = W_2_s(left, bottom + .25)
                    glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                    if yvar[0] != 51:
                        sleft = True
        elif randx == 2:
            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(right, bottom + .05)
            glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sright = True
            else:
                yvar = (GLubyte * 1)(0)
                x, y = W_2_s(right-.2, bottom + .15)
                glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sright = True

            yvar = (GLubyte * 1)(0)
            x, y = W_2_s(left, bottom + .15)
            glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sleft = True
            else:
                yvar = (GLubyte * 1)(0)
                x, y = W_2_s(left, bottom + .05)
                glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sleft = True
        else:
            yvar = (GLubyte * 1)(0)
            x,y = W_2_s(right, bottom + .05)
            glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sright = True
            else:
                yvar = (GLubyte * 1)(0)
                x, y = W_2_s(right, bottom + .15)
                glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sright = True
                else:
                    yvar = (GLubyte * 1)(0)
                    x, y = W_2_s(right, bottom + .25)
                    glReadPixels(x+2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                    if yvar[0] != 51:
                        sright = True

            yvar = (GLubyte * 1)(0)
            x, y = W_2_s(left, bottom + .05)
            glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
            if yvar[0] != 51:
                sleft = True
            else:
                yvar = (GLubyte * 1)(0)
                x, y = W_2_s(left - .1, bottom + .15)
                glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                if yvar[0] != 51:
                    sleft = True
                else:
                    yvar = (GLubyte * 1)(0)
                    x, y = W_2_s(left - .1, bottom + .25)
                    glReadPixels(x-2,y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, yvar)
                    if yvar[0] != 51:
                        sleft = True


