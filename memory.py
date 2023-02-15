from tkinter import *
from PIL import ImageTk, Image
import random, os, time

score_got = 0
first_guess = False
second_guess = False
first_corr = ()
second_corr = ()

def click(x,y):
    
    global first_guess_value, second_guess_value, score_got, first_guess, second_guess, first_corr, second_corr

    
    if not first_guess:
        first_guess = True
        buttons[x][y]["image"] = buttons_img_text[x][y].get()
        first_guess_value = buttons_img_text[x][y].get()
        first_corr = (x,y)
        
    elif not second_guess:
        second_guess = True
        buttons[x][y]["image"] = buttons_img_text[x][y].get()
        second_guess_value = buttons_img_text[x][y].get()
        second_corr = (x,y)
        
        if first_guess_value == second_guess_value:
            score.config(text=str(score_got+10))
            score_got = int(score.cget("text"))
            first_guess, second_guess = False, False
            buttons[first_corr[0]][first_corr[1]].config(state="disabled")
            buttons[second_corr[0]][second_corr[1]].config(state="disabled")
        else:
            window.update()
            window.after(1000, flip_over(first_corr, second_corr))
            first_guess, second_guess = False, False
        

def flip_over(corr1, corr2):
    buttons[corr1[0]][corr1[1]]["image"] = back
    buttons[corr2[0]][corr2[1]]["image"] = back
    
    
def init_board():
    

    random.shuffle(images)
    item = 0
    for i in range(3):
        for j in range(4):
            buttons[i][j] = Button(
                play_frame,
                image=back,
                command=lambda x=i, y=j:click(x,y)
            )
            buttons_img_text[i][j].set(images[item%6])
            buttons[i][j].grid(row=i,column=j, sticky="NSEW")
            item +=1
            
    for i in range(3):
        play_frame.rowconfigure(i, weight=1)
        play_frame.columnconfigure(i, weight=1)
    
    for i in range(len(buttons_img_text)):
        random.shuffle(buttons_img_text[i])

def reset():
    global first_guess, second_guess, score_got
    init_board()
    score.config(text="0")
    score_got = 0
    first_guess, second_guess = False, False
    


window = Tk()
window.resizable(False, False)
window.title("Memory game")


play_frame = Frame(
    window,
    width=384,
    height=384
    
)
play_frame.grid(row=0, column=0, rowspan=3, padx=10, pady=10)

score_frame = Frame(
    window,
    width=100,
    height=100
    
)
score_frame.grid(row=0, column=1, padx=10)
Label(
    score_frame,
    text="SCORE",
    font=14
).grid(row=0, column=1)

score = Label(
    score_frame,
    text="0",
    font=14
)
score.grid(row=2, column=1)

reset_btn = Button(
    play_frame,
    font=14,
    text="Restart",
    command=reset
)
reset_btn.grid(row=4, column=0, columnspan=4)


buttons = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

buttons_click_status = [
    [False for j in range(len(buttons[0]))]
    for i in range(len(buttons))
]


apple = ImageTk.PhotoImage(Image.open("apple.png"), name="apple")
banana = ImageTk.PhotoImage(Image.open("banana.png"), name="banana")
orange = ImageTk.PhotoImage(Image.open("orange.png"), name="orange")
strawberry = ImageTk.PhotoImage(Image.open("strawberry.png"), name="strawberry")
pineapple = ImageTk.PhotoImage(Image.open("pineapple.png"), name="pineapple")
pizza = ImageTk.PhotoImage(Image.open("pizza.png"), name="pizza")
house = ImageTk.PhotoImage(Image.open("house.png"), name="house")
plane = ImageTk.PhotoImage(Image.open("plane.png"), name="plane")
car = ImageTk.PhotoImage(Image.open("car.png"), name="car")
hamburger = ImageTk.PhotoImage(Image.open("hamburger.png"), name="hamburger")
back = ImageTk.PhotoImage(Image.open("back.png"), name="back")

images = [
    apple,
    banana,
    orange,
    strawberry,
    pineapple,
    pizza,
    house,
    plane,
    hamburger,
    car
]

buttons_img_text = [
    [StringVar() for j in range(4)]
    for i in range(3)]

init_board()


first_guess_value = None
second_guess_value = None
    

window.mainloop()