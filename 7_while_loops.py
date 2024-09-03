#INTRODUCING while LOOPS
#Tried to look through the difference between this and for loops...
# I will find out as I go by.

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

#While loops are useful because they keep the program running for as long
# as we want them to. It won't be fun,
# if programs stopped before we tell them to do so.

#LETTING USER CHOOSE WHEN TO QUIT
# parrot = "\n Tell something funny and I will repeat it back to you."
# parrot += "\n\nEnter 'quit' to end the program."

# message = ""
# while message != "quit":
#     message = input(parrot)
#     print(message)

# parrot = "\nTell me something funny, and I will repeat it back to you: "
# parrot += "\nEnter 'quit' to end the program.\n"

# message = ""
# # while message.lower() != "quit":
# #     message = input(parrot)
# #     if message.lower() != "quit":
# #         print(message)
# # Prompt the user for input
# # prompt = "\nTell me something, and I will repeat it back to you: "
# # prompt += "\nEnter 'quit' to end the program. "

# # message = ""
# # while message.lower() != 'quit':
# #     message = input(f"\n{prompt}")
# #     if message.lower() != 'quit':
# #         print(f"\n\t{message.title()}")

# #USING A flag

# #used when checking for multiple conditions that could stop the program.
# For a program that could run as long as many conditions are true,
# the flag is one variable that determines whether or
# not the entire program is active.

# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program. "

# active = True
# message = ""
# while message.lower() != 'quit':
#     message = input(f"\n{prompt}")
#     if message.lower() != 'quit':
#         print(f"\n\t{message.title()}")

# #By adding the flag, we set the condition check prior to everything else
# (I guess I will have to see more of that in the future)

# #USING break TO EXIT A LOOP


# prompt = "\nPlease suggest a name of a city you have visited: "
# prompt += "\nEnter 'quit' when you are finished. "

# while True:
#     city = input(prompt)

#     if city.lower() == "quit":
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

# # It is amazing how LLM are amazing.  THey are so good at debugging.
# # break can be used in any if Python's loop

# # USING continue IN A LOOP

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 ==0:
#         continue

#     print(current_number)

# # AVOIDING INFINITE LOOPS
# # Every while loop needs a way to stop running
# # so it won't continue to run forever.


# print()
# x = 1
# while x <= 5:
#     print(x)
#     x += 1
# If the condition x += 1 is omitted, the program will keep running
# because x <= 5 will always be true.

# TIME TO TRY IT MYSELF

# 1 pizza toppings

# Prompt the user to enter a series of pizza toppings
# until they enter a 'quit' value.


# while True:
#     topping = input("Enter a pizza topping (or 'quit' to finish): ")
#     if topping.lower() == "quit":
#         break
#     print(f"I'll add {topping} to your pizza.")
#     break


#INTRODUCING WHILE LOOPS AGAIN


prompt = "\nTell me something, and I wil repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    if message.lower().strip() == 'quit':
            break
    else:
         print(message)



# I have improved on the code with the help of gpt,
# but still the program is taking too long recognize quit and stop

# Guess a secret number
try:
    secret_number = 7
    guess = 0

    while True:
     guess = secret_number
     guess = int(input("\nGuess the secret number: "))

     if guess < secret_number:
            print("Too low, try again.")
     elif guess > secret_number:
            print("Too high, try again.")
     elif guess == secret_number:
            print("Bravooo! You've guessed the secret number.")
            break

except ValueError:
     print("Invalid input. Please input numbers")


starting = 0
while starting <= 100 :
    print(starting)
    starting += 10


secret_number = 42
max_attempts = 5

print("Welcome to the Guess-the-Number Game!")
print(f"Try to guess the secret number between 1 and 100. "
      f"You have {max_attempts} attempts.")

attempts = 0
game_over = False  # Flag to control the game loop

while not game_over:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print(f"Congratulations! "
              f"You guessed it right ({secret_number}). You win!")
        game_over = True  # Set the flag to end the game
    elif guess < secret_number:
        print("Try a higher number.")
    else:
        print("Try a lower number.")

    if attempts == max_attempts:
        print(f"Sorry, you've reached the maximum attempts."
              f"The secret number was {secret_number}. Game over.")
        game_over = True  # Set the flag to end the game

print()
secret_numb = 75
max_attem = 6

print("This is a guess a number game")
print(f"Try to guess the secret number between 1 and 100. "
      f"You have {max_attem} attempts.")

tries = 0
game_on = True
while game_on:
    guess = int(input("\n\tEnter your guess here: "))
    tries += 1

    if guess == secret_numb:
        print(f"\nCongs! Youu guessed it right {secret_numb}. You win!!")
        game_on = False
    elif guess > secret_numb:
        print("\nTry a Lower number.")
    else:
        print("\nTry a Higher number.")
    if tries == max_attem:
        print(f"\nSorry, you have reached maximum attempts."
              "Please try again.")
        game_on = False

print()

prompt = "\nYou are on a mysterious island. What do you want to do? "
prompt += "\nEnter 'quit' to end the game. "

active = True
while active:
    action = input(prompt)
    if action.lower().strip() == 'quit':
        active = False
    elif action.lower().strip() == 'treasure':
        print("Congratulations! You found the hidden treasure. You win!")
        active = False
    elif action.lower().strip() == 'dragon':
        print("Oh no! You encountered a fearsome dragon. Game over.")
        active = False
    else:
        print("You continue exploring the island...")

# USING break TO EXIT THE LOOP : To exit the loop without running any remaining
#code in the loop.

prompt = "\nEnter the name of the city you have been to."
prompt += "\nEnter 'quit' when you are finished:  "

while True:
    city = input(prompt)

    if city.lower().strip() == "quit":
        break
    else:
        print(f"I'd love to go to {city.title()}!!")
        continue
print("Have you been to any other city?")

# A loop that starts with while True, Will run forever unless it reaches a break
#statement.

# USING continue IN A LOOP: Rather than breaking out of a loop entirely with out
#executing the rest of its code, you can use the continue statement to return to
#the beginning of the loop, based on the result of conditional test.

print()

secret_number = 42
max_attempts = 5

print("Welcome to the Guess-the-Number Game!")
print(f"Try to guess the secret number between 1 and 100."
      f"You have {max_attempts} attempts.")

attempts = 0

while True:  # Infinite loop until explicitly broken
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print(f"Congratulations!"
              f" You guessed it right ({secret_number}). You win!")
        break  # Exit the loop when the correct number is guessed
    elif guess < secret_number:
        print("Try a higher number.")
    else:
        print("Try a lower number.")

    if attempts == max_attempts:
        print(f"Sorry, you've reached the maximum attempts. "
              f"The secret number was {secret_number}. Game over.")
        break  # Exit the loop when max attempts are reached
    else:
        print(f"You have {max_attempts - attempts} attempts left.")
        # Inform remaining attempts
        # continue  # Skip the rest of the loop and start a new iteration

print("Thank you for playing!")
#I don't quite understand the use of continue right now.

number = 0
while number < 10:
    number = number + 1
    if number % 2 == 0:
        continue
    print(number)

