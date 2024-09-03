#Using range() to Make a List of Numbers

for value in range(10,15):
    print(value)
    print()



#num = range(6)
#print(num) i do not know why this function is not working for me.
# It seems to be working in the book.

numbers = list(range(1,6))
print(numbers)

odds = list(range(2,13,2))
print(odds)

squares = []
for value in range(1,11):

    squares.append(value**2)

print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mini = min(digits)
print(mini)

#List Comprehensions: works the same as squares.append(value**2)

square =   [value**2 for value in range(3,15,2)]
print(square)

#Try It Myself

#1 Counting to twenty
one_to_twenty = [number for number  in range (1, 21)]
print(one_to_twenty)

ontwenty = list(range(1,21))
print(ontwenty)

# million = list(range(1,1000001))
# print(million)

# print()

# print(min(million))

# print()
# print(max(million))

# print()
# print(sum(million))

list_of_odds = [odd for odd in range(1,21,2)]

odding = []
for value in range(1,21,2):
    odding.append(value)

print(odding)

threes = [three for three in range(3,31,3)]
print(threes)

cubes = [number**3 for number in range(1,11)]
print(cubes)

cube = []
for value in range(1,11):
    cube.append(value**3)
print(cube)

# Working with Part of a List (Slice)

presidents = ["Paul Kagame", "Etienne Chisekedi", "Joe Biden", "Xi Jin Ping", "Vladmir Putin", " Vladmir Zerenski"]
print(presidents[0:4])
print(presidents[1])
print(presidents[:3])
print(presidents[2:])
print(presidents[-4:])

# Looping Through a Slice

print("\nHere are the presidents who are having conflicting interests in 2024:\n")
for president in presidents[:4]:
    print(president.upper())
    print()
    print("and")
    print()

#Copying a LIst

my_foods = ["pizza","sushi","noodles","红烧肉","cold veges","biryani","steak"]

siyu_foods = my_foods[:]

my_foods.append("hotpot")

siyu_foods.append("ice cream")

print("My fav foods are:")

print()

print(my_foods)

print("\nMy girlfriend's fav foods are:")

print()

print(siyu_foods)

#Time to Practice, Try IT Myself

print("My three most favorite foods are:")
print(my_foods[:2])
print()

print("In the middle of my list are those items:")
print(len(my_foods))
print(my_foods[2:5])
print(my_foods[-3:])

pizzas = ["Pepperoni","Durian", "Margherita"]
Frnd_pizzas = pizzas[:]
print()
print(pizzas)
print()
print(Frnd_pizzas)
pizzas.append("Mozerella")
Frnd_pizzas.append("Mushroom pizza")

print()


print("\nMy favorite pizzas are:")
print()
print(pizzas)

print("\nMy friend's pizzas are:")
print()
print(Frnd_pizzas)

print()
for pizza in pizzas:
    print(pizza.lower())
    print()
print()

for Frnd_pizza in Frnd_pizzas:
    print(Frnd_pizza.upper())
    print()

