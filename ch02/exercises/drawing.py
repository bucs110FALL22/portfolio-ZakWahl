import turtle 

sides = int(input("How many sides do you want the shape to have? ")) 
length = int(input("How long do you want each side to be? ")) 

angle = 360 / sides

screen = turtle.Screen()

my_turtle = turtle.Turtle() 
my_turtle.shape("turtle")
my_turtle.color("red") 

print([angle]*sides)

for i in [angle]*sides:
 my_turtle.left(i)
 my_turtle.forward(length)

 
 






turtle.done() 
my_turtle.exitonclick()