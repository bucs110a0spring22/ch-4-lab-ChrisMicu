import math
import turtle
from math import pi

dart = turtle.Turtle()

 
def drawSineCurve(dart):
  sineColor= str(input("Enter color for sin "))
  for angle in range(-360 , 361):
    y = math.sin(math.radians(angle))
    dart.goto(angle, y )
    dart.pendown()
    dart.pencolor(sineColor)
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
  graphColor= str(input("Enter color for graph "))
  dart.pencolor(graphColor)
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
  cosColor= str(input("Enter color for cos "))
  for angle in range(-360 , 361):
    y = math.cos(math.radians(angle))
    dart.goto(angle, y )
    dart.pencolor(cosColor)
    dart.pd()
  dart.pu()


def drawTangentCurve(dart):
  tanColor= str(input("Enter color for tan "))
  for angle in range(-360 , 361):
    y = math.tan(math.radians(angle))
    dart.goto(angle, y )
    dart.pencolor(tanColor)
    dart.pd()
  dart.pu()


  
##########  Do Not Alter Any Code Past Here ########
def main():
    
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(1)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()

    
#Midterm
  
##Code
def drawFlower():
  dart=turtle.Turtle()
  dart.speed(0)
  dart.goto(0,0)
print("You are beautiful enjoy this rose")
wn = turtle.Screen()
wn.bgcolor("pink")
wn.setworldcoordinates(-150,-200,250,200)
dart.shape("turtle")
dart.color("firebrick","red")


for i in range(36):
  dart.forward(200)
  dart.left(170)
  dart.stamp()
wn.clear()

###Convert Degree to Radian Code##

def factor(n):
  fact = 1
  for i in range(1,n+1):
    fact = fact * i
  return fact
  
def convert(value):
  return value * pi / 180

def sin(y,n):
  sine = 0
  for i in range(n):
    sn = (-1)**i
    sine = sine + ((y**(2.0*i+1))/factor(2*i+1))*sn
  return sine


def cos(y,n):
  cose = 0
  for i in range(n):
    sn = (-1)**i
    cose = cose + ((y**(2.0*i))/factor(2*i))*sn
  return cose


def printMenu():

  while(True):

    print("SELECT A TRIG IDENTITY")
    print("1 - Calculate the sine of a value")
    print("2 - Calculate the cosine of a value")
    print("3 - Calculate the tangent of a value")
    print("4 - See what the curves look like")


    userInput = int(input("Enter your option: "))

    if userInput == 1:
      value = int(input("Enter the value (in degrees): "))
      radians = convert(value)
      result = sin(radians, 10)
      print("The sine of",value,"is %.4f" %result)
    elif userInput == 2:
      value = int(input("Enter the value (in degrees): "))
      radians = convert(value)
      result = cos(radians, 10)
      print("The cos of",value,"is %.4f" %result)
  
    elif userInput == 3:
      value = int(input("Enter the value (in degrees): "))
      
      if value == 90 or value == 270:
        print("The tangent of",value,"is undefined")
      else:
        radians = convert(value)
        result = sin(radians,10) * cos(radians,10) * sin(radians,10) * cos(radians,10)
        print("The tangent of",value,"is %.4f" %result)
  
    elif userInput == 4:
      break
    else:
      print("Invalid Option. Please try again")
printMenu()


'''
    Want to add more of the user controlling these charts. So what color the sin, cos, and tan should be drawn can be chosen by the user. As well as allowing the user to alter the graph and see what it looks like when being drawn at a different radian. Additionally, something to change the entire chart would be to add intersection points and show where they intersect.
  '''
main()