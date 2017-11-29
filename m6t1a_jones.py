#CTI 110
#M6T1A: Shapes
#Reginald Jones
#

import turtle               #Apperence of Turtle
win = turtle.Screen()       #Window of the Turtle
inky = turtle.Turtle()      #Name of the Turtle, Assigned to "Inky"

#Command for a square and traingle
for i in range(4):          #A loop used to simplify the command
    inky.forward(70)
    inky.left(90)

inky.penup()
inky.forward(140)
inky.pendown()

for i in range(3):
    inky.forward(80)
    inky.left(120)

#Ending Command
win.mainloop()
