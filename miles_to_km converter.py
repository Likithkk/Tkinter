import tkinter as tk
#from tkinter import ttk
#ttk has all required widgets
import ttkbootstrap as ttk

#functions
def convert():
    mile_input=entry_Int.get()
    #get the data
    km_out=mile_input*1.61
    output_str.set(km_out)
    #update the output

#window features
#window=tk.Tk() instead for better use
window = ttk.Window(themename='journal')
#other themes are darkly 
window.title("DEMO")
window.geometry("500x300")

#title
title_label=ttk.Label(master=window,text="MILES TO KILOMETERS",font="Calibri 30 bold")
#ttk.Label(master= (to which window),text="Text to be printed ",font="font_style size")

title_label.pack()
#pack() is to add Label to window

#input field
input_frame=ttk.Frame(master = window)
entry_Int=tk.IntVar()
#entryInt stores the int value entered
entry=ttk.Entry(master = input_frame,textvariable=entry_Int)
button=ttk.Button(master = input_frame,text="Convert" ,command=convert)
entry.pack(side="left" , padx= 8)
button.pack(side="left")
input_frame.pack(pady=10)

#output
output_str=tk.StringVar()
#variable for string variable 
output_label=ttk.Label(master=window , text="Output",font="Calibri 30 bold" , textvariable=output_str)
output_label.pack()


#run the window we use mainloop()
window.mainloop()
