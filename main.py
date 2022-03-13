from tkinter import *
from tkinter import ttk
from tkinter import font
from webbrowser import BackgroundBrowser
import Scale_Chooser as scale

root = Tk()
root.title("Scales Randomizer")
root.state('zoomed')
root.configure(background="#0E2C67")

title = Label(root, text="Scales Chooser", font=('VERDANA', 60), bg="#0E2C67", fg="#B3DB46")
title.place(anchor=CENTER, relx=0.5, rely=0.1)

label_scale = Label(root, text="", bg="#0E2C67", fg="#c160a7", font=("VOLKORN", 20))
label_scale.place(anchor=CENTER, relx=0.5, rely=0.5)

label_randomized_scale = Label(root, text="", bg="#0E2C67", fg="#c160a7", font=("MOONGLADE", 20))
label_randomized_scale.place(anchor=CENTER, relx=0.5, rely=0.8)

button_chooser = Button(root, 
    text="Click me to choose a scale!", 
    font=('VERDANA', 20), 
    bg="#196581", 
    fg="#B3DB46", 
    bd="0",     	
    activebackground="#44DB58",
    activeforeground="#DB44C7",
    command=lambda: [scale.update_scale(label_randomized_scale), scale.show_scale(label_scale)])
button_chooser.place(anchor=CENTER, relx=0.5, rely=0.9)

root.mainloop()