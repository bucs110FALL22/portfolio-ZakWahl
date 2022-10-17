import turtle 



side_length = int(input("How long do you want each side to be?: ")) 

num_sides = int(input("How many sides do you want there to be? ")) 



def drawEqShape(myturtle, side_length, num_sides):
  for i in range(num_sides):
    myturtle.shape("turtle")
    myturtle.color("green") 
    myturtle.forward(side_length)
    myturtle.left(360/num_sides)

myturtle = turtle.Turtle()
drawEqShape(myturtle, side_length, num_sides)


