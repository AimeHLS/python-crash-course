places = ["Cairo","Kigali", "Nyagatare","Nyamata","Doha"]
print(places) 

#this isn't the output the users should see, the following shows how to access elements in a List

print(places[4])
print(places[4].upper())
print(places[-2].upper())

# Using Individual Values from a List

speech = f"The other city in Africa I went to except {places[1].upper()} is {places[0].upper()}."
print(speech)

# Try it yourself

names = ["David","Jonathan","Bishaza","Yorke"]
print(names[0])
print(names[-1])
print(names[1]) 
print(names[2])

greet_0 = f"Hi, how are you doing {names[0]}!"
greet_1 = f"Hey hey {names[1]},how is TIANJIN? "
greet_2 = f"Good to hear from you {names[2]}. Rwanda is good. How about XIAN."
greet_3 = f"Hi {names[3]}, can't wait to do parkour again!"

print(greet_0)
print()
print(greet_1)
print()
print(greet_2)
print()
print(greet_3)
print()
vehicles = ["Jeep Sahara","Ford Raptor", "Toyota Landcruiser", "Honda Bike", "BMW Bike"]
print(vehicles)
print()
print(f"I would like to own a blue {vehicles[0]}, or a black{vehicles[1]}.")
print()
print(f"One of my longtime favorite cars is {vehicles[2]}, I like that it can climb mountains.")
print()
print(f"And when it comes to bikes my favorite brands are {vehicles[-1]} and {names[-2]}.")

#Modifying, Adding, and Removing Elements

motorcycles = ["Honda","Yamaha","Harley Davidson","Suzuki","Kawasaki"]

print(motorcycles)
motorcycles[1] = "Ducati"

#1 adding elements by using append() append

print(motorcycles)
motorcycles.append("Yamaha")
print(motorcycles)
motors = []
motors.append("Honda")
motors.append("BMW")
motors.append("Yamaha")
print(motors)

#adding elements by using INSERT, in order to specify position of a new element in the list.

motors.insert(2, "Kawasaki")
print(motors)

# Removing elements from the list
#1 del  statement 

print()
print(motors)
del motors[2]
print()
print(motors)

#2 pop() Method: removes the last item and let you use it, after it was removed from the list

#To pop an item from any position in a list just include its index in the brackets

print()
popped_motors = motors.pop()
print(popped_motors)
print(f"The first motorcycle I rode was {popped_motors.upper()}.")

# Removing items by their names, we use remove(...)

print(motorcycles)
motorcycles.remove("Kawasaki")
print(motorcycles)
print()
#have you ever seen a list in a list
motorcycles_1 = ["Ducati", "Kawasaki", "Honda", "Yamaha", "Suzuki", "Harley Davidson","Ducati"]
print()
too_expensive = "Harley Davidson"
motorcycles_1.remove(too_expensive)
print(motorcycles_1)
print(f"\nA {too_expensive.upper()} is too expensive for me.")

#TRIED IT MYSELF 

guest_list = ["Jordan Peterson", "Martin Luther King Jr.", "Jeff Bezos"]

print()

print(f"\tGreetings, \n\nDear Dr.{guest_list[0]}, \n\nWe will be glad to have you join us for tomorrow's dinner.\n{guest_list[1]} and {guest_list[2]} will also be coming")

print()

print(f"\tGreetings, \n\nDear Dr.{guest_list[1]}, \n\nWe will be glad to have you join us for tomorrow's dinner.\n{guest_list[0]} and {guest_list[2]} will also be coming")


print()

print(f"\tGreetings, \n\nDear Dr.{guest_list[2]}, \n\nWe will be glad to have you join us for tomorrow's dinner.\n{guest_list[1]} and {guest_list[0]} will also be coming")


print()

print(guest_list)
print()
print(f"Dear {guest_list[0]} & {guest_list[2]} \n\nWe are sorry to inform you that {guest_list[1].upper()}cannot make it for tonight's dinner because he has been shot.")

guest_list[1] = "Alistair Begg"
print()
print(guest_list)


print()

print(f"\tGreetings, \n\nDear Dr.{guest_list[0]}, \n\nWe will be glad to have you join us for tomorrow's dinner.")

print()

print(f"\tGreetings, \n\nDear Pastor   {guest_list[1]}, \n\nWe will be glad to have you join us for tomorrow's dinner.")

print()

print(f"\tGreetings, \n\nDear{guest_list[2]}, \n\nWe will be glad to have you join us for tomorrow's dinner.")

print()

print("To our distinguished guests,\n\nwe are glad to inform you that we found a bigger table. \nHence we will be inviting three more guests for tomorrow's dinner.")

print()

guest_list.insert(0, "Elon Musk")
guest_list.insert(2, "Sean Carter")
guest_list.append("Paul Kagame")
print(guest_list)

print()

print(f"\tGreetings, \n\nDear {guest_list[0]}, \n\nWe will be glad to have you join us for tomorrow's dinner.")

print()

print(f"\tGreetings, \n\nDear {guest_list[2]}, \n\nWe will be glad to have you join us for tomorrow's dinner.")

print()

print(f"\tGreetings, \n\nDear H.E {guest_list[-1]}, \n\nWe will be glad to have you join us for tomorrow's dinner.")

print()

print(f"\tGreetings, \n\nDear {guest_list[1]}, \n\nWe will be glad to have you join us for tomorrow's dinner.")

print()

print(f"\tGreetings, \n\nDear {guest_list[3]}, \n\nWe will be glad to have you join us for tomorrow's dinner.")

print()

print(f"\tGreetings, \n\nDear {guest_list[4]}, \n\nWe will be glad to have you join us for tomorrow's dinner.")

print()

print(f"Dear invitees, this is to inform you of an unfortunate news that the new found table won't arrive on time due to unforeseen reasons, hence we will be able to host only two guests that will be chosen randomly")

print()

print(guest_list)

print()
pop_1 = guest_list.pop()

print(f"Dear {pop_1}, we regret to inform you that your invitation has been revoked due to not having enough space. \nWe promise that you will be our guest of honor for the next event.\n\nSincerely Yours.")

pop_2 = guest_list.pop()

print()

print(f"Dear {pop_2}, we regret to inform you that your invitation has been revoked due to not having enough space. \nWe promise that you will be our guest of honor for the next event.\n\nSincerely Yours.")

print()

pop_3 = guest_list.pop()
print(f"Dear {pop_3}., we regret to inform you that your invitation has been revoked due to not having enough space. \nWe promise that you will be our guest of honor for the next event.\n\nSincerely Yours.")

print()

pop_4 = guest_list.pop()
print(f"Dear {pop_4}, we regret to inform you that your invitation has been revoked due to not having enough space. \nWe promise that you will be our guest of honor for the next event.\n\nSincerely Yours.")

print()

print(f"Dear {guest_list[0]}, it is with pleasure that we inform you that your invitation still holds.\nWe be glad to see you this evening for foreamentioned diner event.\nSincerely ")

print()

print(f"Dear {guest_list[1]}, it is with pleasure that we inform you that your invitation still holds.\nWe be glad to see you this evening for foreamentioned diner event.\nSincerely ")

print()

del guest_list[0]

print()

del guest_list[0]
print(guest_list)

print()
print("SORTING LISTS STARTS HERE.")
print()

#ORGANIZING LISTS PERMANENTLY

#Sorting a List Peremanently with the sort() Method: after using reverse function, the order of the list can never be reversed.

cars = ["toyota", "jeep", "mercedes benz", "volkswagen", "ford", "bmw", "range rover", "bentley", "porsche"]

cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

#ORGANIZING LISTS TEMPORARILY: SORTED FUNCTION

print()

print("Here is the orginal list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#Printing a List in Reverse Order: reverse()
print()
cars.reverse()
print(cars)

#Finding the Length of a List 
print(len(cars))

print()
#TRIED IT MYSELF

print("Exercise on Sorting Lists...")
print()
places_to_visit = ["shanghai", "zanzibar", "seychelles", "gisenyi", "akagera national park"]
print(places_to_visit)

print()

print(sorted(places_to_visit))

print()

print(places_to_visit)

print()

places_to_visit.reverse()
print(places_to_visit)

print()

places_to_visit.sort()
print(places_to_visit)

#How can I use sort again to reverse the order of the list again. That's possible? I will have to check this on YouTube
print()

places_to_visit.reverse()
print(places_to_visit)

print()
print(places_to_visit)

print(len(guest_list))

print("All Functions Exercise, Starts from Here.")

mountains = ["Kalisimbi","Kilimanjaro", "Everest", "Gahinga", "Mount Kigali","Maranyundo", "Juru"]
print(len(mountains))

print()

print(sorted(mountains))

print()

mountains.sort()
print(mountains)

print()

mountains.reverse()

print()

print(mountains)

print()

mountains.remove("Everest")
print()

print(mountains)

print(mountains.pop())

print(mountains[3])

print(f"\nOne of the mountains that I want to hike is {mountains[3]}.")

print()

mountains.append("Alps")
mountains.append("Nyiragongo")
print(mountains)

# Replacing Something in a List
print()
mountains[2] = "Sabyinyo"
print(mountains)

print()

mountains.insert(0,"Mt. Kigali")

print()

del mountains[-1]
print(mountains)

print()

mountains.remove("Maranyundo")
print(mountains)

print()

print(mountains[4].upper())

print()

print(mountains[3].lower())

print()

mountains.reverse()
print(mountains)

#dangerous = ["Sabyinyo"]
#mountains.remove(dangerous)
#print(mountains)
# I used this function before. But now I don't know why it is not working. I have no idea why, I guess I will keep moving. 

# Avoiding Index Errors When Working with Lists 

#1 IndexError: list index out of range
#solutions: use -1 to access the last item or print the length of the list to see how big is your list. 
motorbikes = ["honda","bmw", "harley davidson"]
print(motorbikes[3]) 

#chapter summary 
