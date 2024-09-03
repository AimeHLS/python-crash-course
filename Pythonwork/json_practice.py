import json
from json_data import people_string
from urllib.request import urlopen


data = json.loads(people_string)
# converting json to a python.

for person in data['people']:
    print(person['name'])


# Dump a python object into json string
for person in data['people']:
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)
print(f"\n{new_string}")

# json.load: it takes JSON data from file-like object...
# json.loads: it takes JSON-formatted string as input and converts it
# into a Python data structure

#1 Open the file
with open('states.json') as file:
#2 load the file into a python object
    data = json.load(file)
# for state in data['states']:
        # print(state['name'], state['abbreviation'])

#3 write the python into json
for state in data['states']:
    del state['area_codes']

with open('new_states.json', 'w') as f:
    json.dump(data, f)

   