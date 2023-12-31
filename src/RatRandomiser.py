import random
from Hobo import Hobo
from Toad import Toad
from Ratata import Rat
from cat import Cat
import other_events
import rat as OthRat

hobo = Hobo()
toad = Toad()
rat = Rat()
cat = Cat()
other_rat = OthRat.OtherRat()



def event(rat):
    filth_chance = rat.filth/100
    n = random.random()
    dialog = []
    options = []
    option_func = []
    if n <= filth_chance:
        re_values = filth_event(rat)
    else:
        re_values = other_event(rat)
    if len(re_values) == 4:
        dialog,options,option_func,second_dialog = re_values
        dialog.append(filth_trigger(rat))
        return dialog, options, option_func,second_dialog
    elif len(re_values) == 3:
        dialog,options,option_func = re_values
        dialog.append(filth_trigger(rat))
        return dialog, options, option_func
    else:
        print("Critical Error in Return Value")

def other_event(rat):
    n = random.random()

    if not "cheese" in rat.belongings or rat.belongings["cheese"] < 2: shop_chance = 0.0
    else: shop_chance = 0.25    
    if shop_chance > 0 and len(rat.rat_gang) > 0: flood_chance = 0.1
    else: flood_chance = 0.0

    theft_chance = 0.1
    pond_chance = 0.2
    if n <= shop_chance:
        return toad.shop(rat)
    elif n <= shop_chance + theft_chance:
        return other_events.theft(rat)
    elif n <= shop_chance + theft_chance + flood_chance:
        return other_events.flood(rat)
    elif n <= shop_chance + theft_chance + flood_chance + pond_chance:
         return other_events.pond(rat)
    else:
        return other_rat.rat_encounter(rat)
    
def filth_event(rat):
    cat_chance = 0.5
    n = random.random()
    if n <= cat_chance:
        return cat.encounter(rat)
    else:
        return hobo.hobo_interact(rat)
    
def filth_trigger(rat):
    if rat.filth <= 25:
        return "\nYou are too clean for a rat, get filthy."
    elif rat.filth > 25:
        return "\nYou are moderately nasty."
    elif rat.filth > 50:
        return "\nYou are excessively foul smelling."
    elif rat.filth > 75:
        return "\nYou are the epitome of disgust, perfect."
    else:
        return "\n You are too clean for a rat. Go get filthy!"


#print(event(rat)[0])