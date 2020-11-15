from tkinter import *
import json
from difflib import get_close_matches
from time import sleep

root = Tk()
root.title("Dictionary")
root2 = Tk()
root2.title("")

def sarcasm():
    labele = Label(root2, text = "What? Can't you read?\nEnter Y if yes, N if no.\nDumbass").pack()


def clicketyNo():
    labele = Label(root2, text = "The word does not exist").pack()

def clicketyYes():
    lab = Label(root2, text = words[get_close_matches(search, words.keys())[0]]).pack()


def onClick():
    search = ent.get().lower()

    words = json.load(open("/home/tango/Documents/Python/DictionaryApp/data.json"))

    if ent.get() in words:
        for i in words[search]:
            labele = Label(root2, text = i).pack()

    elif len(get_close_matches(search, words.keys())) > 0:
        labell = Label(root2, text = "Did you mean %s instead?(Y/N): " % get_close_matches(search, words.keys())[0]).pack()
        choices = Entry(root2, width = 25, bg = "grey", fg = "white", borderwidth = 5)
        choices.pack()
        c = choices.get()

        #sleep(3)

        if c == "Y":
            button = Button(root2, text="Search", padx = 5, pady = 5, fg = "white", bg = "grey", command = clicketyYes).pack()

        elif c == "N":
            button = Button(root2, text="Search", padx = 5, pady = 5, fg = "white", bg = "grey", command = clicketyNo).pack()
        
        else:
            button = Button(root2, text="Search", padx = 5, pady = 5, fg = "white", bg = "grey", command = sarcasm).pack()
    
    else:
        labele = Label(root2, text = "The word does not exist").pack()
    
    


label = Label(root, text="Enter word:  ").grid(row = 0, column = 0)
ent = Entry(root, width = 25, bg = "grey", fg = "white", borderwidth = 5)
ent.grid(row = 0, column = 1)

button = Button(root, text="Search", padx = 5, pady = 5, fg = "white", bg = "grey", command = onClick).grid(row = 1, column = 1)



root2.mainloop()

root.mainloop()



