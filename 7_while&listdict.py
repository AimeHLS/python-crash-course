# USING while LOOPS WITH LISTS AND DICTIONARIES

#Can be useful if you want to modify the lists,
# dictionaries as you work through it.
#Since for loops will have trouble identifying the list if it happens to change

# MOVING ITEMS FROM ONE LIST TO ANOTHER
#task: for a website, there newly registered users and verified users.
# But how to move a user from newly registered users to verified users?

#Start with users that need to be verified,
# and an empty list to hold comfirmed users
uncomfirmed_users = ["wonderland", "o'conor", "owens"]
comfirmed_users = []

#verify each user until there are no more uncomfirmed users.
#Move each verified user into the list of comfirmed users.

while uncomfirmed_users:
    current_user = uncomfirmed_users.pop()

    print(f"Verifying... {current_user.title()}")
    # From the last one, users are added one by one.
    # That's why we can print them one after another
    comfirmed_users.append(current_user)

#Display all comfirmed users.
print("\nThis may take a moment...")
for comfirmed_user in comfirmed_users:
    print(f"\n\t{comfirmed_user.title()} is comfirmed.")

#REMOVING ALL INSTANCES OF SPECIFIC VALUES FROM A LIST
# Say you have a lis of pets with "cat" appearing more than once in the list.
print()

pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

# Remove both "cat" and "dog" from the list
# while "cat" in pets or "dog" in pets:

#     pets.remove("cat")
#     pets.remove("dog")

# print(pets)


#FILLING A DICTIONARY WITH USER INPUT

responses = {}
# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    #Prompt for the person's name and response.
    name = input ("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")

    #Store the response in the dictionary.
    responses[name] = response
    # This means: responses(dictionary)has name as keys and response
    # as values of the keys

    #Find out if anyone else is going to take a poll.
    repeat = input("Would you like to let another person respond? (yes/ no)")
    if repeat.lower().strip() == "no":
        polling_active = False

    #Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")

#If you are for getting better at somethings, time is no longer your enemy, but
#becomes your best ally.

# CHAPTER SUMMARY
# Work with both numerical and text input. While loops to make the program run
# as long as the user want them to(tricky,you might end up
# running an infinite loop)
# Ways to control the flow of the while loop:
# active flag, break statement and continue
# Using while loops to move items from one list to another,
# and how to remove all instances of a value from a list.
# Using while loops and dictionaries 