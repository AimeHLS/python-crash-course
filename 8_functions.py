#   WHAT TO EXPECT
# Using Functions to break programs into small parts,
# each one doing a specific job.
# Hence, be able to write more efficient code that's easier to troubleshoot,
# maintain，store in other places and reuse in different programs

#1 DEFINING A FUNCTION #Simplest structure of a fuction

def greet_user():
    """Display a simple greeting message"""
    print("Hello!")

greet_user()

# PASSING INFORMATION TO A FUNCTION

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user("james")
greet_user("sam")

#ARGUMENTS AND PARAMETERS

# username: PARAMETER: information the function needs to do its job
# "james" or "sarah": ARGUMENT:information that's passed from a function call to
# a function.

# TRYING MYSELF

def display_message(chapater_8):
    """Python crash course chapter 8"""
    print(f"I am learning how {chapater_8} work in python.")

display_message("functions")

def favorite_book(title):
    """My favorite book"""
    print(f"\n{title.title()}, This is my all time favorite book. "
          "I could read it a hundred times")

favorite_book("when breath becomes air")

# PASSING ARGUMENT

#1 Positional Argument

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet("hamster", "harry")
describe_pet("dog", "puppy")

#2 Keyword Argument
#mostly to avoid mixing up things

def describe_pet(pet_name, animal_type= "dog" ):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type="hamster", pet_name="harry")
describe_pet(animal_type="dog", pet_name="puppy")
describe_pet("willie")

#3 Default Values

#4 Equivalent Function Calls
# It doesn't matter which calling style I use as long as it produces intended
# output and easiest for me to understand.

# AVOIDING ARGUMENT ERRORS # Unmatched arguments: most common.

# TRY IT MYSELF
#1 T-shirt
def make_shirt(size, message):
    """Make T-shirts again"""
    print(f"\nI made an {size.upper()} size shirt and it says: {message.title()}")

make_shirt("m", "brighter days loading...")
make_shirt(size= "xl", message= "tired but kept moving.")

print()

def make_shirt(message, size= "l" ):
    """Make T-shirts again"""
    print(f"\nI made an {size.upper()} size shirt and it says: {message.title()}")

make_shirt("I love python")
print()

def make_shirt(size, message= "Tonight we mourn, tomorrow we hunt" ):
    """Make T-shirts again"""
    print(f"\nI made an {size.upper()} size shirt and it says: {message.title()}")

make_shirt("l")
make_shirt("m")

#2 Cities
def describe_city(city, country= "japan"):
    """Describe three cities"""
    print(f"{city.title()} is in {country.title()}.")

describe_city("tokyo", "japan")
describe_city("osaka")
describe_city("Nagasaki")

#RETURN VALUES

#1 Returning a Simple Value

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("jimi", "hendrix")
print(musician)

#2 Making an Argument Optional
#Optioanal valuess allow functions to handle a wide range of use cases while
#letting function calls remain as simple as possible.


def get_formatted_name_well(first_name, last_name, middle_name= ""):
    """Return a full name, neatly formatted."""
    if middle_name:
       full_name = f"{first_name} {middle_name} {last_name}"
    else:
       full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name_well("jimi", "hendrix")
print(musician)

musician = get_formatted_name_well("john", "hooker", "lee")
print(musician)

# RETURNING A DICTIONARY
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {"first": first_name, "last": last_name}
    return person

musician = build_person("jimi", "hendrix")
print(musician)

#Extending the fun
print()
def build_person(first_name, last_name, age= None):
    """Return a dictionary of information about a person."""
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person

musician = build_person("jimi", "hendrix", age=27)
print(musician)

# USING A FUNCTION WITH A WHILE LOOP

# Let's try to greet users more formally
def get_formatted_name(first_name, last_name):
    """Get formatted name"""

    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("And enter 'q' at any time to quit.")

    f_name = input("First name: ")
    if f_name.lower().strip() == "q":
        break

    l_name = input("Last name: ")
    if l_name.lower().strip() == "q":
        break
    if f_name.lower().strip() != "q" and l_name.lower().strip() != "q":
         formatted_name = get_formatted_name(f_name, l_name)
         print(f"\nHello, {formatted_name}!")

#TRYING IT MYSELF

#1 City Names

def city_country(city, country):
    """Cities and their country"""
    travel = f"{city}, {country}"
    return travel.title()



places = city_country("havannah", "cuba")
print(places )

places = city_country("shanghai", "china")
print(places)

places = city_country("austin texas", "usa")
print(places)

print()

#2 Albums

def bestselling_album(title, singer):
    """Return a string representation of the bestselling album."""
    return f"Name: {title}  Artist: {singer}"

# Example usage
first_bestselling = bestselling_album("Thriller", "Michael Jackson")
print(f"\nThe first bestselling album is:\n\t{first_bestselling}")

second_bestselling = bestselling_album("Greatest hits 1971 - 1976",
                                       "The Eagles")
print(f"\nThe second bestselling album is:\n\t{second_bestselling}")

third_bestselling = bestselling_album("Back in Black", "AC/DC")
print(f"\nThe third bestselling album is:\n\t{third_bestselling}")

print()

def bestselling_album(title, singer, sold_copies= None, release_year= None):
    """Return a string representation of the bestselling album."""
    goats = {"Name": title, "Artist": singer}
    if sold_copies:
        goats["Sold_copies"] = sold_copies
    if release_year:
        goats["Year"] = release_year
    return goats

first_bestselling = bestselling_album("Thriller", "Michael Jackson",
                                      "66M", "1982")
print(f"\nThe first bestselling album is:\n\t{first_bestselling}")

second_bestselling = bestselling_album("Greatest hits 1971 - 1976",
                                       "The Eagles", "42M", "1976")
print(f"\nThe second bestselling album is:\n\t{second_bestselling}")

third_bestselling = bestselling_album("Back in Black", "AC/DC", "50M")
print(f"\nThe third bestselling album is:\n\t{third_bestselling}")


#3 User album
def user_album(title, singer, name):
    """Get users to tell their favorite album"""

    tell = f"\n{name.title()}'s favorite album is"
    f" {title.title()} by {singer.title()}"
    return tell

while True:
    print("\n\nTell us your name and your favorite album.")
    print("And enter 'quit' to exit")

    name = input("Your Name: ")
    if name.lower().strip() == "quit":
        break
    album = input("Fav. album: ")
    if album.lower().strip() == "quit":
        break
    artist = input("singer: ")
    if artist.lower().strip() == "quit":
        break
    if album.lower().strip() != "quit" and artist.lower().strip() != "quit":
        report = user_album(album, artist, name)
        print(report)
    if name.lower().strip() != "quit":
        report = user_album(album, artist, name)
        print(report)


# Let the user tell their favorite food and desserts

def attendee_food_dessert(name, food , dessert):#set parameters
    """Get users' name, favorite food and dessert"""#describe what you want to
    #accomplish
    foods = f"{name.title()} would like to eat {food} and {dessert} as a dessert."
    return foods # what would you like to see in the output.

#

while True:  #Set a way to exit a while loop
    print("\nTell us your name and what would you like to eat.")
    print("Enter 'done' once you have finished.")

    attendee = input("Name: ")
    if  attendee.lower().strip() == "done":
        break

    meal = input("I would like to eat: ")
    if  meal.lower().strip() == "done":
        break
    after_meal = input("Dessert: ")
    if  after_meal.lower().strip() == "done":
        break
    #set inputs and use if statements to stop the loop after every

    if attendee.lower().strip() != "done" or meal.lower().strip() != "done":
    # Use last if statement to avoid printing the exit word

        selected_food = attendee_food_dessert(attendee, meal, after_meal)
        #Set a string to use to call the function with inputs as arguments
    if after_meal.lower().strip() != "done":
         selected_food = attendee_food_dessert(attendee, meal, after_meal)

    print(selected_food)
        #Output


#PASSING A LIST

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ["hannah", "ty", "margot"]
greet_users(usernames)

print()

# MODIFYING A LIST IN A FUNCTION

# 1 Without using functions

# Case study: a company that prints 3D stuffs sent by users

# Start with some designs that need to be printed.
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

# Simulate printing each design, until none left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models:
print("\nThe following models have been printed:")
print(completed_models)

# Consider a class of six phD students as each one passes their own defence are
# added in a different list of those who are about to graduate

class_of_2024 = ["john", "bob", "andy", "tom", "kim", "max"]
graduated_students = []

while class_of_2024:

    passed_defence = class_of_2024.pop()
    print(f"{passed_defence.title()} has passed defence:")
    graduated_students.append(passed_defence)

# Show the list of all graduated students
print(f"\nThe following students have graduated")
print(graduated_students)

#2 Using function: we will have to use two functions
print()

# def print_models(unprinted_designs, completed_models):
#     """Simulate printing each design, until none is left.
#        Move each design to completed_models after printing.
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     """Show all the models that were printed."""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
# completed_models = []

# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)

# PREVENTING A FUNCTION FROM MODIFYING A LIST
# In case the original list needs to be kept.
# Send a copy of a list to a function like this:

#function_name(list_name[:])

# TRY IT MYSELF

# #1 Messages
# short_messages = ["We Are The World", "One More Night", "Could You Be Loved"]
# def show_messages(short_messages):
#     """Show some short messages"""

#     for message in short_messages:
#         print(message)

# show_messages(short_messages)

# #2 Sending Messages

# def sending_messages(short_messages, sent_messages):
#     """Print  and send a message to different list."""

#     while short_messages:
#         sending = short_messages.pop()
#         sent_messages.append(sending)

# def send_messages(sent_messages):
#     for message in sent_messages:
#         print(message)

# short_messages = short_messages = ["We Are The World",
#                                    "One More Night", "Could You Be Loved"]
# sent_messages = []

# sending_messages(short_messages, sent_messages)
# send_messages(sent_messages)

short_messages = ["We Are The World", "One More Night",
            "Could You Be Loved"]

sent_messages = []

while short_messages:
    messages = short_messages.pop()
    sent_messages.append(messages)


    for message in sent_messages:
          print(f"\n{message}")

def send_message(short_messages, sent_messages):
    """Getting message one by one"""
# First part takes from the list of items by taking
# one by one item using a while loop

    while short_messages:
        message = short_messages.pop()
        print(f"\nThese are the messages "
              f"to be sent to our clients:\n\t{message}")
        sent_messages.append(message)

# Second part displays those items that have been fetched
# from the list using a for loop

def already_sent_messages(sent_messages):
    """Display those messages that have been sent."""
    print("\nThese are sent messages")
    for sent_message in sent_messages:
        print(f"\n{sent_message}")

# Third part is going to provide the lists for fucntions to work with
short_messages = ["We Are The World", "One More Night",
            "Could You Be Loved"]

sent_messages = []

# Fourth part calls both functions
send_message(short_messages, sent_messages)
already_sent_messages(sent_messages)
# Right now I do not understand how this is simple.

#3 Archived Messages:

def send_message(short_messages, sent_messages):
    """Getting message one by one"""
# First part takes from the list of items by taking
# one by one item using a while loop

    while short_messages:
        message = short_messages.pop()
        print(f"\nThese are the messages "
              f"to be sent to our clients:\n\t{message}")
        sent_messages.append(message)

# Second part displays those items that have been fetched
# from the list using a for loop

def already_sent_messages(sent_messages):
    """Display those messages that have been sent."""
    print("\nThese are sent messages")
    for sent_message in sent_messages:
        print(f"\n{sent_message}")

# Third part is going to provide the lists for fucntions to work with
short_messages = ["We Are The World", "One More Night",
            "Could You Be Loved"]

sent_messages = []

# Fourth part calls both functions
send_message(short_messages[:], sent_messages)
already_sent_messages(sent_messages)
# I do not undertand why the arguments have to be the same parameters
# It is kind of confusing to me
print(short_messages)

# PASSING AN ARBITRARY NUMBER OF ARGUMENTS
# Giving the option of including as many arguments as need

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following topping:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")

# MIXING POSITIONAL AND ARBITRARY ARGUMENTS

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")

# USING ARBITRARY KEYWORD ARGUMENTS
# Giving the option of accepting as many parameters as possible

def build_profile(first, last , **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first_name"] = first # Why did we need to add this again ?
    # Because we want the output to be consistent: dictionary
    user_info["last_name"] = last
    return user_info

user_profile = build_profile(
    "albert","einstein",
    location = "princeton",
    field = "physics",
    invention = "theory of relativity"
    )

print(user_profile)

#TRYING IT MYSELF

#1 SANDWICHES:

def make_sandwich(*stuffings):
    """Making a sandwich"""
    print("\nThis is what will be included in your sandwich:")

    for stuffing in stuffings:
      print(f"\t-{stuffing.title()}")

make_sandwich("tunna", "cheese", "sliced tomato", "ham")
make_sandwich("lettuce", "fried egg")
make_sandwich("diced cucumbers", "onions", "boiled egg")

print()

#2 USER PROFILE

def build_my_profile(first, last, **info):
    """Build my profile using a function."""
    info["first_name"] = first
    info["last_name"] = last
    return info

my_profile = build_my_profile(
                 "aime",
                 "yeh",
                 field= "engineering",
                 hobby= ["movies","parkour", "reading", "bass guitar"]
                 )
print(my_profile)

#3 CARS VROOOOM!



# STORING FUNCTIONS IN MODULES
# Relevant notes and exercises in the following files: making_pizaa.py, pizza.py
# printing_functions.py and printing_models.py

#SUMMARY
# Write functions and pass arguments
# Positional and keyword arguments
# Accept arbitrary number of of arguments
# Functions that disp;ay output and functions that return values
# Use functions with lists, dictionaries,
# if statements(for setting conditions to exit loops),and while loops
# Store files in a different files called modules
# Styling functions





