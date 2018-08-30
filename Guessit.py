from tkinter import *
import tkinter.messagebox
import random



root = Tk()
canvas = Canvas(root, width =500,height = 400 )
canvas.create_text(250,150,text="Welcome To The Game Of Numbers\n", font = ("Roman",20))
canvas.create_text(250,250,text="This program will randomly generate a number,\nuser needs to guess the number in minimum number of Guesses,\n program will show you if it is higher or lower")
canvas.pack()
lable = Label(root, text="Enter The Number")
lable.place(x=250,y=350)
lable.pack()

number = random.randrange(10000)
guess = 0

def resetthegame(event):
    number = random.randrange(10000)
    guess = 0

def game(event):
    inp = answer.get()
    num = int(inp)
    global guess
    global number
    
    guess+=1
    if num == number:
        tkinter.messagebox.showinfo("Yipee!!", "You guessed the correct number in " + str(guess) + "Guesses")
        guess = 0
        number = random.randrange(10000)
    if num > number:
        hint.configure(text="Hint : The number is smaller than this one")
    if num < number:
        hint.configure(text="Hint : The number is bigger than this one")
    hint.pack()

def exiting(event):
    root.destroy()

hint = Label(root)
answer = Entry(root)
answer.bind("<Return>", game)
answer.pack()
exit = Button(text="Exit Game")
exit.bind("<Button-1>",exiting)
exit.pack(side = BOTTOM)
reset = Button(text="Reset")
reset.bind("<Button-1>",resetthegame)
reset.pack(side = BOTTOM)


root.mainloop()