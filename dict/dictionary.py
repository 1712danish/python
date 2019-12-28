import json
from difflib import get_close_matches

data=json.load(open("dictionary.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        yn = input("Did you mean %s instead?Enter Y if yes and N if no: " % get_close_matches(w,data.keys())[0])
        if yn=='Y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=='N':
            return "The word doesnt exist. Please double check it."  
        else:
            return "Sorry we did'nt understand your entry."      
    else:
        return "The word does'nt exist. Please double check it."    


word = input('Enter: ')
output=translate(word)

if type(output)==list:
    for item in list:
        print(item)
else:
    print(output)        