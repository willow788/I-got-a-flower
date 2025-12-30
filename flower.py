import time
import math 
from turtle import *

speed(0) 
# speed of the drawing animations

bgcolor("black") 
#the background color of the window

color("#924CB4") 
#flower color

hideturtle()
#hides the turtle icon while drawing

def r(theta, k=7):
    return 300 * math.sin(k * theta)
#this is the polar equation for the flower

#main loop of the drawing
for i in range(2000):
    t = i /50
    #angle changes consectively slowly for the animation

    radious = r(t)

    #getting the cartesian coordinates from polar coordinates
    x = radious * math.cos(t)
    y = radious * math.sin(t)

    #this is basically class 11 physics circular motion equations
    #ugh the trauma

    penup()
    goto(0, 0)
    pendown()
    goto(x, y)


done()
