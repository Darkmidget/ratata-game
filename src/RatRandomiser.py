import random
from Hobo import Hobo
from Toad import Toad
from Ratata import Rat

hobo = Hobo()

rat = Rat()


def event(rat):
    filth_chance = 0 
    n = random.random()
    dialog = []
    options = []
    option_func = []
    if n <= filth_chance:
        dialog,options,option_func = filth_event(rat)
    else:
        dialog,options,option_func = other_event(rat)
    dialog.append(hunger_trigger(rat))
    dialog.append(filth_trigger(rat))
    return dialog, options, option_func

def other_event(rat):
    n = random.random()
    toad = Toad
    # if not "cheese" in rat.belongings or rat.belongings["cheese"] < 2:
    #     shop_chance = 0
    # else:
    #     shop_chance = 0.2
    if n <= 0:
        return toad.shop(toad, rat)
    else:
        return hobo.hobo_interact(rat)
    
def filth_event(rat):
    cat_chance = 0.1
    hobo_chance = 0.15
    n = random.random()
    if n <= cat_chance:
        pass #cat event
    elif n <= cat_chance + hobo_chance:
        pass #hobo event
    else:
        pass #rat event

def hunger_trigger(rat):
    if rat.hunger <= 0:
        rat.health  = rat.health - 15
        return "\nYou are malnourished, your consciousness is slowly fading. Life will drop by 1 every 10 seconds."
    elif rat.hunger < 25:
        rat.health  = rat.health - 1
        return "\nYou are desperate for food, you feel weak. Life will drop by 1 every minute."
    elif rat.hunger < 50:
        return "\nYour stomach is grumbling, you need to find food."
    elif rat.hunger < 75:
        return "\nYou are feeling peckish."
    else:
        return "\nYou don’t feel hungry."
    
def filth_trigger(rat):
    if rat.filth > 25:
        rat.health  = rat.health - 1
        return "\nYou are moderately nasty."
    elif rat.filth > 50:
        return "\nYou are excessively foul smelling.”"
    elif rat.filth > 75:
        return "\nYou are the epitome of disgust, perfect."


print(event(rat)[0])
    
# def action():
#     response = input("Select an Action : (1)Wash (2)Eat (3)Find Food (4)Skip")
#     if response == '1':
#         pass # reduce filth
#     elif response == '2':
#         pass # eat function
#     elif response == '3':
#         food_event()
#     elif response == '4':g
#         event()
#     else:
#         print("Invalid Input. Please try again")
#         action()
 
# def food_event(rat):
#     free_food_chance = 0.45
#     steal_food_chance = 0.3
#     n = random.random()
#     if n <= free_food_chance:
#         pass #food event
#     elif n <= free_food_chance + steal_food_chance:
#         pass #steal food
#     else:
#         pass #no food
