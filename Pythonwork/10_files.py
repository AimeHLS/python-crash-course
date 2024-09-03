import pandas as pd 

# what to expect
# How to handle errors so the program won't crash when they encounter unexpected
# situations : Exceptions

# json module which is used to save user data so it isn't lost when program stops
# running

# READING FROM A FILE

from pathlib import Path
import json

path = Path("pi_digits.txt")
contents = path.read_text().rstrip()
print(contents)

# RELATIVE and ABSOLUTE FILE PATHS
#1 Incase the file being accessed is in in the same folder with the code:
# path = Path("file_name.txt")

#2 Incase the file I want to access in stored in a folder that is stored in the
# same place with python code:
# Path = Path("folder/filename.text")

#3 Not in the same location, I have to tell python where to look:
# path = Path ("/hone/myself/data_files/filename.text")

# ACCESSING A FILE LINES

# If I want to examine each line of the file I shall use: splitlines() method and
# use a for loop to examine each line from a file, one at a time

# for line in contents.splitlines():
#     print(line)

# WORKING WITH FILE CONTENTS

pi_string = " "
for line in contents.splitlines():
    print(line)
    pi_string += line

print(pi_string)
print(len(pi_string))



# Use a variable to import the file/access the file
path_0 = Path("pi_million.txt")

# Read contents of the text
read_file = path_0.read_text()

# Split its contents into individual lines
# lines_pi = read_file.splitlines()

# Use those lines to form a string
string = " "
for line in read_file.splitlines():
    # pick line by line from the reading
    string += line

print(len(string))

# Checking if my birthday is in first pi million digits.
birthday = ("Enter your birthday, in the form mmddyy: ")

if birthday in string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

# TRY IT MYSELF

# Find the text to work with
print()
find_text = Path("learning.txt")

# Read the found text and print it
text = find_text.read_text()
print(text)

print()
# Split the text into lines and print it using a for loop
for line in text.splitlines():
    print(line)


# Change the text into a string(sentence)
text_string = " "
for line in text.splitlines():
    text_string += line

#  Assign the string to a variable and replace Python with C
replaced_text = text_string.replace("Python", "C")
print(f"\n{replaced_text}")

# WRITING TO A FILE
#1 Writing a Single Line

path_1 = Path("programming.text")
path_1.write_text("I am loving programming.")

#2 Writing multiple lines

# Form a long string
talk = "He said I am never gonna let you down.\n"
talk += "Let's eat oranges now.\n"
talk += "I know you will love them.\n"

# Tell python to find the name of file you want to create. If not found, python will create it.
path_2 = Path("Talk.txt")

# Use the string to write into the file
path_2.write_text(talk)

# TRY IT MYSELF

#1 Prompt one user to tell their name and write their name in the file.
new_prompt = input("Please write down your name: ")
users = new_prompt
path_3 = Path("Guest.text")
path_3.write_text(users)

#2 Use a while loop to prompt more users and write their name in the list.

while True:
    print("\nPlease tell us your name and type exit to quit")
    new_prompt = input("Name: ")
    new_user = new_prompt
    if new_prompt.lower().strip() == "exit":
        break

    path_4 = Path("Guest_list.text")
    with open(path_4, "a") as file:
        file.write(new_user.title() + "\n")

print("Guest list updated successfully")


#STORING DATA

#1 USING json.dumps() AND json.loads()

# Store a set of numbers and read them back into memory
numbers = [1,2,3,4,5,6,7,3]
path = Path('numbers.json')
content = json.dumps(numbers)
path.write_text(content)
print(numbers)






