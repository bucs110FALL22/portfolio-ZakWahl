import turtle #1. import modules
import random

import pygame
import math


#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
#race 1
range1 = random.randrange(1,100)
range2 = random.randrange(1,100)
print(range1, range2)
#distance = random.randrange(range)
michelangelo.forward(range1)
leonardo.forward(range2) 
print(range1, range2)

# reset to starting point
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)



#race 2
range3 = random.randrange(1,10)
range4 = random.randrange(1,10)

for i in range(0,10):
  range3 = random.randrange(1,10)
  range4 = random.randrange(1,10)
  michelangelo.forward(range3)
  leonardo.forward(range4) 


michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# PART B - complete part B here
#import pygame
#import math

pygame.init()
window = pygame.display.set_mode() 
surface = pygame.display.get_surface()
def shape_points(num_sides):
  coords = []
  num_sides = num_sides  
  side_length = 100
  offset = 150

  for i in range(num_sides):
    theta = (2.0 * math.pi * (i)) / num_sides
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    t_list = (x,y)
    coords.append(t_list) 
  return coords


pygame.draw.polygon(surface, "gold", shape_points(3))
pygame.display.flip()
pygame.time.wait(200)
window.fill("black") 

pygame.draw.polygon(surface, "red", shape_points(4))
pygame.display.flip()
pygame.time.wait(200)
window.fill("black") 

pygame.draw.polygon(surface, "purple", shape_points(6))
pygame.display.flip()
pygame.time.wait(200)
window.fill("black") 

pygame.draw.polygon(surface, "green", shape_points(9))
pygame.display.flip()
pygame.time.wait(200)
window.fill("black") 

pygame.draw.polygon(surface, "pink", shape_points(360))
pygame.display.flip()
pygame.time.wait(200)
pygame.display.get_surface()




turtle.done()
window.exitonclick() 
