from dialogue import interact_handler
from Ratata import Rat
from time import sleep

rat = Rat()

def meet_hobo(rat: Rat):
    # Dialogues
    dialogue = ["You have encountered a hobo that finds you cute.",
                "He passed you a cheese and went on his way."]

    # Options
    options = ["1. Keep the cheese in your belonging",
               "2. Eat the cheese"]

    answer = ["1", "2"]

    user_input = interact_handler(dialogue, options, answer)

    match user_input:
        case "1":
            rat.belongings["Cheese"] = rat.belongings.get("Cheese", 0) + 1

        case "2":
            rat.health += 10
            rat.hunger += 10


def cat_attack(rat: Rat):
    dialogue = ["Meowth has found you while taking its evening stroll"]
    # Small rat
    if rat.size < 5:
        dialogue.append(["Due to your small size, you took huge damage from Meowth just swiping lazily at you.",
                         "Luckily, you fell into a small hole and landed back in the sewers.",
                         "You took 20 damage from the encounter"])
        rat.health -= 20

    else:    
        # Big rat
        dialogue.append(["With your huge size, you are given the option to fight back."])
        options = ["1. Fight back and gain a chance at victory!",
                    "2. Run away like the lil rat you are."]
        answers = ["1", "2"]

        user_answer = interact_handler(dialogue, options, answers)

        # Based on the rat size and your gang members, determine if you win the cat or not
        attack_power = rat.size + len(rat.rat_gang)

        match user_answer:
            case "1":

                if attack_power > 20:
                    print("Meowth has been slain")
                else:
                    dialogue = ["You lost the battle, why would you ever think mere sewer rats can win in a battle against a cat?",
                                "You took 40 damage from the encounter"]
                    interact_handler(dialogue)


            case "2":
                if len(rat.rat_gang) > 0:
                    dead_rat = rat.rat_gang.pop()

                    dialogue = [f"While running away with your tail behind your back, {dead_rat} got caught by Meowth while trying to defend your back.",
                                "What kind of leader would leave their gang behind and run at the first sight of danger..."]
                    interact_handler(dialogue)
                    return

                dialogue = ["You took 15 ounce of damage while escaping"]
                interact_handler(dialogue)
                rat.health += -15

print(vars(rat))
sleep(5)
meet_hobo(rat)
print(vars(rat))