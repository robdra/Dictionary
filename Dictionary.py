import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif get_close_matches(word, data.keys(), cutoff=0.8):
        return str(get_close_matches(word, data.keys(), cutoff=0.8)[0]) + ": " + str(data[get_close_matches(word, data.keys())[0]])
    else:
        return "Cant find word"

word = input("Search for: ")

out = meaning(word)

if type(out) == list:
    for item in out:
        print(item)
else:
    print(out)