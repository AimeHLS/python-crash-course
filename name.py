# name = 'ada'
# print(name.title())

# first_name = 'ada'
# last_name = 'lovelace'
# full_name = f'{first_name} {last_name}'
# print(first_name)
# print(last_name.title())
# print(full_name.upper())


# greetings = f'Hey, {full_name.title()}!'
# print(greetings)

#Add a tab to the text (\t)
# print('Python')

# print('\tPython')

# #Add a new line in a string (\n)
# print('languages:\nPython\nC\nJavaScript')

# #Combining newlines and tabs in a string("\n\t")
# print('languages:\n\tPython\n\tC\n\tJavaScript')

#Stripping Whitespace
favorite_language = ' Python'
favorite_language.rstrip()
favorite_language = favorite_language.rstrip()
print(favorite_language)

favorite_language = ' python '
favorite_language.rstrip()
fav_lang_nospace = favorite_language.rstrip()
print(fav_lang_nospace)
# this does not make sense, unless it something you start with on the top,
# otherwise why would you want to remove the white space when you already
# know tha it is already there? And how can you see the whitespace
# in the terminal? Also, I do not see any difference with rstrip function.

# Removing Prefixes
nonstarch_url = 'https://nonstarch.com'
nonstarch_url.removeprefix('https://')
simple_url = nonstarch_url.removeprefix('httpss://')
print("simple_url")

#Seems like it does not work with print. But how else am I supposed to see the change?

# use single and double quotes correctly

message = "One of Python's strengtths is its diverse community."
print(message)
