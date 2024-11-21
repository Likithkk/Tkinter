import tkinter as tk
calculation=""

def adding_to_caluculation(Symbol):
    global calculation
    calculation+=str(Symbol)
    result.delete(1.0,"end")
    result.insert(1.0,calculation)

def evaluation_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        result.delete(1.0,"end")
        result.insert(1.0,calculation)
    except:
        clear_field()
        result.insert(1.0,"ERROR")
        pass

def clear_field():
    global calculation
    calculation=""
    result.delete(1.0,"end")

root=tk.Tk()
root.geometry("300x265")

result=tk.Text(root,height=2,width=16,font=("Arial",24))
result.grid(columnspan=5)

btn1=tk.Button(root,text="1",command=lambda :adding_to_caluculation(1),width=5,font=("Arial",14))
btn1.grid(row=2,column=1)
btn2=tk.Button(root,text="2",command=lambda :adding_to_caluculation(2),width=5,font=("Arial",14))
btn2.grid(row=2,column=2)
btn3=tk.Button(root,text="3",command=lambda :adding_to_caluculation(3),width=5,font=("Arial",14))
btn3.grid(row=2,column=3)
btn4=tk.Button(root,text="4",command=lambda :adding_to_caluculation(4),width=5,font=("Arial",14))
btn4.grid(row=3,column=1)
btn5=tk.Button(root,text="5",command=lambda :adding_to_caluculation(5),width=5,font=("Arial",14))
btn5.grid(row=3,column=2)
btn6=tk.Button(root,text="6",command=lambda :adding_to_caluculation(6),width=5,font=("Arial",14))
btn6.grid(row=3,column=3)
btn7=tk.Button(root,text="7",command=lambda :adding_to_caluculation(7),width=5,font=("Arial",14))
btn7.grid(row=4,column=1)
btn8=tk.Button(root,text="8",command=lambda :adding_to_caluculation(8),width=5,font=("Arial",14))
btn8.grid(row=4,column=2)
btn9=tk.Button(root,text="9",command=lambda :adding_to_caluculation(9),width=5,font=("Arial",14))
btn9.grid(row=4,column=3)
btn0=tk.Button(root,text="0",command=lambda :adding_to_caluculation(0),width=5,font=("Arial",14))
btn0.grid(row=5,column=2)
btnadd=tk.Button(root,text="+",command=lambda :adding_to_caluculation("+"),width=5,font=("Arial",14))
btnadd.grid(row=2,column=4)
btnsub=tk.Button(root,text="-",command=lambda :adding_to_caluculation("-"),width=5,font=("Arial",14))
btnsub.grid(row=3,column=4)
btnmulti=tk.Button(root,text="*",command=lambda :adding_to_caluculation("*"),width=5,font=("Arial",14))
btnmulti.grid(row=4,column=4)
btndiv=tk.Button(root,text="/",command=lambda :adding_to_caluculation("/"),width=5,font=("Arial",14))
btndiv.grid(row=5,column=4)
btno=tk.Button(root,text="(",command=lambda :adding_to_caluculation("("),width=5,font=("Arial",14))
btno.grid(row=5,column=1)
btnc=tk.Button(root,text=")",command=lambda :adding_to_caluculation(")"),width=5,font=("Arial",14))
btnc.grid(row=5,column=3)
btnequal=tk.Button(root,text="=",command=evaluation_calculation,width=10,font=("Arial",14))
btnequal.grid(row=6,column=3,columnspan=2)
btnclear=tk.Button(root,text="AC",command=clear_field,width=10,font=("Arial",14))
btnclear.grid(row=6,column=1,columnspan=2)
root.mainloop()
