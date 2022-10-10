import random 
import turtle 

window = turtle.Screen() 
canvwidth = turtle.window_width()
canvheight = turtle.window_height
leonardo = turtle.Turtle() 
leonardo.color("red")
leonardo.shape('turtle') 
leonardo.setpos(0,0) 
 
while abs(leonardo.xcor()) < (canvwidth/2) and abs (leonardo.ycor()) < (canvwidth/2):
  mylist = ["heads", "tails"] 
  coinflip = random.choice(mylist)
  print(random.choice(mylist)) 
  if coinflip == "heads": 
    leonardo.left(90)
    leonardo.forward(50)
  elif coinflip == "tails": 
    leonardo.right(90)
    leonardo.forward(50)








turtle.done()
window.exitonclick() 