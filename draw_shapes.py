import turtle

# Creating a window screen
wn = turtle.Screen()
wn.title("Mid-Term Project - Drawing Tool")
wn.bgcolor("black")
wn.setup(width=1024, height=768)

hd = turtle.Turtle()
hd.speed(0)
hd.color("red")
hd.penup()
hd.hideturtle()
hd.goto(-350, 300)
hd.write("Type X to Exit", align="center",
         font=("arial", 18, "italic"))

pen = turtle.Turtle()
pen.color("yellow")
pen.shape("arrow")
pen.goto(0, 0)


# drawing = True

# Main function with parameter size to draw a square
def draw_square(size):
    pen.fillcolor("lightyellow")
    pen.begin_fill()
    for i in range(4):
        pen.forward(size)
        pen.right(90)
    pen.end_fill()
    pen.hideturtle()
    # turtle.done()


# Additional function with parameter rad to draw a circle
def draw_circle(rad):
    pen.fillcolor("yellow")
    pen.begin_fill()
    pen.circle(rad)
    pen.end_fill()
    pen.hideturtle()
    # turtle.done()


# function with parameter size to draw an equilateral triangle
def draw_triangle(size):
    pen.fillcolor("red")
    pen.begin_fill()
    for i in range(3):
        pen.forward(size)
        pen.left(120)
    pen.end_fill()
    pen.hideturtle()
    turtle.done()


wn.listen()
wn.onkeypress(quit, "x")

# Calling function to draw a square with a passed size argument
draw_square(200)

# Calling function to draw a circle with a passed radius argument
draw_circle(50)

# Calling function to draw a triangle with a passed size argument
draw_triangle(200)
