#CTI 110
#M6T1C: Snowflake
#Reginald Jones
#

import turtle               #Apperence of Turtle
win = turtle.Screen()       #Window of the Turtle
pinky = turtle.Turtle()     #Name of Turtle, Assigned to "Pinky"
pinky.color("pink")         #Pointer will be Pink
win.bgcolor("grey")         #Background will be Grey

#Test to drawing a Pink Snowflake
pinky.penup()
pinky.forward(90)
pinky.left(45)
pinky.pendown()

def branch():
    for i in range(3):
        for i in range(3):
            pinky.forward(30)
            pinky.backward(30)
            pinky.right(45)
        pinky.left(90)
        pinky.backward(30)
        pinky.left(45)
    pinky.right(90)
    pinky.forward(90)

for i in range(8):
    branch()
    pinky.left(45)
    
#Test to drawing a Parallelogram Snowflake
##for i in range(10):
##    for i in range(2):
##        pinky.forward(100)
##        pinky.right(60)
##        pinky.forward(100)
##        pinky.right(120)
##    pinky.right(36)

win.mainloop() #Ending Command
