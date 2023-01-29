import json
data = json.load(open("data.json"))
def dictionary(word):  # Run, RuN, RUN
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word. upper() in data:
        return data[word.upper()]
    else:
        return "The word is not in our DB"
