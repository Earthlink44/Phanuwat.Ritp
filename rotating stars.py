import turtle
import time

# Create a turtle name earth
earth = turtle.Turtle()
earth.speed(0)
earth.pencolor('red')
earth.pensize(2)
earth.hideturtle()

# Create a turtle name zelda
zelda = turtle.Turtle()
zelda.speed(0)
zelda.pencolor('blue')
zelda.pensize(2)
zelda.hideturtle()

# Create a turtle name zelda
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
    
    earth.penup()
    earth.goto(0,0)
    earth.left(1)
    earth.pendown()
    earth.clear()

    for x in range(400): # earth create a star
        earth.forward(x)
        earth.left(144)


    zelda.penup()
    zelda.goto(200,210)
    zelda.right(1)
    zelda.pendown()
    zelda.clear()
    
    
    for x in range(100): # zelda create a star
        zelda.forward(x)
        zelda.left(144)

    ganon.penup()
    ganon.goto(-200,-210)
    ganon.right(1)
    ganon.pendown()
    ganon.clear()
    
    
    for x in range(100): # ganon create a star
        ganon.forward(x)
        ganon.left(144)

    turtle.update()
    time.sleep(0.001)

    

    

    
    
    

        








    




