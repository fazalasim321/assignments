# Declare a variable student_id with value 101 (integer) and a variable grades with a list: [85, 90, 92].
#Print the value and type of both variables using the type() function.
student_id = 101
grades =[85,90,92]
print(student_id,type(student_id))
print(grades,type(grades))
# Create a variable price with value 19.99 (float) and a variable dimensions with a tuple: (5.5, 3.2).
#Print the value and type of both variables.
price = 19.99
dimensions = (5.5, 3.2)
print(price, type(price))                 # Float type
print(dimensions, type(dimensions))
#Declare a variable complex_value with a complex number 2 + 3j, and a variable numbers with range(1, 5).
#Print the value and type of both variables.
complex_value = 2 + 3j
numbers = range(1, 5)
print(complex_value, type(complex_value)) # Complex number
print(numbers, type(numbers))        
 #Create a variable is_active with boolean value True, and a variable unique_ids with a set: {1, 2, 3}.
#Print the value and type of both variables.
status = 'Active'
fixed_colors = frozenset(["red", "blue"])
print(status, type(status))               # String
print(fixed_colors, type(fixed_colors)) 
#Create a variable country with a string "Canada" using double quotes, and a variable cities with a list: ["Toronto", "Vancouver"].
#Print the value and type of both variables.
country = "Canada"
cities = ["Toronto", "Vancouver"]
print(country, type(country))             # String
print(cities, type(cities)) 
#Declare a variable motto with the string 'Keep it simple' using triple single quotes, and a variable coordinates with a tuple: (10, 20, 30).
#Print the value and type of both variables.
motto = '''Keep it simple'''
coordinates = (10, 20, 30)
print(motto, type(motto))                 # String
print(coordinates, type(coordinates)) 
#Create a variable quantity with value 50 (integer), and a variable tags with a set: {"urgent", "new"}.
#Print the value and type of both variables.
quantity = 50
tags = {"urgent", "new"}
print(quantity, type(quantity))           # Integer
print(tags, type(tags))
#Declare a variable distance with a float value 42.5, and a variable steps with range(0, 10, 2).
#Print the value and type of both variables.
distance = 42.5
steps = range(0, 10, 2)
print(distance, type(distance))           # Float
print(steps, type(steps))   
#**Create a variable note with a multi-line string using triple double quotes:

#Meeting at 9 AM  
#Bring notebook

#and a variable locked_values with a frozenset: {100, 200, 300}.
#Print the value and type of both variables.**
note = """Meeting at 9 AM  
Bring notebook"""
locked_values = frozenset({100, 200, 300})
print(note, type(note))                   # Multiline String
print(locked_values, type(locked_values))