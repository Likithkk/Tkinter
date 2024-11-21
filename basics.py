#basics
import tkinter as tk
from tkinter import ttk

def button_fun:
    print("button is pressed")

#create a window
window=tk.Tk()
window.title("window and widgets")
window.geometry("800x500")
#geometry=widthxheight

#create widgets
#master is the area where we need to place the widgets
#tk.Text(master=window).pack()
#pack()is used to add the widgets to the master

#ttk widgets
#ttk label
label=ttk.Label(master=window,text="Label")
label.pack()

#ttk entry
entry=ttk.Entry(master=window,textvariable=string_var)
#textvariable assign the entry value into the given var
entry.pack()

#tkinter variables
string_var=StringVar(value="start value")
string_var.set("the value to be set")

#ttk button
button=ttk.button(master=window,text="but_name",command=button_func)
#command=func_name or lambda:print(" ")
button.pack()

#run the window
window.mainloop()

