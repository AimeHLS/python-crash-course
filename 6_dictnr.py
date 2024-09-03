# Dictionaries are used to connect pieces of related information.
# A collection of key-value pairs

# SIMPLE DICTIONARY

alien_0 = {"color":"green", "points": 5}

print(alien_0["color"])
print(alien_0["points"])

# WORKING WITH DICTIONARIES

new_points = alien_0["points"]
print(f"You have just earned {new_points} points!")
# Remember to return to those exercises.

# ADDING NEW key-value PAIRS

print(alien_0)
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

# STARTING WITH AN EMPTY DICTIONARY

alien_0 = {}

print(alien_0)

alien_0["color"] = "green"
alien_0["points"] = 5
alien_0["x_position"] = 4
alien_0["y_position"] = 20

print(alien_0)

# MODIFYING VALUES IN A DICTIONARY

print(f"\nThe alien is {alien_0["color"]}.")

alien_0["color"] = "yellow"
print(f"\nThe alien is now {alien_0['color']}.\n")

#let's track the position of an alien that can move at different speeds.

alien_1 = {"x_position":4, "y_position":22, "speed":"slow"}
print(f"Original positon: {alien_1['x_position']}")
alien_3 = {"y_position":5, "speed": "fast"}

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_1["speed"] == "slow":
    x_increment = 1
    y_increment = 2
    #you can have multiple inputs too, incredible...
elif alien_1["speed"] == "medium":
    x_increment = 2
elif alien_3["speed"] == "fast":
    x_increment = 3

# The new position will be the old position plus the increment.

alien_1["x_position"] = alien_1["x_position"] + x_increment
alien_3["y_position"] = alien_3["y_position"] + x_increment

print(f"New position: {alien_0['x_position']}")

print(f"Right now the new position:{alien_1['x_position']} ")
print(f"This is the fastest alien: {alien_3['y_position']}")

# REMOVING key-value PAIRS

print()
alien_0 = {"color": "green", "points": 6}
print(alien_0)

print()
del alien_0 ["points"]
print(alien_0)
# The deleted value is removed permanently.

# A DICTIONARY OF SIMILAR OBJECTS

poll_fav_languages = {
"jen" : "python",
"sam" : "c",
"eddy" : "rust",
"fidel" : "python"
}

print()

for name, language in poll_fav_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
    print()
#Proudly, this could the best piece of code I have ever written

# USING get() to ACCESS VALUES

print()
point_value = alien_3.get("x_position", "Not assigned yet.")
point_value_1 = alien_3.get("y_position", "Not assigned yet.")
print(point_value)
print(point_value_1)
# if you suspect that the key being looked for does not exist,
# use get() method rather than square bracket notation

# TIME TO TRY IT MYSELF

print()

friend_Idk = {
    "name" : "dominic",
    "last_name" : "lumba",
    "age" : 45,
    "city" : "kigali"
}

print(friend_Idk.get("name"))
print(friend_Idk.get("last_name"))
print(friend_Idk.get("age"))
print(friend_Idk.get("city"))

print(f"My friend {friend_Idk.get("name").title()} "
      f"lives in {friend_Idk.get("city").title()}")

people_fav_nmbrs = {
    "carol" : 12,
    "keycee" : 23,
    "costa" : 6,
    "aime" : 64,
    "lewis" : 500
}

print()

for person, number in people_fav_nmbrs.items():
    print(f"I know for sure {person.title()}'s favorite number is {number}.")
    print()

glossary = {
    "string" : "a chain of the words/sentence.",

    "boolean" : "a statement whether something is right or wrong.",

    "list" : "a group of items kept together using square brackets",

    "dictionary" : "a list of items kept together using braces and colon",

    "tuple" :
        "a list of items grouped together using brackets. it cannot be changed",

    "set" :
        "a group of items that is used to avoid duplicates, it also used braces"
}

print()

for word, meaning in glossary.items():
    print(f"\n A {word.title()} is {meaning}")

# LOOPING THROUGH A DICTIONARY

#1 Looping Through All key-value pairs

user_0 = {
    "username" : "ifeuba",
    "first name" : "enrique",
    "last name" : "iglesias"
}

print()

for k, v in user_0.items():
    print(f"\nKey : {k.title()};")
    print(f"\nValue: {v.title()}")

#2 Looping Through All Keys in a Dictionary

print()

poll_fav_languages_0 = {
"john" : "html",
"eliott" : "Javascript",
"felix" : "python"
}


for name in poll_fav_languages_0.keys():
    print(name.title())
print("Looping through all the keys")
# The default here is to print keys(). I can use it or omit it.
# I can also use the method values () to make python print values

print()
friends = ["john", "eliott", "janette" ]

poll_fav_languages_0 = {
    "john" : "java",
    "eliott" : "Javascript",
    "felix" : "python",
    "jake" : "python",
    "roland" : "c++"
}

friends = ["john", "eliott", "janette"]

for name in poll_fav_languages_0.keys():
    print(f"\nHi {name.title()}!")
    if name in friends:
        print(f"\t{name.title()} I see you love "
              f"{poll_fav_languages_0[name].title()}!")

for friend in friends:
    if friend not in poll_fav_languages_0:
        print(f"\nHi {friend.title()}, please take a poll"
              " and tell us your favorite programming language")

#3 Looping Through a Dictionary in a Particular Order
print()
for name in sorted(poll_fav_languages_0.keys()):
    print(f"\n{name.title()}, thank you for taking the poll.")

#4 Looping Through All the Values in a Dictionary
# Nothing new. replace .key() with .value()

print("\n\nThe following languages have been mentioned: \n")

for language in poll_fav_languages_0.values():
    print(language.title())
    print()

# Use set() to avoid duplicates when looping through values.
# A set is a collection of values where each item must be unique.
print("\n\nThe following languages have been mentioned: \n")

for language in set(poll_fav_languages_0.values()):
    print(language.title())
    print()
# I noticed that the value Python came only once in the results

# This is a set
languages = {"python", "rust", "python", "rust", "c"}
print(languages)

#TIME TO TRY IT MYSELF

rivers = {"nile": "egypt", "akagera": "rwanda", "zamabezi": "zambia"}

# for river, country in rivers.items():
#     print(f"\n{river.title()} river runs through {country.title()}.")

# print()

# for river in rivers.keys():
#     print(river.title())
#     print()

# print()

# for country in rivers.values():
#     print(country.title())
#     print()


for river, country in rivers.items():
    print(f"\n{river.title()} river runs through {country.title()}.")
    print(f"River: {river.title()}")
    print(f"Country: {country.title()}\n")

print()

rivers = {"nile": "egypt", "akagera": "rwanda", "zamabezi": "zambia"}

formatted_strings = []
keys = []
values = []

for river, country in rivers.items():
    formatted_strings.append(f"{river.title()} river runs through"
                             f"{country.title()}.")
    keys.append(river.title())
    values.append(country.title())

print("Formatted Strings:")
for string in formatted_strings:
    print(string)

print("\nKeys:")
for key in keys:
    print(key)

print("\nValues:")
for value in values:
    print(value)
# I do not quite get this one right now. But will retun to check...
# there is a fucntion I used in the lists of adding things in
# the list one by one? printing the list separated with a comma.
# But I do not remember it
print()
polling = {
    "jojo" : "python",
    "jimmy" : "rust",
    "john" : "java",
    "johnson" : "c"
}

waiting_poll = ["raymond","rudy","sean", "jojo", "johson"]

for person in polling.keys():
    print(f"\n{person.title()}, Thank you for participating in this poll.")


for friend in waiting_poll:
    if friend not in polling:
        print(f"\n{friend.title()}, please take the poll.")



#  NESTING:

# Storing multiple dictionaries in a list or list of items
# in as a value in a dictionary or a dictionary inside a dictionary.

#1 A LIST OF DICTIONARIES

alien_0 = {"color" : "green" , "points" : 5}
alien_1 = {"color" : "yellow" , "points" : 4}
alien_2 = {"color" : "red" , "points" : 8}

aliens_list = [alien_0, alien_1, alien_2]

print()
for alien in aliens_list:
    print(alien)

# A more realistic example. we  use range to creat a fleet of 30 aliens

#1  Make an empty list  for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {"color" : "green", "points" : 5, "speed" : "slow"}
    aliens.append(new_alien)

# 3 Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# 4 Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)} ")

# How to work with this kind of list: though they have the same characteristics,
# python sees each alien as a unique object.
# this gives a chance to change anything alien we want in the list as we wish

# For example change the first three aliens to yellow.
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
        print(alien)
    elif alien["color"] == "yellow":
         alien["color"] = "red"
         alien["speed"] = "fast"
         alien["points"] = 15
         print(alien)

#2 A LIST IN A DICTIONARY

#1 Store Information About a Pizza Being Ordered
pizza = {
    "crust" : "thick" ,
    "toppings" : ["mushrooms, extra cheese"]
}

#2 Summarize the Order
print(f"\nYou have orderd a {pizza["crust"]}-crust pizza "
        "with the following toppings:")
for topping in pizza["toppings"]:
    print(f"\t{topping}")

print()
print()

fav_languages = {
    "jimmy"  : ["python", "rust"],
    "tony" : ["c"],
    "edwin" : ["rust", "go"],
    "peter" : ["python", "haskell"]
}

for name, languages in fav_languages.items():
    if len(languages) ==1:
      print(f"\n{name.title()}'s favorite language is:")
      for language in languages:
        print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
           print(f"\t{language.title()}")

#Note: It is not recommended to nest lists and dictionaries too deeply.
#If nesting has to be deeper, there must be simple ways to solve the problem

#3 A DICTIONARY IN A DICTIONARY

#Note that the code will get complicated very quickly.

#Example: several website users

users = {
    "aeinstein": {
        "first" : " albert" ,
        "last" : "einstein" ,
        "location" : "princenton"
    },

    "mcurie" : {
        "first" : "marie" ,
        "last" : "curie" ,
        "location" : "paris"

    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info["first"]} {user_info["last"]}"
    location = user_info["location"]

    print(f"\n\tFullname: {full_name.title()}")
    print(f"\n\tLocation: {location.title()}")

#TRY IT MYSELF

#1 people

applicants = {

    "dianna" : {

    "first" : "dianna",
    "last" : "lumba",
    "age" : 45,
    "gender" : "female",
    "city" : "kigali"

} ,
    "nikitta" : {
        "first" : "nikitta",
        "last" : "kulchev",
        "age" : "82",
          "gender" :"male",
        "city" : "moscow"
    }

    }

for applicant, appl_info in applicants.items():
    name = f"{appl_info["first"]} " f"{appl_info["last"]}"
    age = f"{appl_info["age"]}"
    gender = f"{appl_info["gender"]}"
    location = f"{appl_info["city"]}"

    print(f"\nName: {name.title()}")
    print(f"\tAge:{age}")
    print(f"\tGender: {gender.title()}")
    print(f"\tLocation: {location.title()}")

pet_0 = {

    "type" : "dog",
    "owner" : "alice" ,
    "age" : "2years old",
    "breed" :  "german shepherd",
    "health" : "good"
}

pet_1 = {

    "type" : "dog",
    "owner" : "mr.Smith" ,
    "age" : "3 years old",
    "breed" :  "pitbul ",
    "health" : "allergic to diary"
}

pet_2 = {

    "type" : "cat",
    "owner" : "ms.siyu" ,
    "age" : "5 years old",
    "breed" :  "not known ",
    "health" : "good"
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(pet)
#In order to clean the print, it is better to nest these dictionaries into
# a dictionary called pets

# Define the pets dictionary
pets = {
    "pet_0": {
        "type": "dog",
        "owner": "alice",
        "age": "2 years old",
        "breed": "german shepherd",
        "health": "good"
    },
    "pet_1": {
        "type": "dog",
        "owner": "mr. Smith",
        "age": "3 years old",
        "breed": "pitbull",
        "health": "allergic to dairy"
    },
    "pet_2": {
        "type": "cat",
        "owner": "ms. siyu",
        "age": "5 years old",
        "breed": "not known",
        "health": "good"
    }
}

# Iterate over each pet and print the information
for pet_id, pet_info in pets.items():
    print(f"\n{pet_id}:")
    print(f"Type: {pet_info['type'].title()}")
    print(f"Owner: {pet_info['owner'].title()}")
    print(f"Age: {pet_info['age']}")
    print(f"Breed: {pet_info['breed'].title()}")
    print(f"Health: {pet_info['health'].title()}")
    print()  # Add an empty line for better readability



favorite_places = {

    "aime" : [
        "tianjin city",
        "doha",
        "kigali"
    ] ,

    "bosco" : [
        "johannesburg",
        "zanzibar",
        "nairobi"
    ] ,

    "richard" : [
        "thailad",
        "mexico city"
    ]
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are: ")
    for place in places:
        print(f"\t{place.title()}")

favorite_numbers = {
    "carol" : [12,23,27] ,
    "keycee" : [23, 45, 69] ,
    "costa" : [6,2,3,4],
    "aime" : [64, 1],
    "lewis" : [500, 1000000]
}
for person, numbers in favorite_numbers.items():
    print(f"\n{person.title()}'s favorite numbers are: ")
    for number in numbers:
        print(f"\t{number}")


cities = {
    "kigali" : {
        "country" : "rwanda",
        "population" : "1.3 millions",
        "fact" : "the cleanest city in africa "

    } ,

    "beijing" : {
        "country" : "china",
        "population" : "22 millions",
        "fact" : "one of  the Oldest cities "
    } ,

    "washington dc" :{
        "country" : "united states of america",
        "population" : " 19.5 millions",
        "fact" : " home of more than 170 embassies and cultural centers"
    }
}

for city, city_info in cities.items():
    print(f"\n{city.title()} is the capital city of "
         f"{city_info["country"].title()}. "
         f"Its population is {city_info["population"]}"
         f" and it is {city_info["fact"]}")

# SUMMARY FOR THIS CHAPTER
# Define dictionary, access and modify individual elements in a dict., loop
#througha all the information in the dict. loop with key-values, keys, values.
# Nest a dicts. in a list, a list in dict. and dict in a dict.

#Upnext: while loops to make my code more interactive