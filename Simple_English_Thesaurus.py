''' This project is an example of a simple English Thesaurus
    A word is taken as input and if its meaning is available in the data file,
    its meaning is displayed on the screen'''

# Importing libraries
import json
from difflib import get_close_matches

# Reading the json file
data = json.load(open("data.json"))

# print(type(data))
# print(data["rain"])


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        ch = input("Did you mean %s instead? Enter Y if yes and N if no: " % get_close_matches(w, data.keys())[0])
        if ch == 'Y':
            return data[get_close_matches(w,data.keys())[0]]
        elif ch == 'N':
            return "The word doesn't exist"
        else:
            return "We did not understand your query"
    else:
        return "The word does not exist"


word = input("Enter a word: ")
output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
