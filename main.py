import math
import turtle

dart = turtle.Turtle()

def drawSineCurve(dart):
  
  for angle in range(-360 , 361):
    y = math.sin(math.radians(angle))
    dart.goto(angle, y )
    dart.pendown()
  dart.pu()


########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help

def setupWindow(wn):
  wn.bgcolor('lightblue')
  wn.setworldcoordinates(-360,-1,360,1)
  
def setupAxis(dart):

  dart.pu()
  dart.goto(-360,0)
  dart.pd()    
  dart.goto(360,0)
  dart.pu()
  dart.goto(0,-1)
  dart.pd()
  dart.goto(0,1)
  dart.pu()
  dart.goto(0 , 0)
  

def drawCosineCurve(dart):
  
  for angle in range(-360 , 361):
    y = math.cos(math.radians(angle))
    dart.goto(angle, y )
    dart.pd()
  dart.pu()


def drawTangentCurve(dart):
  
  for angle in range(-360 , 361):
    y = math.tan(math.radians(angle))
    dart.goto(angle, y )
    dart.pd()
  dart.pu()


  
##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(1)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()