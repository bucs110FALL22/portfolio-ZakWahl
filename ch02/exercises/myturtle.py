import turtle

my_turtle = turtle.Turtle()  #creates the object
my_screen = turtle.Screen()

#create a purple square
my_turtle.color("purple")
my_turtle.shape("turtle")
my_turtle.fillcolor("purple")
my_turtle.begin_fill()
length = 50
my_turtle.fillcolor("purple")
my_turtle.forward(length)
my_turtle.left(90)
my_turtle.forward(length)
my_turtle.left(90)
my_turtle.forward(length)
my_turtle.left(90)
my_turtle.forward(length)
my_turtle.left(90)
my_turtle.end_fill()


#create new red square
my_turtle.right(90)
my_turtle.penup()
my_turtle.forward(length)
my_turtle.pendown()
my_turtle.color("red")
my_turtle.fillcolor("red")
my_turtle.begin_fill()
my_turtle.forward(length)
my_turtle.left(90)
my_turtle.forward(length)
my_turtle.left(90)
my_turtle.forward(length)
my_turtle.left(90)
my_turtle.forward(length)
my_turtle.left(90)
my_turtle.end_fill()

turtle.done()

my_turtle.exitonclick()




