import random
import requests
import json
import random
nacountries = ['Canada', 'the United States']
global chatting
chatting = 1
keywords = ['sport', 'food', 'eat', 'age', "what's your name",
            'what is your name', 'you called', 'what country',
            'what nation', 'you from', "old are you"]


def name():
    name = requests.get("https://random-data-api.com/api/name/random_name")
    return name.json()['first_name']


def country():
    countries = requests.get("https://random-data-api.com/api/nation/random_nation")
    localiseChance = random.random()
    if localiseChance <= 0.1:  # 10% chance to have something other than NA as their home country
        return f"I am from {countries.json()['nationality']}."
    elif 0.1 < localiseChance < 0.3:  # 20% chance to have immigrated to NA
        return f"I came from {countries.json()['nationality']} to {random.choice(nacountries)}."
    else:
        return f"I am from {random.choice(nacountries)}."


def language():
    countries = requests.get("https://random-data-api.com/api/nation/random_nation")
    localiseChance = random.random()
    if localiseChance <= 0.1:  # 10% chance to have something other than English as their main language
        return f"{countries.json()['language']} and some English"
    elif 0.1 < localiseChance < 0.3:  # 20% chance to have 2 languages, including English as their main language.
        return f"English and {countries.json()['language']}"
    else:
        return "English"


def keyword(ui):
    for i in keywords:
        if i in ui:
            return response(i)


def response(kword):
    burh = {"sport": xsport,
            "food": xfood,
            "eat": xfood,
            "age": age,
            "old are you": age,
            "what is your name": f"My name is {xname}",
            "what's your name": f"My name is {xname}",
            "you called": f"My name is {xname}",
            "what country": xcountry,
            "what nation": xcountry,
            "you from": xcountry,
            }
    return burh[kword]


def sport():
    countries = requests.get("https://random-data-api.com/api/nation/random_nation")
    return f"I enjoy {countries.json()['national_sport']}."


def food():
    ffood = requests.get("https://random-data-api.com/api/food/random_food")
    foodWeight = random.randint(1, 3)
    foodResponse = {1: f"I like to eat {ffood.json()['dish'].lower()}.",
                    2: f"I don't have a favorite food, but if I had to choose, it would be {ffood.json()['dish'].lower()}.",
                    3: f"Anything with {ffood.json()['ingredient'].lower()}, and it's good."
                    }
    return foodResponse[foodWeight]


def age():
    ageWeight = random.randint(1, 100)
    ageDict = {range(1, 5): f"I am 6{random.randint(0, 9)} years old.",
               range(6, 10): f"I am 5{random.randint(0, 9)} years old.",
               range(11, 15): f"I am 4{random.randint(0, 9)} years old.",
               range(16, 90): f"I am {random.randint(2,3)}{random.randint(0,9)} years old.",
               range(91, 100): f"I am 1{random.randint(8,9)} years old."}
    for key, value in ageDict.items():
        if ageWeight in key:
            return value


xname = name()  # variables assigned to functions, as calling a function again
xcountry = country()  # will cause it to funny
xlanguage = language()
xsport = sport()
xfood = food()
age = age()
# introduction
print(f"Hi there, my name is {xname}, and I speak {xlanguage}. {xcountry}")
# runtime
while chatting:
    userInput = input('Say: ')
    print(f"{xname}: {keyword(userInput.lower())}")
