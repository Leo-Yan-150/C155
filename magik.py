from tkinter import *
import random

root=Tk()
root.title("Mutidimensional Arrays")
root.geometry("500x500")

LM = Label(root)
LI = Label(root)
LT = Label(root)

Dictionary = {'Mutable': "Values can be changed just like a list.","Immutable":"Value cannot be changed just like a tuple", "TKinter" : "This is the GUI library of python"}

def LMM():
    LM['text'] = Dictionary['Mutable']
def LIM():
    LI['text'] = Dictionary['Immutable']
def LTM():
    LT['text'] = Dictionary['TKinter']

b1 = Button(root, text="Hey Alexa define Mutable", command=LMM)
b1.place(relx=0.5,rely=0.2,anchor=CENTER)
LM.place(relx=0.5,rely=0.3,anchor=CENTER)
b2 = Button(root, text="Hey Siri define Immutable", command=LIM)
b2.place(relx=0.5,rely=0.4,anchor=CENTER)
LI.place(relx=0.5,rely=0.5,anchor=CENTER)
b3 = Button(root, text="Hey google define TKinter", command=LTM)
b3.place(relx=0.5,rely=0.6,anchor=CENTER)
LT.place(relx=0.5,rely=0.7,anchor=CENTER)



root.mainloop()

#this code is totoally not scuffed and totally not copied off of byju's future school