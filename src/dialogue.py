import time
import os

DELAY = 1.5
KEY_WORD = "any"

def display(lst,dia_bool = False):
    for txt in lst:
        print(txt)
        time.sleep(DELAY) if dia_bool else time.sleep(0)
        
def interact_handler(*args):
    if len(args)>3: return None
    if len(args) == 3:
        for i in range(len(args)-1): display(args[i],i%2==0)
        return check_valid(args[2])
    else:
        for i in range(len(args)): display(args[i],i%2==0)
    
def check_valid(lst_valid_ans):
    valid = False
    while not valid:
        response = input("What do you do?\n")
        if (KEY_WORD in lst_valid_ans): 
            os.system("clear")
            return response
        elif (response in lst_valid_ans): 
            os.system("clear")
            return response
        else:
            print("Invalid Response")
        
dialog = ["Hellow","VIncent", "123"]
options = ["Choose 1 ", "Choose 2"]
ans = ["1","2"]