# PYTHON DICTIONARY

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# retrieving items from a dictionary
print(programming_dictionary["Bug"])

# adding new items to a dictionary
programming_dictionary["loop"] = "the action of doing someting repeatedly by a computer"

print(programming_dictionary)

# create an empty dictionary
programming_dictionary = {}

# modify an item in a computer
programming_dictionary["Bug"] = "a moth in a computer"
print(programming_dictionary)

# loop into a dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


# wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# dictionary nesting
{"country": ["poland", "italy", "nigeria"], "fruits": ["banana", "orange", "strawberry"]}

# nesting a dictionary in a dictionary

travel_log = {
    "country": {"country_visited": ["poland", "italy", "nigeria"], "total_visits": 12},
    "fruits": {"fruits_eaten": ["banana", "orange", "strawberry"], "total": 16},
}

# nesting dictionary inside a list
travel_log = [
    {"travel log": "country", "country_visited": ["poland", "italy", "nigeria"], "total_visits": 12},
    {"fruits": "natural", "fruits_eaten": ["banana", "orange", "strawberry"], "total": 16},
]
