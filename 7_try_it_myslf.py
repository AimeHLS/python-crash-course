# # HERE TO TRY IT MYSELF

# #1 PIZZA TOPPINGS

# print("\nPlease tell us what topping you would like for your pizza."
# "\n Enter 'none' once you have finished.")
# message_user = "\nI  would like: "

# while True:
#     topping = input(message_user)
#     if topping.lower().strip() == "none":
#         break
#     else:
#         print(f"Topping ({topping.title()}) will be added to your pizza.")
#         continue

# print("Thank for helping us customize your pizza.")

# print()

# print("\nPlease tell us what topping you would like for your pizza."
# "\n\nEnter 'none' once you have finished.")

# message_user = "\n\tI  would like: "

# more_toppings = True

# while more_toppings:
#     topping = input(message_user)

#     if topping.lower().strip() == "none":
#         print("\nGot it ✓. Your pizza 🍕 will be customized accordingly 😎")
#         more_toppings = False

#     else:
#         print(f"\nTopping ({topping.title()}) will be added to your pizza.")

# print("\nThank you for helping us customize your pizza🍕.")

# #2 MOVIE TICKETS

# print("\nWelcome to LMY movie theater."
#       "To see the price tickets, please tell us your age.")
# print("\nEnter done once you have finished checking the price of the tickets.")

# while True:
#     age_input = input("\n\tI am: ")

#     if age_input.lower().strip() == "done":
#         break
# #Extract the numeric part from the input(this is amazing)
#     age_parts = age_input.split()
#     for part in age_parts:
#         if part.isdigit():
#             age = int(part)
#             break
#         else:
#             print("Invalid input. Pleae enter a valid age.")

#     if age <= 3:
#         print("Your ticket price is **$0**.")

#     elif age <= 12:
#        print("Your ticket price is **$10**.")

#     else:
#         print("Your ticket price is **$15**.")

# print("Thank you for shopping with us.")

# prompt = "Tell us what would you like to add on your pizza. And enter 'ok' "
# "once you are done: "
# pizza_topping = ""

# prompt = "Tell us what you would like to add to your pizza. "
# "Enter 'OK' once you are done: "
# pizza_topping = ""

# while pizza_topping.lower().strip() != "ok":
#     pizza_topping = input(prompt)
#     print(f"Got it. {pizza_topping.title()} will be added to your pizza")

# print("Thank you for customizing your pizza")


# # while AND LISTS

# sandwiches = [
#     "turkey sandwich",
#     "ham sandwich",
#     "egg sandwich",
#     "tuna sandwich"
# ]
# finished_sandwiches = []

# while sandwiches:
#     making = sandwiches.pop()
#     print("\nMaking:")
#     print(f"\n\t{making.title()}")
#     finished_sandwiches.append(making)

# print(finished_sandwiches)
# print(sandwiches)
# print("\nThese are finished sandwiches:")
# for finished_sand in finished_sandwiches:
#     print(f"\n\t{finished_sand.title()}")

print()

sandwiches = [
    "pastrami",
    "ham sandwich",
    "egg sandwich",
    "pastrami",
    "tuna sandwich",
    "pastrami"
]

# Initialize an empty list for finished sandwiches
finished_sandwiches = []

print("Sorry! We have run out of pastrami.\n\nThese are on the menu:")

for sandwich in sandwiches:
    if sandwich == "pastrami":
        continue
    else:
        print(sandwich.title())

while sandwiches:
    current_sandwich = sandwiches.pop()
    if current_sandwich.lower() == "pastrami":
        continue
    else:
        print(f"\nMaking:\n\t{current_sandwich.title()}")
        finished_sandwiches.append(current_sandwich)

print("\nThese are finished sandwiches:")
for finished_sand in finished_sandwiches:
    print(f"\n\t{finished_sand.title()}")


# while LOOP and DICTIONARY

vactions = {}

polling = True

while polling:
    person = input("\nPlease tell us your name: ")
    place = input("\nIf you could visit on place in the world,"
                  " where would you go? ")

    vactions[person] = place

    another = input("Any other place? (yes/no)")
    if another.lower().strip() == "no":
        polling = False
print("\nThese are the names of the people who participated in the poll and "
      "the places they would like to visit")

for person,place in vactions.items():
    print(f"\n{person.title()} would like to visit {place.title()}")

print()

vacations = {}

while True:
    person = input("\nPlease tell us your name: ")
    places = []
    while True:
        place = input("\nIf you could visit one place in the world, "
                      "where would you go? ")
        places.append(place)
        another = input("Any other place? (yes/no)")
        if another.lower().strip() == "no":
            break

    vacations[person] = places

    more_people = input("Is there another person "
                        "who would like to participate? (yes/no)")
    if more_people.lower().strip() == "no":
        break

print("\nThese are the names of the people who participated in the poll "
      "and the places they would like to visit:")

for person, places in vacations.items():
    if len(places) == 1:
        print(f"\n{person.title()} would like to visit {places[0].title()}")
    else:
        print(f"\n{person.title()} would like to visit "
              f"{', '.join([p.title() for p in places[:-1]])} and"
              f" {places[-1].title()}")





