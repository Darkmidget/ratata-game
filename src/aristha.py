import tkinter as tk
import random

root = tk.Tk() #creates a window?

root.geometry("600x600") #dimensions of the window created
root.title("can you do the super bag?") #title of the window

#initial coordinates of basket
x_coord_of_basket = 6*50
    

basket = tk.Label(root, text="[___]", anchor = "center", font=('Arial', 18)) #parent object, what to put into, format 
basket.place(x = x_coord_of_basket - 15, y = 10*50)

#^the thing changing will be the rows, cause falling down, 0 is the top, then max 10 rows, so the 10th row is where the basket is

#x coord keeps going back to 3-1 or 3+1 hm
def go_left():
    global x_coord_of_basket
    if x_coord_of_basket > 3*50:
        x_coord_of_basket = x_coord_of_basket - 50
        basket.place(x = x_coord_of_basket - 15, y = 10*50)

def go_right():
    global x_coord_of_basket
    if x_coord_of_basket < 9*50:
        x_coord_of_basket = x_coord_of_basket + 50
        basket.place(x = x_coord_of_basket - 15, y = 10*50)
    
def move_basket(keyboardpress):
    #print(x_coord_of_basket)
    #print(keyboardpress) #can see each individual keypresses and the change in state, x y is the position of mouse when keypress happens?
    #print(event.keysym) #show the specific properties
    #print(event.state)
    if keyboardpress.keysym == "a" or keyboardpress.keysym == "Left": 
        go_left() #activating/calling go_left
    elif keyboardpress.keysym == "d" or keyboardpress.keysym == "Right":
        go_right() #activating/calling 
    elif keyboardpress.keysym == "Escape":
        running_switch_1()
        

def end_the_game():
    #seconds = 0
    global num_lives, running
    def restart_game():
        global y_object, x_object, object_value, answer, question, score
        endscreen.place_forget()
        restart.destroy()
        answer = 0
        answerbtn.configure(text = answer)
        question = random.randint(1, 50)
        questionbtn.configure(text = question)
        score = 0
        scorebtn.configure(text = "Score: "+str(score))
        x_object = random.randrange(150, 500, 50)
        y_object = 25
        object_value = random.randint(1, question)
        number.place_forget()
        lives.configure(text = "Lives left\n" + num_lives*"\U0001F49A")
        lives.place_forget()
        startingscreen.place(x = 20, y = 20)
    running = False
    num_lives = 3    
    endscreen.configure(text = "Game Over!\n\nYour Score:\n" + str(score) + "\n")    
    number.place_forget()
    questionbtn.place_forget()
    root.after(100, endscreen.place(x=10, y=10, height=600, width=600))
    restart = tk.Button(endscreen, text = "Restart", font = ('Courier, 20'), command = restart_game)
    root.after(150, restart.place(x=170, y=400, height=100, width=250))
    pass
    #end the game, reset all display the score in the middle of the screen? 


# initial_time = 300000 #ms
# minutes = 5
# seconds = 0
speed = 100
# ms = 0

# def timer():
#     global minutes, seconds, initial_time, ms 
#     timebtn = tk.Button(root, text = "Time Left = "+ str(int(minutes)) + ":" + str(int(seconds)), font=('Courier', 12))    
#     ms = initial_time
#     ms = ms - speed
#     minutes = (ms/1000)//60
#     seconds = (ms/1000)%60
#     timebtn.destroy()
#     timebtn = tk.Button(root, text = "Time Left = "+ str(int(minutes)) + ":" + str(int(seconds)), font=('Courier', 12))
#     timebtn.place(x=10, y=10, height=50, width=200)
    
#     #what keeps the game running? timer? not updating idk why
    
def minus_lives():
    global num_lives
    num_lives = num_lives - 1
    lives.configure(text = "Lives left\n" + num_lives*"\U0001F49A")
    #print("test-1")
    
                    
answer = 0
question = 10

score = 0
num_lives = 3
    
object_value = random.randint(1, 10)
x_object = 5*50
y_object = 25
number = tk.Label(root, text = object_value, font = ('Courier', 12))

   
def next_level():
    good_text = ["Your mother is proud of you!!", "Good Job!!!!!", "Kumon paid off!", "WOW!", "So smart", "slayyy", "+1 yay"]
    pick_good = random.randint(0, len(good_text)-1)
    message = tk.Label(root, text = good_text[pick_good], font = ('Comic Sans', 18), fg="#08E000")
    message.place(x = 130, y = 100)
    root.after(1000, message.place_forget) 
    update()
    root.after(speed, falling1)
    
def failed_level():
    global num_lives
    bad_text = ["Greedy >:(", "Do better!", "Try again. but still -1 tho", "again??", "Your mother is not proud", "Even my grandma can do better", "I think you need Kumon"]
    pick_bad = random.randint(0, len(bad_text)-1)
    message = tk.Label(root, text = bad_text[pick_bad], font = ('Comic Sans', 18), fg="#FF0000")
    if num_lives > 1:
        message.place(x = 300, y = 100)
    root.after(1000, message.place_forget)
    update()
    root.after(speed, falling1)
    
def update():
    def update_answer():
        #set answer back to 0
        global answer
        answer = 0
        answerbtn.configure(text = answer)
        
    def update_question():
        #creates a new question
        global question
        question = random.randint(0,50)
        questionbtn.configure(text = question)

    root.after(500, update_answer)
    root.after(500, update_question)
    
def falling1():
    global y_object, x_object, question, answer, number, object_value, score, lives
    #print(running)
    if running == True and num_lives != 0:
        y_object = y_object + 25
        number.place(x = x_object, y = y_object)
        questionbtn.place(x=200, y=10, height=30, width=200)
        lives.place(x = 10, y = 10)
        #timer()
        #print(y_object)

        def make_new_object():
            global y_object, x_object, question, answer, number, object_value, score, num_lives
            y_object = 25
            x_object = random.randrange(150, 500, 50)
            if question - answer > 10:
                object_value = random.randint(10, (question-answer))
            elif question - answer < 4:
                object_value = random.randint(1, 4)
            else:
                object_value = random.randint(1, 10)
            number = tk.Label(root, text = object_value, font = ('Courier', 12))
    #         print("aaa") #why is it looping at this point?
    #         print(object_value)
    #         print(question)
    #         print(y_object)

        if y_object == 10*50 and x_object == x_coord_of_basket:
            answer = answer + object_value
            #make the number green
            collected_number = number
            collected_number = tk.Label(root, text = object_value, font = ('Courier', 12), fg="#08E000")
            collected_number.place(x = x_object, y = y_object)
            #destroys the number after it's been caught
            root.after(150, collected_number.place_forget)
            root.after(150, number.place_forget)
            #updates the display of the answer:
            answerbtn.configure(text = answer)

            if question == answer:
                next_level()
                green_answerbtn = tk.Button(root, text = answer, font=('Courier', 18), bg="#05FF00")
                green_answerbtn.place(x=250, y=540, height=50, width=100)
                green_questionbtn = tk.Button(root, text = question, font=('Courier', 18), bg="#05FF00")
                green_questionbtn.place(x=200, y=10, height=30, width=200)
                score = score + 1
                scorebtn.configure(text = "Score: "+str(score))
                root.after(250, green_answerbtn.destroy)
                root.after(250, green_questionbtn.destroy)


            elif question < answer:
                minus_lives()
                failed_level()
                red_answerbtn = tk.Button(root, text = answer, font=('Courier', 18), bg="#FF0000")
                red_answerbtn.place(x=250, y=540, height=50, width=100)
                red_questionbtn = tk.Button(root, text = question, font=('Courier', 18), bg="#FF0000")
                red_questionbtn.place(x=200, y=10, height=30, width=200)      
#                 score = score - 1
#                 scorebtn.configure(text = "Score: "+str(score))
                root.after(250, red_answerbtn.destroy)
                root.after(250, red_questionbtn.destroy)

            else:
                make_new_object()
                root.after(speed, falling1)

        #looping falling function every 500 ms
        elif question != answer and y_object <= 10*50:
            root.after(speed, falling1)

        #destroys the number if it is not caught after it fully falls down
        else:
            fallennumber = number
            fallennumber.place_forget()
            make_new_object()
            root.after(speed, falling1)
    
    else:
        end_the_game()
        pass
            
            
running = False

def running_switch_1():
    global running
    startingscreen.place_forget()
    if running == True:
        running = False
    else:
        running = True
    root.after(250, falling1)
    
        
root.bind("<KeyPress>", move_basket) #binds a keypress to a shortcut//something happening inside the [root]


startingscreen = tk.Label(root, text="Hello! Press any of the Modes to start!\n Press Esc to end anytime!\n\nMode 1 = catch the numbers               \nMode 2 = catch both numbers and operators", font=('Courier', 16))
startingscreen.place(x = 20, y = 20)

start1btn = tk.Button(root, text = "Mode 1", font=('Courier', 18), command = running_switch_1)
start1btn.place(x=10, y=440, height=50, width=100)

questionbtn = tk.Button(root, text = question, font=('Courier', 18))

answerbtn = tk.Button(root, text = answer, font=('Courier', 18))
answerbtn.place(x=250, y=540, height=50, width=100)

scorebtn = tk.Button(root, text = "Score: "+str(score), font=('Courier', 12))
scorebtn.place(x=10, y=540, height=50, width=100)

lives = tk.Label(root, text = "Lives left\n" + num_lives*"\U0001F49A", font = ('Courier', 18))



#----------------------------------------------------------------------------------------------------------------------
start2btn = tk.Button(root, text = "Mode 2", font=('Courier', 18), command = falling1)
start2btn.place(x=10, y=340, height=50, width=100)

#----------------------------------------------------------------------------------------------------------------------

endscreen = tk.Label(root, text = "Game Over!\n\nYour Score:\n" + str(score) + "\n", font = ('Courier, 30'))

root.mainloop() #keeps the window open
