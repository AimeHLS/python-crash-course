from pathlib import Path
import json

# TRY IT MYSELF
path = Path('fav_num.json')
with open (path, 'w') as file:
    file.write_text(path)

with open(path) as file:
    content = file.read()

print(f"I know your favorite number is {content}")


# fav_num = input("Tell your favorite number: ")
# stored = Path('fav_num.json')
# placed = json.dumps(fav_num)
# content_00 = stored.write_text(placed)

# print(f"I know your favorite number is {content_00}")



fav_food = input("Tell your favorite food: ") # Get user input
path = Path('fav_food.json') # Make a path for it
store_input = json.dumps(fav_food) # dump data into memory
content_11 = path.write_text(store_input)

print(f"I know that your favorite food is {content_11}")
