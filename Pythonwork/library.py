import random
from random import randint
print(randint(1, 10))

from random import choice
players = ["charles", "martin", "michael", "nemma","eli"]
first_up = choice(players)
print(first_up)


class Die:
    """Simulate random outcome on a dice."""

    def __init__(self,sides):
        """Initializing attribute"""
        self.sides = sides


    def roll_dice(self):
        """Showing which side after rolling a dice."""

        print(randint(1, self.sides))

# Create a 6-sided die
six_sided_die = Die(10)

#Roll the 6-sided die 10 times with a while loop
count = 0
while count < 20:
    six_sided_die.roll_dice()
    count += 1



tickets = ["A", "B", "C", "D", 1, 2, 3, 4]
prizes = ["400$", "100$", "10$", "car",
          "T-shirt", "air jordan", "motorbike", "house"]

# Create a dictionary to map tickets to prizes
lottery_dict = dict(zip(tickets, prizes))

# Check if the ticket is in the dictionary and print the corresponding prize
for ticket in tickets:
    if ticket in lottery_dict:
        print(f"If your ticket reads {ticket},"
             f"you have won {lottery_dict[ticket]}")

tickets = ["A", "B", "C", "D", 1, 2, 3, 4]
prizes = ["400$", "100$", "10$", "car",
          "T-shirt", "air jordan", "motorbike", "house"]

# Create a dictionary to map tickets to prizes
lottery_dict = dict(zip(tickets, prizes))

# Take user input for the ticket
# user_ticket = input("Enter the ticket you have: ")

# Check if the user's ticket is in the dictionary and
# # print the corresponding prize
# if user_ticket in lottery_dict:
#     print(f"If your ticket reads "
#           f"{user_ticket}, you have won {lottery_dict[user_ticket]}")
# else:
#     print("Sorry, your ticket is not a winning ticket.")


bulk_ticket = (1,2,3,4,5,6,7,8,9,10,"A","B","C","D")
winners = (3,5,8,"D")
print("\nAny ticket matching these numbers or letters is the winner.")
for winner in winners:
    print(winner)

print()
count = 0
while count < 15:
    print(choice(bulk_ticket))
    count += 1




# Define a list containing 10 numbers and 5 letters
lottery_numbers_letters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Randomly select 4 numbers or letters from the list
winning_ticket = random.sample(lottery_numbers_letters, 4)

# Print the winning ticket
print("The winning ticket is:", winning_ticket)

# Define my_ticket
my_ticket = [1, 'A', 5, 9]

# Initialize a counter for the number of iterations
num_iterations = 0

# Loop until my_ticket wins
while True:
    # Randomly select 4 numbers or letters
    drawn_ticket = random.sample(lottery_numbers_letters, 4)

    # Increment the counter
    num_iterations += 1

    # Check if the drawn ticket matches my_ticket
    if drawn_ticket == my_ticket:
        print(f"Congratulations! Your {my_ticket} ticket have won the lottery!")
        print("Number of iterations:", num_iterations)
        break
