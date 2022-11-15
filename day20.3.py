from tkinter import *
from time import sleep


def red():
    canvas1.create_oval(75, 75, 60, 60, fill='red', outline='white')
    canvas2.create_oval(75, 75, 60, 60, fill='white', outline='white')
    canvas3.create_oval(75, 75, 60, 60, fill='white', outline='white')
    canvas4.create_oval(75, 75, 60, 60, fill='white', outline='white')
    canvas5.create_oval(75, 75, 60, 60, fill='orange', outline='white')
    canvas6.create_oval(75, 75, 60, 60, fill='white', outline='white')
    canvas7.create_oval(75, 75, 60, 60,fill='white',outline='white')
    canvas8.create_oval(75, 75, 60, 60, fill='white', outline='white')
    canvas9.create_oval(75, 75, 60, 60, fill='green', outline='white')





def orange():
    canvas1.create_oval(75, 75, 60, 60, fill='white', outline='white')
    canvas2.create_oval(75, 75, 60, 60, fill='orange', outline='white')
    canvas3.create_oval(75, 75, 60, 60, fill='white', outline='white')
    canvas4.create_oval(75, 75, 60, 60, fill='white', outline='white')
    canvas5.create_oval(75, 75, 60, 60, fill='white', outline='white')
    canvas6.create_oval(75, 75, 60, 60, fill='Green', outline='white')
    canvas7.create_oval(75, 75, 60, 60, fill='red', outline='white')
    canvas8.create_oval(75, 75, 60, 60, fill='white', outline='white')
    canvas9.create_oval(75, 75, 60, 60, fill='white', outline='white')

def green():
    canvas1.create_oval(75, 75, 60, 60, fill='white', outline='white')
    canvas2.create_oval(75, 75, 60, 60, fill='white', outline='white')
    canvas3.create_oval(75, 75, 60, 60, fill='green', outline='white')
    canvas4.create_oval(75, 75, 60, 60, fill='red', outline='white')
    canvas5.create_oval(75, 75, 60, 60, fill='white', outline='white')
    canvas6.create_oval(75, 75, 60, 60, fill='white', outline='white')
    canvas7.create_oval(75, 75, 60, 60, fill='white', outline='white')
    canvas8.create_oval(75, 75, 60, 60, fill='orange', outline='white')
    canvas9.create_oval(75, 75, 60, 60, fill='white', outline='white')

count = 25
def start():
    counter(count)


def new(c):
    if c > 15:
        red()
        e.config(text=c)
        obj.update()
        sleep(1)
        counter(c)
    elif c > 10 and c <= 15:
        orange()
        e.config(text=c)
        obj.update()
        sleep(1)
        counter(c)
    elif c > 0 and c <= 10:
        green()
        e.config(text=c)
        obj.update()
        sleep(1)
        counter(c)
    elif c == 0:
        count = 25
        red()
        e.config(text=c)
        obj.update()
        sleep(1)
        counter(count)


def counter(cou):
    if cou > 0:
        cou -= 1
        new(cou)


obj = Tk()
obj.title('testing')
obj.geometry()
obj.configure(bg='yellow', borderwidth=2)
e = Label(obj, font=('Calibri', 13))

canvas1 = Canvas(obj, bg='gray', height=100, width=300)
canvas1.grid(row=1, column=1)
canvas2 = Canvas(obj, bg='gray', height=100, width=300)
canvas2.grid(row=2, column=1)
canvas3 = Canvas(obj, bg='gray', height=100, width=300)
canvas3.grid(row=3, column=1)

canvas4 = Canvas(obj, bg='blue', height=100, width=300)
canvas4.grid(row=1, column=2)
canvas5 = Canvas(obj, bg='blue', height=100, width=300)
canvas5.grid(row=2, column=2)
canvas6 = Canvas(obj, bg='blue', height=100, width=300)
canvas6.grid(row=3, column=2)


canvas7 =Canvas(obj,bg='green',height=100,width=300)
canvas7.grid(row=4,column=1)
canvas8 =Canvas(obj,bg='green',height=100,width=300)
canvas8.grid(row=5,column=1)
canvas9 =Canvas(obj,bg='green',height=100,width=300)
canvas9.grid(row=6,column=1)

Button(obj, text='Start', command=start, font=('Calibri', 15), bg='lightgray', fg='blue', width='10',height='1', ).grid(row=7,column=1)

obj.mainloop()
