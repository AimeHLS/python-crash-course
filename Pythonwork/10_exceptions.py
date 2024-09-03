from pathlib import Path

# Exceptions: Making sure incase of an error, users sees a friendly message
#             instead of a traceback

# Handling the ZeroDivisionError Exception

# print(5/0)

# This will stop the code from running, so we need to provide
# some fallback in the case of an error:


# USING try-except BLOCKS
try:
    print(5/0)
except ZeroDivisionError:
    print("\nYou can't divide by zero.")

# USING EXCEPTIONS TO PREVENT CRASHES
# Case scenario: working with user inputs

# print("Give me two numbers, and I will divide them.")
# print("Enter 'q' to quit.")

# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     answer = int(first_number)/int(second_number)
#     print(answer)

# This code does nothing to handle errors, in case a user ask python to divide
# by zero, then the program will crash and give a traceback error.


# Do this instead
# THE ELSE BLOCK

print("\nGive me two numbers, and I will divide them.")
print("Enter 'q' to quit.")


while True:
    first_number = input("\nFirst number: ")
    if first_number.lower().strip() == 'q':
        break
    second_number = input("Second number: ")
    if second_number.lower().strip()  == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)

    except ZeroDivisionError:
        print("You can't divide by zero.")

    except ValueError:
        print("Please input a valid number")

    else:
        print(answer)


# HANDLING THE FileNotFoundError EXCEPTION
path = Path("alice30.txt")
try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"\nSorry, the file {path} does not exist.")


# ANALYZING TEXT

path = Path("tale_two_cities.txt")
try:
    contents = path.read_text()
except FileNotFoundError:
    print(f"\nSorry, the file {path} does not exist.")
else:
    words = contents.split()
    numb_words = len(words)
    print(f"\nThe file alice30 has about {numb_words} words.")

# WORKING WITH MULTIPLE FILES



def count_words(path):
    """Count the approximate number of words in a file."""

    try:
        contents = path.read_text(encoding="utf-8")

    except FileNotFoundError:
        # pass
        print(f"\nSorry, the file {path} does not exist.")

    else:
        words = contents.split()
        numb_words = len(words)
        print(f"\nThe file alice30 has about {numb_words} words.")

filenames = [

            "alice30.txt",
             "tale_two_cities.text",
             "moby_dick.text",
             "litte_women.text"
             ]
for filename in filenames:
    path = Path(filename)
    count_words(path)

# FAILING SILENTLY
# sometimes it is notneccessary to let users know about errors in the program
# rather than printing a messae in except block, I can use pass to let python
# continue.
# The rule of thumb for deciding when to inform users is this: do not provide
# users with unnecessary information.

#TRY IT MYSELF

print("\nGive me two numbers and I will add them for you.\nType exit to finish.")


while True:
    first = input("\nFirst number: ")
    if first.lower().strip() == "exit":
       break

    second = input("\nSecond number: ")
    if second.lower().strip() == "exit":
      break
    try:
        answer = int(first) + int(second)
    except ValueError:
        print("Please input numbers only.")
    else:
        print(f"You have given {first} plus {second}. The answer is: {answer}")







