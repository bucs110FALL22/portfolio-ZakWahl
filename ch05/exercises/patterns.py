def star_pyramid(): 
  rows = int(input("Enter a number of rows: ")) 
  for i in range(rows): 
    for j in range(i+1):
      print("* ", end="")
    print("\n")
star_pyramid()

def rstar_pyramid(): 
  rows = int(input("Enter a number of rows: ")) 
  for i in range(rows, 0, -1): 
    for j in range(0,i):
      print("* ", end="")
    print("\n") 
rstar_pyramid() 

