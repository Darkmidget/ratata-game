input_dialogues = ["You have encountered a hobo that finds you cute.",
                "He passed you a cheese and went on his way."]

# Options
input_options = ["1. Keep the cheese in your belonging",
            "2. Eat the cheese"]


import time
from Ratata import Rat
def visual(**kwargs):
    for key, value in kwargs.items():
        if key == "dialogues":
            # dialogues = [list of dialogue]
            for dialogue in value:
                print(dialogue)
                time.sleep(1)

        if key == "rat":
            for attribute, value1 in value.__dict__.items():
                print(attribute, value1)

        if key == "options":
            # option =[list of choosable option]
            for option in value:
                print(option)
                time.sleep(1)


## Testing Corner
input_rat = Rat()
visual(dialogues = input_dialogues,rat = input_rat, options = input_options)