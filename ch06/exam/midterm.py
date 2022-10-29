import turtle 
import math

bob = turtle.Turtle() 
window = turtle.Screen()

my_colors = ['purple','yellow','blue','pink','red']
color_loop=0

def draw_balloons(x_pos,y_pos,radius,color):
  bob.penup()
  bob.goto(x_pos,y_pos)
  bob.pendown()
  bob.color(my_colors[color_loop])
  bob.begin_fill()
  bob.circle(radius)
  bob.end_fill()
  


def calc_points(balloon):
  x_coordinate = 0
  y_coordinate = 20
  
  new_x_coordinate = x_coordinate * math.cos(-10 * balloon) - y_coordinate * math.sin(-10 * balloon)
  
  new_y_coordinate = x_coordinate * math.sin(-10 * balloon) + y_coordinate * math.cos(-10 * balloon)
  
  return(new_x_coordinate,new_y_coordinate) 

color_loop = 0
for balloon in range(5):   
  (_x,_y) = calc_points(balloon)
  draw_balloons(_x,_y,20,my_colors[color_loop])
  bob.fillcolor(my_colors[color_loop])
  color_loop = color_loop +1 
  


string_length = 65
bob.color("black")
bob.penup()
bob.goto(0,-14)
bob.pendown() 
bob.right(90)
bob.forward(string_length) 


window.exitonclick()