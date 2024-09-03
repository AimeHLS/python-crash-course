heading = "Message to Eric"
print(heading)

message = "\nHey, would you like to learn some Python today?"
print(message)

print()

heading_upper = heading.upper()
print(heading_upper)

print()

message_sentence = message.title()
print(message_sentence)

print()

heading_lower = heading.lower()
print(heading_lower)    

Quote = 'Nietzche said, "what doesn\'t kill you makes you strong"'
print(Quote)

name = " \tYeho_Aim"
print(name)
print(name.strip())

# I do not understand how these fuunctions work. I can get python to strip off the white space. 
# I figured it out. It is because I was not using the function inside print command
removing_items = "www.pyhton_notes.txt"
print(removing_items.removeprefix("www."))
print(removing_items.removesuffix(".txt"))