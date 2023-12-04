from Toad import handle_item
import random

def theft(rat):
    dialog = ["You are on the hunt for Cheese!", "\nBut who will you steal it from?"]
    options = ["Trash : 1 Cheese : 100% Success Rate", "Other Rats : 2 Cheese : 40% Success Rate", "A House : 4 Cheese : 25% Success Rate"]
    option_functions = [trash, steal_from_rats, steal_house]
    return dialog, options, option_functions

def trash(rat):
    handle_item(rat, "cheese", 1)
    return rat

def steal_from_rats(rat):
    if random.random() >= 0.5:
        handle_item(rat, "cheese", 2)
        return rat
    else:
        return rat

def steal_house(rat):
    if random.random() >= 0.25:
        handle_item(rat, "cheese", 4)
        return rat
    else:
        return rat

def flood(rat):
    dialog = ["It is rainning and the sewers are flooded!", "\n What will you save?"]
    options = ["My Rats! : -2 Cheese", "My Cheese! : -1 Gang Member", "Stay and Help!: - 5 HP"]
    option_functions = [save_rats, save_cheese, stay]
    return dialog, options, option_functions

def save_rats(rat):
    handle_item(rat, "cheese", -2)
    return rat

def save_cheese(rat):
    rat.rat_gang.pop()
    return rat

def stay(rat):
    rat.health = rat.health - 5
    return rat

def pond(rat):
    dialog = ["You feel like going for a bath, but which pond will you choose?"]
    options = ["Dirty pond : +10 Filth", "Clean Pond : -10 Filth", "On Second Thought. No Bath"]
    option_functions = [dirty, clean, no]
    return dialog, options, option_functions

def dirty(rat):
    rat.filth = rat.filth + 10
    return rat

def clean(rat):
    rat.filth = rat.filth - 10
    return rat

def no(rat):
    return rat