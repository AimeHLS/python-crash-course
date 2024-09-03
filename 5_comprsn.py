cars = ["audi","bmw","merceds benz","jeep","toyota","ford"]

for car in cars:
    if car == "ford":

        print("This could be my fav car:")
        print(car.upper())
    else:
        print(car.title())

# CONDITIONAL TESTS

#1 CHECKING FOR EQUALITY (most exercises happened in the terminal section)
car = "Jeep"
car.lower() =="jeep"
# This test will return True because it really is the case.
# the value of the variable car is still "Jeep". However we did not change the
#  the variable to be lower case
car == "jeep" # this is false
# So the question is, why are they saying that this function is case insensitive?

#2 CHECKING FOR INEQUALITY (Inequality operator:!=)

requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("Hold the anchovies!")
# Most of conditional tests, will test for equality. But sometimes, you it is
# necessary to test for inequality.

# NUMERICAL COMPARISONS

net_profit =[100,200]

for profit in net_profit:
    if net_profit == 100:
         print("\nYou need to think and work harder my friend.\n")
    else:
        print("\nWe have achieved our goal.")
# For some reasons the code does not print two different messages for different conditions.
# I really do not know why.


# CHECKING MULTIPLE FUNCTIONS

#1 USING "and" to check whether Multiple conditions are satisfied.
# the test will pass only when both terms are satisfied
#Practice done in the terminal section and is well understood.

#2 USING"or"..the test comes out True, when either or both individual tests pass
#Practice done in the terminal section and is well understood.

# Questions raised: None
#Comments: section well grasped.

# CHECKING WHETHER A VALUE IS IN THE LIST. Uses the keyword "in".

# Questions raised: None
#Comments: section well grasped.

print()

# def checkitem(item,requested_toppings):
#     if (item in requested_toppings):
#         return True
#     return False

# print(checkitem("anchovies",requested_toppings))

order = "onions"  # Example value for demonstration purposes
requested_topping = ["pepperoni", "mushrooms", "olives"]

if order in requested_topping:
    print("\nYour topping is on the way.\n")
else:
    available_toppings = ', '.join(requested_topping).title()
    print(f"\nSorry, {order.upper()} is out of stock. Please choose among "
          f"{available_toppings}.")
#Questions raised: How can I use "if...else" statements properly? I wanted
# to print two different messages for two conditions
# but it did not workout pretty well.



# CHECKING WHETHER A VALUE IS NOT IN A LIST

banned_users = ["andreas", "carl", "daniel"]
user = "marie"

if user not in banned_users:
    print(f"\n{user.title()}, you may post a comment if you wish.\n")


# BOOLEAN EXPRESSIONS
# A boolean expression is just another name for a conditional test.(after it
# has been evaluated?)

#Try It Myself

bird = ["hawk","claw","eagle"]
print("Is bird == 'hawk'? I think it is True.")
print('hawk' in bird)

print("\nIs bird == 'pigeon' I think it is False.")
print("eagle" in bird)

print("\n Is chicken included in birds? I suspect the answer is False.")
print("This is the answer",'chicken'in bird)

cities = ["Tianjin","Guanzhou","Doha","Cairo","Kigali", "Beijing"]
print()
print(len(cities) == 2)
print(len(cities) == 6)
print(cities == "Harare")
print(cities == ["Tianjin","Guanzhou","Doha","Cairo","Kigali", "Beijing"] )
print("New York" in cities)
print(type(cities) == list)
print(type (cities) == bool)

city =["New York", "Shanghai", "Doha","Kigali"]

cities = ["Tianjin","Guanzhou","Doha","Cairo","Kigali", "Beijing"]

for city_name in city:
     if city_name in cities:
         print(f"True,I have been to  {city_name}")
else:
     print(f"False,I haven't been  to {city_name}. I would like  to travel there.")
print("New York" not in cities)
print(cities != city)

print()
house = "Maison"
print(house == "maison")
print(house.lower() == "maison")
print(house.lower() != "maison")

team_1_points = 30
team_2_points = 28
team_3_points = 45

print(team_1_points >= 20 and team_2_points >= 35)

print(team_1_points >= 20 or team_2_points >= 35)

print(team_1_points == 20 and team_2_points < 10 or team_3_points <=50)

print()
print("Kigali" in cities or city)
print("Kigali" in city or "Kigali" in cities)
#very strange rather than printing whether it is true or false,
# python chose to print the list itself. But when I check whether the item is
# included in one list, the answwer becomes True or False
print("kigali" not in city or cities)

# if STATEMENTS

#SIMPLE if STATEMENT

#1 if conditional_test is satisfied:
    #do something

age = 12
if age >= 18:
    print("You are old enough to drink alcholic drinks!")

    print("So, do you want a recommendation of good bars in the town?")
else:
    print("Sorry you are not old enough to drink yet!")
    print("Wait until your 18 years old.")

#2 THE if-elif-else CHAIN : Often you need to test more
# than two possible situations

# A swimming pool case, entry fee based on the age
# 4 years old and below = free
# Between 4 and 18 years old = $25
# 18 years old and above = 50$

print()

# ages = [3,10, 19,40,20,71]
# for age in ages:

#      if age < 4:
#          print("\nYour admission cost is 0$.")
#      elif age < 18:
#          print("\nYour admission cost is $25.")
#      elif age >= 70:
#          print("\nYour admission cost is 5$.")
#      else:
#          print("\nYour admission cost is 50$.")

ages = [3,18, 19,40,20,71]
for age in ages:
     if age < 4:
         price = 0
     elif age < 18:
         price = 25
     elif age >= 70:

         price = 10
     else:
         price = 50
     print(f"\nYour admission cost is ${price}.")
#OMITTING THE else BLOCK(recommended):
# It is not necessary to end with "else" statement.
# actually it is much better to end with elif statement to avoid
# your code running a malicious intruder. Because anything else outside
# the specified conditions will pass through the "else" command.
print()
ages = [3,10,18, 19,40,20,71]
for age in ages:
     if age < 4:
         price = 0
     elif age < 19:
         price = 25
     elif age > 19:
         price = 50
     elif age >= 65:
         price = 30
     print(f"\nYour admission cost is ${price}.")

#TESTING MULTIPLE CONDITIONS
#If-elif-else statement is poweful but it's only appropriate
# when you just need one test to pass. When multiple conditions need to satis-
#fied, consider using multiple simple "if" statements

print()
pizza_toppings = ["mushrooms", "extra cheese"]
if "mushrooms" in pizza_toppings:
    print("\nGot it. Adding mushrooms.")
if "extra cheese" in pizza_toppings:
    print("\nGot it. Adding extra cheese.")
if "pepperoni" in pizza_toppings:
    print("\nGot it. Adding pepperoni.")
print("\nFinished making your delicious pizza.")

#Interestig Python does not continue to run tests,
#the initial test has passed. Then, a solution will be to a "for" loop.

print()

# if "mushrooms" in pizza_toppings:
#     print("Adding mushrooms")
# elif "pepperoni" in pizza_toppings:
#     print("Adding pepperoni")
# elif "extra cheese" in pizza_toppings:
#     print("Adding  extra cheese")

# print("\nFinished making your pizza!")

#TIME FOR Try Something Myself
# Alien Colors #1

alien_color = ["black & yellow", "purple"]

if "purple" in alien_color:
    print("Wow, I could not have imagined that.")

if alien_color == "black & yellow":

    print("Hooooray! You have won 5 points!")

if alien_color == "yellow":
    print("Great job! You've won 2 points!")

#Alien Colors # 2

alien_color_1 = "red"

if alien_color_1 == "green":
    print("\nYou have earned 5 points!")
if alien_color_1 != "green":
    print("\nYou have just earned 10 points!")

if alien_color_1 == "green":
    print("You have just earned 5 points!")
else:
    print("You have just earned 10 points!")

# Alien Colors #3

if alien_color_1 == "green":
    print("Congrats. Here is 5 points for you!")
elif alien_color_1 == "yellow":
    print("Congrats. Here is 10 points for you!")
elif alien_color_1 == "red":
    print("Congrats. Here is 15 points for you!!")

# 'is' is used for identity (it does not check their values) verification.
# To check whether two variables point to the same object.
#It is not recommended to use 'is' to compare two variables like

# a is b? we already know that a and b are two different things.

# But a is 455? is the right way to use.
# The valid question to ask between a and b is whether or not they are equal.

print()
print("Here's an example that shows the difference between is, in, and ==:")
# Define a list and a variable
a = [1, 2, 3]
b = a  # b and a are the same object
c = [1, 2, 3]  # c has the same value as a, but is a different object
d = 2  # d is an element of a

# Check identities
print(a is b)  # Output: True
print(a is c)  # Output: False

# Check equality
print(a == b)  # Output: True
print(a == c)  # Output: True

# Check membership
print(d in a)  # Output: True

# Stages of life # try it myself # 4

age_of_life = 96
if age_of_life  <2:
    print("\nYou are just a baby.")

if age_of_life >2 and age_of_life <4:
    print("\nYou are a toddler.")

if age_of_life >=4 and age_of_life <13:
    print("\nYou are a kid.")

if age_of_life >= 13 and age_of_life <20:
    print("\nYou are a teenager.")

if age_of_life >= 20 and age_of_life < 65:
    print("\nYou are an adult.")

if age_of_life >= 65 and age_of_life <= 85:
    print("\nYou are an elder.")
if age_of_life > 85:
    print("\nYou might have become a baby again.")
    print("And what age were you before you were a baby?")

# Favorite Fruit #5
print()
fav_fruity = ["tangerine","banana", "grapes", "mango"]
if "mango" in fav_fruity:
    print(f"\n{fav_fruity[3]} Yummy! All I think about is you.")
if "banana" in fav_fruity:
    print("\nDo you want some bananas. I am not calling you a monkey.")
if "grapes" in fav_fruity:
    print("\nI love to eat and drink grapes")
if "tangerine" in fav_fruity:
    print(f"\n{fav_fruity[0]} Sweet and easy to peel. I love it!\n")

# USING if STATEMENTS WITH LISTS

pizza_toppings = ["green peppers", "mushrooms"]

# for pizza_topping in pizza_toppings:
#     if pizza_topping == "green peppers":
#         print("Sorry, we are out green peppers right now.")
#     else:
#       print(f"Adding {pizza_topping}.")
# print("\nFinished making your pizza!")

# CHECKING THAT A LIST IS NOT EMPTY

# if pizza_toppings:
#     for pizza_topping in pizza_toppings:
#         if pizza_topping == "green peppers":
#             print("Sorry, we are out green peppers right now.")
#         else:
#          print(f"Adding {pizza_topping}.")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

pizza_toppings = ["green peppers", "mushrooms"]
pizza_made = True

if pizza_toppings:
    for pizza_topping in pizza_toppings:
        if pizza_topping == "green peppers":
            print("Sorry, we are out of green peppers right now.")
            pizza_made = False
        else:
            print(f"Adding {pizza_topping}.")
    if pizza_made:
        print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

print()
# Didn't quite understand the code. But I will figure it out.

# USING MULTIPLE LISTS

available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni",
                      "pineapple", "extra cheese"]

requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"\nAdding {requested_topping}.")
        print("Finished making your pizza!")
    else:
        print(f"\nSorry, we don't have {requested_topping}.")
        # print(f"Please consider available toppings:{available_toppings}")
        # print(f"Please consider choosing from
        #       available toppings: {', '.join(available_toppings)}")
        print(f"\nPlease consider choosing from available toppings: "
      f"{', '.join(available_toppings)}")

# I prefer to use this version because it is much more clear.
# Let's brag: In just a few lines of code, we've managed
# a real-world situation prettey effectively

# TRY IT MYSELF
print()

# Hello admin
site_users = ["admin", "kim", "Ali", "matt", "Molotov"]

for site_user in site_users:
    if site_user == "admin":
        print("Hello, Admin would you like to check on other users?")
    else:
        print(f"\nHello, {site_user.title()}! Good to see you again.")

print()

# No users, check whether the list is empty and print the corresponding message

site_users = []
if site_users:
    for site_user in site_users:
        if site_user == "admin":
            print("Hello, Admin would you like to check on other users?")
        else:
            print(f"\nHello, {site_user.title()}! Good to see you again.")
else:
    print("We need to find some users.")

# Checking Usernames
print()
print()
current_users = ["James", "John", "Lucas", "Brandon"]
new_users = ["Cassie", "Elton", "Casper", "Lucas", "James"]

# for new_user in new_users:
#     if new_user in current_users:
#         print(f"\nSorry {new_user}, username already taken.
# Choose a new username")
#     else:
#         print("\nUsername available, proceed.")

# Make the comparison case insensitive by using .lower()



current_users = ["James", "John", "Lucas", "Brandon"]
new_users = ["Cassie", "Elton", "Casper", "LUCAS", "james"]

for new_user in new_users:
    if new_user.casefold() in (current_user.casefold() for current_user in current_users):
        print(f"\nSorry {new_user.title()}, "
              "username already taken. Please Choose a new username.")
    else:
        print(f"\nHi {new_user.title()}!"
              f" Your chosen username is available, please proceed.")
# There is an interesting function called "casefold", it is recommended to use it
#in case the language in use is not English. But It is good for other languages
#it becomes a good practice to use with English too.
for new_user in new_users:
    lower_new_user = new_user.lower()
    lower_current_users = (user.lower() for user in current_users)

    if lower_new_user in lower_current_users:
        print("Username taken. Please choose another username")
    else:
        print("Proceed to the next step")
# The code works because the input and the list are changed into lower case
# before comparison.

# Please comeback to this. It is not very clear the meaning of the the code
# Easy to write or easy to read.

# Ordinal Numbers
ord_numbers = 1,2,3, 4, 5, 6, 7, 8, 9
for number in ord_numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")

# STYLING MY if STATEMENTS: well implemented already
# ASSIGNMENT: RECORDING MY IDEAS.

#>>> DO an AI system that can predict where ground water is close to the surface
#so that it can be drilled at a cheaper price.

#>>> web library for kids' education videos










