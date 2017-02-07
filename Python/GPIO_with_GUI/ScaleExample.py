'''
Created on Jan 26, 2017

@author: Evgenii_Lartcev
'''
from Tkinter import *

def sel():
   selection = "Value = " + str(var.get())
   label.config(text = selection)

root = Tk()
var = DoubleVar()
scale = Scale( root, variable = var )
scale.pack(anchor=CENTER)

button = Button(root, text="Get Scale Value", command=sel, fg='green', bg='black')
button.pack(anchor=CENTER)

label = Label(root)
label.pack()

root.mainloop()