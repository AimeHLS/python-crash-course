magicians = ["Alice","David","Carol"]

for magician in magicians:
    print(magician)
# This can be take to mean: for every magician in the list of magician, print 
# magician's name

for magician in magicians:
    print(f"{magician.upper()}, bravo! That was a great trick.")
    
    print(f"I'm looking foward to your event{magician.title()}.\n")
    
    print()
print("Thank you, everyone. That was a great show!")
#Doing Something After a For a loop
    
print()
print()
 
places = ["the white house","world trade center","burj khalifa","shanghai tower"
          ,"twin towers"]

for place in places:
    print(place.title())
    
    print()  

# A closer look at Looping 
# ...computer automates repetitive task.

# Doing Something Within a for Loop
for place in places:
    
    print(f"{place.title()}, this is one of breathtaking buildings 
          on planet earth.")
    
    print(f"\nI can't wait to visit this place.")
    
    print()
    
print("On my next vacation, I am definitely going to one of these places!")

#Avoiding Indentation Errors
#1 Always indent the line that comes after the "for" statement in the loop

#2 Forgetting to Indent Additional Lines. This may result in python printing
# message for one user, whilst we need to loop. The main reason why,
# this happen, is because the intended message is not indented.

#3 Indenting Unnecessarily
# Indent only when you have specific reaseon to do so. In this case, only the
# actions you want to repeat for each item in a for a loop.

#4 Indenting unnecessarily After the Loop (this code will be counted as a part 
# of the loop or will result in an error.)

# I shouldn't feel bad when a small error takes a long time to fix. It is common. 
# (Gecko)

print()

print("\nTry It Myself Exercise Starts from Here.\n")
# Tried it myself 
Pizzas = ["Pepperoni","Durian", "Margherita"]

for  pizza in Pizzas:
    print(pizza)
    
    print()
for pizza in Pizzas:
    
    print(f"\nIt is not only one of the most popular pizza, {pizza.upper()} is
          also one of my favorite pizza. 
          I really enjoy eating {pizza.title()} pizza\n")
    
print("\nI love eating Pizza, I can't wait to have one very soon!\n")

animals = ["cat", "lion","tiger","panther","jaguar", "leopard"]

for animal in animals:
    print(animal.title())
    print()
    print(f"A {animal} will make a dangerous but a great companion.")
    
print("\nAll these animals belongs to big cat family.\n")

#M