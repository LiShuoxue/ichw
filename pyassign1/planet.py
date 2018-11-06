"""planet.py: The procedure can roughly simulate the motion of the planets in the solar system.

__author__ = "Lishuoxue"
__pkuid__ = "1800011839"
__email__ = "1800011839@pku.edu.cn"
"""

import turtle
import math

planet=['mercury','venus','earth','mars','jupiter','saturn']
color=['red','brown','blue','green','purple','white']
a=[30,60,105,165,240,330]
e=[0.206,0.007,0.017,0.093,0.048,0.056]

def c(t):
    """ c(t) is the focal length of an elliptical orbit.
    """
    return a[t]*e[t]

def b(t):
    """ b(t) is the short axis of the elliptical orbit.
    """
    return a[t]*((1-e[t]**2)**0.5)

def initialize():
    """ to show the initial state of the sun and the planets.
    """
    bg=turtle.Screen()
    bg.bgcolor('black')
    sun=turtle.Turtle()
    sun.color('yellow')
    sun.shape('circle')
    for x in range(6):
        planet[x]=turtle.Turtle()
        planet[x].pu()
        planet[x].shape('circle')
        planet[x].color(color[x])
        planet[x].setx(a[x]+c(x))
        planet[x].speed(0)
        planet[x].left(90)
        planet[x].pd()

def run():
    """ to start the motion of the planets.
    """
    k=1
    while (1):
        for x in range(6):
            planet[x].goto(a[x]*math.cos(k/a[x])+c(x),\
                            b(x)*math.sin(k/a[x]))
            k=k+1

def main():
    """main module
    """
    turtle.tracer(False)
    initialize()
    turtle.tracer(True)
    run()

if  __name__=='__main__':
    main()
    
