class Num:
  def __init__(self):
    self.num = 5 
n = Num() 
print(n) 
print(id(n))


class Graph:
  def __init__(self, title="My Graph"):
    self.points = []
    self.title = title 
  
  def add_point(self, p):
    point_str = "" 
    
    return self.title

  def __str__(self):
    point_str = ""
    for p in self.points:
        point_str = f"({self.x}, {self.y})"
    return f"{self.title}: {point_str}"


def main():
  g = Graph()
  print(g) 

main()