from tkinter import *
root=Tk()
root.geometry('500x500')
root.maxsize(600,600)
def f1():
    a=txt.get()
    s.config(text=a.upper())

def f2():
    b=txt.get()
    s.config(text=b.lower())
    
def f3():
    c=txt.get()
    s.config(text=c.capitalize())
def f4():
    d=txt.get()
    s.config(text=d.title())
def f5():
    e=txt.get()
    s.config(text=e.swapcase())
    
txt=StringVar()

Label(root,text='text transform',font='algerian 12').place(x=200, y=0)
Label(root,text='enter your text',font='aerial 12').place(x=2, y=20)
Entry(root,textvariable=txt,font='arial 11').place(x=2, y=40)
Button(root,text='upper',command=f1).place(x=20, y=60)
Button(root,text='lower',command=f2).place(x=100, y=60)
Button(root,text='capital',command=f3).place(x=180,y=60)
Button(root,text='title',command=f4).place(x=20,y=100)
Button(root,text='swap',command=f5).place(x=100,y=100)
Label(root,text=' your text',font='aerial 12').place(x=2, y=200)
s=Label()
s.place(x=2,y=220)
root.mainloop()
