from Ratata import Rat
import random

def handle_item(rat: Rat, item, num):
    if not item in rat.belongings:
        rat.belongings.update({item : num})
    else:
        rat.belongings[item] = rat.belongings[item] + num
    return rat

def health_potion(rat: Rat):
    rat = handle_item(rat, "cheese", -3)
    rat.health = rat.health + 15
    return rat
    
def rat_slave(rat: Rat):
    rat = handle_item(rat, "cheese", -2)
    rat.rat_gang.append("rat slave")
    return rat
    
def soap(rat: Rat):
    rat = handle_item(rat, "cheese", -4)
    rat.filth = rat.filth - 15
    return rat
    
def cheese_lottery(rat: Rat):
    rat = handle_item(rat, "cheese", -2)
    rat = handle_item(rat, "cheese", random.randint(0, 4))
    return rat

class Toad:
    def shop(self, rat: Rat):
        dialog = ["What would you like to buy?", ]
        options = ["Health Pot : 15 Health : Priced at 3 Cheese",
                  "Rat Slave : +1 Gang Member : Priced at 2 Cheese", 
                  "Soap : -15 Filth : Priced at 4 Cheese", 
                  "Cheese Lottery : Get 2 to 4 Cheese : Priced at 4 Cheese"]
        options_functions = [health_potion, rat_slave, soap, cheese_lottery]
        return (dialog, options, options_functions)

