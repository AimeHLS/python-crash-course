#Tuples:...sometimes you'll want to create a list of items that cannot change.
# Such things are called immutable, and immutable lists are known as tuples.

#Defining tuples: just like a list but it uses paratheses

dimensions = (100,50)
print(dimensions)
print(dimensions[0])
print(dimensions[1])

one_nmb_tp = (4,)
print(one_nmb_tp)

#Looping Through All Values in a Tuple  
dimensions = (100,50)
for dimension in dimensions: 
    print(dimension)
    
print()

# Writing Over a Tuple 
dimensions = (200,20)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions: 
    print(dimension)

#Try it Myself: Buffet
print()

Buffet = ("BBQ Chiken Wings", "Beijing Roasted Duck", "Beef Noodles", 
          "Pineaple Yoghurt" , "T-bone Steak")
for meal in Buffet: 
    print(meal)
    print()

print()

Buffet = ("Hot Pot", "Sushi", "Beef Noodles", "Pineaple Yoghurt" ,
          "T-bone Steak")
for food in Buffet: 
    print(food)
    print()

# Styling My Code, Python Enhancement Proposal (PEP8), 
# "code is read more often that it is written"

# Point1: Identation: Use four spaces per indentation level rather than tabs

#Point 2: Line Length: It is recommended that I use 80 characters per line
# 72 characters per line on comments (but how to count these ??)    

# Do not use blank lines excessively  in your program files

# Summary of Chapter Four 
# 1 work efficiently with lists and using "for" loops
# 2 Simple numerical lists using "Slices"
# 3 Tuples 
# 4 Making written code easy to read 

#Upcoming: Responding to appropriately to different conditions 
#using "if" statements and so on...