from tkinter import *
import tkinter.messagebox
import random

root = Tk()



lable = Label(root,text="Enter The Number")
lable.pack()
guess = 1
number = 100
def game(event):
    inp = answer.get()
    num = int(inp)
    if num == number:
        tkinter.messagebox.showinfo("Yipee!!","You guessed the correct number in "+ str(guess)+"Guesses")
    if num > number :
        hint.configure(text = "Hint : The number is smaller than this one")
    if num < number:
        hint.configure(text="Hint : The number is bigger than this one")
    hint.pack()



guess +=1
hint = Label(root)
answer = Entry(root)
answer.bind("<Return>",game)
answer.pack()
root.mainloop()

