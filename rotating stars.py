import turtle
import time

# Create a turtle name link
link = turtle.Turtle()
link.speed(0)
link.pencolor('red')
link.pensize(2)
link.hideturtle()

# Create a turtle name zelda
zelda = turtle.Turtle()
zelda.speed(0)
zelda.pencolor('blue')
zelda.pensize(2)
zelda.hideturtle()

# Create a turtle name ganon
ganon = turtle.Turtle()
ganon.speed(0)
ganon.pencolor('green')
ganon.pensize(2)
ganon.hideturtle()

# Adjust the window    
turtle.tracer(0)
turtle.bgcolor('black')
turtle.title('Codekids')

while True:

    # earth create a star
    link.penup()
    link.goto(0,0)
    link.left(1)
    link.pendown()
    link.clear()

    for x in range(400): 
        link.forward(x)
        link.left(144)

    # zelda create a star
    zelda.penup()
    zelda.goto(200,210)
    zelda.right(1)
    zelda.pendown()
    zelda.clear()
    
    for x in range(100): 
        zelda.forward(x)
        zelda.left(144)

    # ganon create a star
    ganon.penup()
    ganon.goto(-200,-210)
    ganon.right(1)
    ganon.pendown()
    ganon.clear()
    
    for x in range(100): 
        ganon.forward(x)
        ganon.left(144)

    turtle.update()
    time.sleep(0.001)
