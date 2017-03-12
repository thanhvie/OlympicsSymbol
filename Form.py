import turtle
from turtle import*

a= turtle.Screen()

def draw():
    ai = turtle.Turtle()
    ai.shape("turtle")
    ai.speed(3)
    ai.pensize(40)
    ai.penup()
    ai.right(180)
    ai.forward(190)
    ai.pendown()
    #draw yellow circle
    ai.pencolor("yellow")
    ai.circle(140,360)
    ai.penup()

    #draw green circle
    ai.home()
    ai.right(180)
    ai.penup()
    ai.forward(-150)
    ai.pendown()
    ai.pencolor("green")
    ai.circle(140,360)
    ai.penup()

    #draw blue circle
    ai.home()
    ai.left(180)
    ai.forward(500)
    ai.left(90)
    ai.forward(-10)
    ai.pendown()
    ai.pencolor("blue")
    ai.circle(140,360)
    ai.penup()

    #draw black circle
    ai.home()
    ai.forward(120)
    ai.left(90)
    ai.forward(10)
    ai.pendown()
    ai.pencolor("black")
    ai.circle(140,360)
    ai.penup()

    #
    ai.home()
    ai.forward(460)
    ai.left(90)
    ai.forward(10)
    ai.pendown()
    ai.pencolor("red")
    ai.circle(140,360)
    ai.penup()

for x in range(0,1000):
    draw()
    a.clearscreen()

a.exitonclick()
a.mainloop()




