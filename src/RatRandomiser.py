import random

def event():
    filth_chance = 0.05
    n = random.random()
    if n <= filth_chance:
        filth_event()
        print("filth")
    else:
        other_event()
        print("other")
        
def action():
    response = input("Select an Action : (1)Wash (2)Eat (3)Find Food (4)Skip")
    if response == '1':
        pass # reduce filth
    elif response == '2':
        pass # eat function
    elif response == '3':
        food_event()
    elif response == '4':
        event()
    else:
        print("Invalid Input. Please try again")
        action()

def filth_event():
    cat_chance = 0.1
    hobo_chance = 0.15
    n = random.random()
    if n <= cat_chance:
        pass #cat event
    elif n <= cat_chance + hobo_chance:
        pass #hobo event
    else:
        pass #rat event
    
def food_event():
    free_food_chance = 0.45
    steal_food_chance = 0.3
    n = random.random()
    if n <= free_food_chance:
        pass #food event
    elif n <= free_food_chance + steal_food_chance:
        pass #steal food
    else:
        pass #no food

def other_event():
    
    n = random.random()
        