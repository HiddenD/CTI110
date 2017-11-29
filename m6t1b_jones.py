#CTI 110
#M6T1B: Initials
#Reginald Jones
#

import turtle               #Apperence of Turtle
win = turtle.Screen()       #Window of the Turtle
blinky = turtle.Turtle()    #Name of Turtle, Assigned to "Blinky"
blinky.color("red")         #Pointer will be Red


#Command for Initial R
blinky.left(90)
blinky.forward(120)

for i in range(3):
    blinky.right(90)
    blinky.forward(60)

blinky.left(140)
blinky.forward(90)

blinky.penup()
blinky.left(40)
blinky.forward(50)
blinky.pendown()

#Command for Initial J
blinky.forward(50)
blinky.left(90)
blinky.forward(120)
blinky.left(90)
blinky.forward(50)
blinky.left(180)
blinky.forward(100)

win.mainloop() #Ending Command
