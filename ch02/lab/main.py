import random



#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print(cost_per_week, type(cost_per_week)) #just incase
print("Cost per week:", cost_per_week)
#

classes_per_week = 3 
print(classes_per_week, type(classes_per_week))

cost_per_class = cost_per_week / classes_per_week
print(cost_per_class, type(cost_per_class))


print("The cost per class is: $" , cost_per_class)


#Part B

list_of_numbers = [ 1, 2, 3, 4, 5]
#do i need another print statement here?


random.choice(list_of_numbers) 

random_result = random.choice(list_of_numbers)

print("Your random choice from the list is:", random_result) 