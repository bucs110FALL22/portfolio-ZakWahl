
grade = int(input("What is your current grade? "))

def percentage_to_letter(score=0):
  if score>= 90:
    print("A")
  if score>= 80 and score < 90:
    print("B")
  if score>= 70 and score <80: 
    print("D")
  if score<=59:
    print("F")

def is_passing(letter=None):
  if letter in("A", "B", "C"):
    return True 
  else:
    return False 

grade = int(input("What is your current grade? "))
percentage_to_letter(grade) 
result = (percentage_to_letter)
is_passing(result) 
