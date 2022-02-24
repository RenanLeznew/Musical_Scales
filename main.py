from tkinter import *

from sympy import re, riemann_xi
import Scale_Chooser as scale

root = Tk()
root.title("Scales Randomizer")
root.geometry("1600x900")

title = Label(root, text="Scales Chooser", font=('VERDANA', 20), fg="cyan")
title.place(anchor=CENTER, relx=0.5, rely=0.1)

label_scale = Label(root, text="", font=40)
label_scale.place(anchor=CENTER, relx=0.5, rely=0.8)

button_chooser = Button(root, text="Click me to choose a scale!", font=30, command=lambda: scale.update_scale(label_scale))
button_chooser.place(anchor=CENTER, relx=0.5, rely=0.9)

root.mainloop()