from tkinter import *
import math

window = Tk()
window.title("GUI Mathematical Calculator")
window.geometry("400x550")
window.resizable(False, False)

expression = ""

entry = Entry(window, font=("Arial", 22), bd=8, relief=RIDGE, justify="right")
entry.pack(fill=BOTH, ipadx=8, ipady=15, padx=10, pady=10)


def press(value):
    global expression
    expression += str(value)
    entry.delete(0, END)
    entry.insert(END, expression)


def clear():
    global expression
    expression = ""
    entry.delete(0, END)


def equal():
    global expression
    try:
        result = str(eval(expression))
        entry.delete(0, END)
        entry.insert(END, result)
        expression = result
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")
        expression = ""


def square_root():
    global expression
    try:
        result = math.sqrt(float(expression))
        entry.delete(0, END)
        entry.insert(END, result)
        expression = str(result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")
        expression = ""


def power():
    press("**")


def modulus():
    press("%")


def off():
    window.destroy()


frame = Frame(window)
frame.pack()

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

for (text,row,col) in buttons:
    if text == "=":
        Button(frame,text=text,width=8,height=3,font=("Arial",14),
               command=equal).grid(row=row,column=col,padx=2,pady=2)
    else:
        Button(frame,text=text,width=8,height=3,font=("Arial",14),
               command=lambda t=text: press(t)).grid(row=row,column=col,padx=2,pady=2)

Button(frame,text="C",width=8,height=3,font=("Arial",14),
       command=clear).grid(row=5,column=0,padx=2,pady=2)

Button(frame,text="√",width=8,height=3,font=("Arial",14),
       command=square_root).grid(row=5,column=1,padx=2,pady=2)

Button(frame,text="^",width=8,height=3,font=("Arial",14),
       command=power).grid(row=5,column=2,padx=2,pady=2)

Button(frame,text="%",width=8,height=3,font=("Arial",14),
       command=modulus).grid(row=5,column=3,padx=2,pady=2)

Button(frame,text="OFF",width=36,height=2,bg="red",fg="white",
       font=("Arial",14),command=off).grid(row=6,column=0,columnspan=4,pady=10)

window.mainloop()