import json
from difflib import get_close_matches as match

def dictionary(word):
    word = word.lower()
    if(word in data):
        return data[word]
    elif(len(match(word,data.keys(),cutoff=0.8)) > 0):
        answer =input("Did you mean '%s' ?Y/N" % match(word,data.keys())[0])
        if(answer == "Y"):
            return data[match(word,data.keys())[0]]
        elif(answer == "N"):
            print("The word does not exists.\n")
        else:
            return "Error!"
    else:
        return "The word does not exists.\n"

data = json.load(open("data.json"))

word = input("Enter Word:")
output = dictionary(word)
if(type(output) == list):
    for i in output:
        print(i)
else:
    print(output)