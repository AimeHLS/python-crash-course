
from pathlib import Path
import json

people_string = """
{
    "people": [
        {
            "name": "John Smith",
            "phone": "65757-555",
            "emails": ["johnsmith@email.com", "john.smithbuild@build.com"],
            "has_license": false
        },

        {
            "name": "Jane Doe",
            "phone": "560-555777",
            "emails": null,
            "has_license": true
        }
    ]
}
"""# This will convert to a nested dictionary.

# This is json data/object.
# In the file above, people is "Key" and corresponding data are

#1. WORKING WITH STRINGS

# Loading json string into python
data = json.loads(people_string) # It is helpful to read loads as load string
print(type(data))

for person in data['people']:
    print(person['name'])

# Dump a python object into a json string
for person in data['people']:
    del person['phone']
    new_string = json.dumps(data, indent=2, sort_keys=True)

print(new_string)

#2. WORKING WITH FILES

with open('states.json') as sf: # Load json file to python
    states_data = json.load(sf)

    for state in states_data['states']:
        print(state['name'], state['abbreviation'])# Get the output

    for state in states_data['states']:# Modify the file
        del(state['area_codes'])

with open('new_states_data.json', 'w') as wsf: # Dump modified file to json
    json.dump(states_data, wsf, indent=2)






