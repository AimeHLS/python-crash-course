# #What to expect:
# # 1. Know how to use input() function in appropriate ways
# # 2. Prompt the user for required input type
# # 3. Keep the program running as long as users want them to,
# # so that they can enter information as they need to
# # 4. Python while loops

# # HOW THE input() FUNCTION WORKS

# # Get the first joke from the user

# message = input("Tell me something funny, and I will tell you something "
#                 "even more funny: ")
# print(f"\nI found this to be interesting. Tell me,"
#       f" why did the chicken cross the road?")

# # Get the user's response (second joke)
# response = input("Enter your answer: ")

# # Print the second joke
# print(f"\nAh, I see! The chicken crossed the road because it wanted to "
#      "get to the other side. Classic! 😄")

# print()

# def tell_joke():
#     """Function to get a joke from the user."""
#     user_joke = input("Tell me a joke: ")
#     print(f"Ha! That's a good one. Now it's my turn!")

# def respond_to_joke():
#     """Function to respond with a joke."""
#     print("Why did the scarecrow win an award?")
#     input("Press Enter to reveal the answer...")  # Wait for user input
#     print("Because he was outstanding in his field! 🌾")

# # Main interaction loop
# while True:
#     tell_joke()
#     respond_to_joke()

#     # Ask if the user wants to continue
#     another_round = input("Do you want to exchange more jokes? (yes/no): ")
#     if another_round.lower() != "yes":
#         print("Thanks for the laughs! Have a great day!")
#         break

# # prompt = "if you share your name, we can personalize this message you see."
# # prompt += "\n what is your name?"
# # name = input(prompt)
# # print(f"\nHello, {name}!")

# #First of all how does this work? I do not understand it at all.

# # USING int() to ACCEPT NUMERICAL INPUT

# # checking whethe people are tall enough to ride a rollercoaster
# height = input("How tall are you, in inches?")
# height = int(height)

# if height >= 48:
#     print("\nYou are tall enough to ride!")
# else:
#     print("You will be able to ride when you are a little older.")
# Be sure to convert input value from string to a numerical representation.

#THE MODULO OPERATOR: a useful numerical information  (%)
# This can be used to determine whether the number is odd or even.
# When the number is even, it returns 0 and when the number is odd, the function
# gives the remainder.
#Q: Of what use is this?

#even_or_odd
number = input("Enter a number, and I'll tell you if it's even or odd: ")
try:
    number = int(number)

    if number % 2 == 0:
      print(f"\nThe number {number} is even.")
    else:
      print(f"\nThe number {number} is odd.")
except ValueError:
    print("Invalid input. Please input a valid integer.")
#TRY UT MYSELF

print()

print("welcome to our rental car services."
      "\n\nPlease tell me what car are you looking for. ")

car = input( "\nI am looking for: ")

print(f"\n Let me see if I can find you a {car}")

print()

print("Welocome to our Restaurant.""\n\nPlease tell me how many people are you so that I can find a table for you.")

dinners = input("We are: ")
dinners = int(dinners)

if dinners <= 8:
    print("Go inside there will be a table waiting for you.")
else:
    print("Please wait a moment as make a bigger table ready for you.")


print("Enter a number then I will tell you whether or not it is a multiple of ten.")

user_input = ("Number: ")

try:
    number = int(user_input)

    if number % 10 == 0:
        print(f"{number} is a multiple of ten.")
    else:
        print(f"{number} is not a multiple of ten.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

