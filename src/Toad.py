from Ratata import Rat
import random

def handle_item(rat: Rat, item, num):
    if not item in rat.belongings:
        rat.belongings.update({item : num})
    else:
        rat.belongings[item] = rat.belongings[item] + num
    return rat

class toad:
    def __init__ (self):
        self.encounter = False
    def shop(rat: Rat):
        dialog = ["What would you like to buy?", ]
        options = ["Health Pot : 15 Health : Priced at 3 Cheese",
                  "Rat Slave : +1 Gang Member : Priced at 2 Cheese", 
                  "Soap : -15 Filth : Priced at 4 Cheese", 
                  "Cheese Lottery : Get 2 to 4 Cheese : Priced at 4 Cheese"]
        options_functions = ["health_potion", "rat_slave", "soap", "cheese_lottery"]
    def health_potion(rat: Rat):
        rat = handle_item(rat, "cheese", -3)
        rat.health = rat.health + 15
    def rat_slave(rat: Rat):
        rat = handle_item(rat, "cheese", -2)
        rat.gang.append("rat slave")
    def soap(rat: Rat):
        rat = handle_item("cheese", -4)
        rat.filth = rat.filth - 15
    def cheese_lottery(rat: Rat):
        rat = handle_item("cheese", -2)
        rat = handle_item("cheese", random.randint(0, 4))
        
