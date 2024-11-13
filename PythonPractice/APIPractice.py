# Using this API endpoint:
#
# http://api.open-notify.org/astros.json
#
# 1) Write a function that returns the number of people in space.
#
# 2) Write a function that given an astronaut name returns the space
# craft that astronaut is on. Handle the case where the name is of a
# person *not* currently in space.
#
# 3) Write a function that given a space craft name return all astronauts
# on that craft. Handle the case where the name is not a valid space
# craft.

import requests
import re

# This function is simply getting the json file from an API endpoint and returning the output as a dictionary for us to parse.
def get_json_file():
    r = requests.get('http://api.open-notify.org/astros.json')
    json_contents = r.json()
    return json_contents

data = get_json_file()

# Gives me a list of dicts, each entry in the list is a dictionary containing info of astronaut name and their ship craft.
def get_people():
    astronauts = data.get("people")
    return astronauts

astronauts_list = get_people()

# Counting the amount of people on a spaceship
def space_count():
    people_count=0
    for people in astronauts_list:
        if people.get("craft") != "none":
            people_count += 1
    return people_count

# Checking if the astronaut is indeed in space, however needs to perfectly match the value. Dynamically, we want to implement regex to try and search and check if an astronaut is in space.
'''
def person_check(astronaut_name,astronauts_list):
    for name in astronauts_list:
        if name.get("name") == astronaut_name:
            craft = name.get("craft")
            return f"{astronaut_name} is currently on the {craft}"
    return f"{astronaut_name} is not currently in space"
'''

# Regex version of person_check function.
def person_check_regex(astronaut_name,astronauts_list):
    for name in astronauts_list:
        if re.search(re.escape(astronaut_name), name.get("name"), re.IGNORECASE):
            astronaut_match = name.get("name")
            craft = name.get("craft")
            return f"{astronaut_match} is currently on the {craft}"
    return f"{astronaut_name} is not currently in space"

def check_ship_personnel(ship_name, astronauts_list):
    personnel = []
    for ship in astronauts_list:
        if re.search(re.escape(ship_name), ship.get("craft"), re.IGNORECASE):
            astronaut_name = ship.get("name")
            personnel.append(astronaut_name)
    if not personnel:
        return f"No personnel found for the ship '{ship_name}'. Please try again with a valid ship name."
    return personnel


count = space_count()
print(count)

astronaut_name = input()
isPerson_in_space = person_check_regex(astronaut_name, astronauts_list)
print(isPerson_in_space)

ship_name = input()
shipPersonnel = check_ship_personnel(ship_name, astronauts_list)
print(shipPersonnel)