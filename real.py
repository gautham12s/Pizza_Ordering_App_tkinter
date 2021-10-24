
from tkinter import *
def raise_frame(frame):
    frame.tkraise()


    
root=Tk()


cart=[]
p=PhotoImage(file='Corn.Gif')
p1=PhotoImage(file='Cheese.Gif')
p2=PhotoImage(file='Paneer.Gif')
p3=PhotoImage(file='Pork.Gif')
p4=PhotoImage(file='Chicken.Gif')
p5=PhotoImage(file='Fish.Gif')
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
def back():
    aftrsub()

for frame in (f1, f2,f3,f4):
    frame.grid(row=0, column=0, sticky='news')

def che():
    raise_frame(f4)
    bi=Button(f4,text='back',command=back)
    l23=Label(f4,text='you have selected cheese')
    e3=Entry(f4)
    l22=Label(f4,text="Address")
    butt=Button(f4,text='submit')
    l23.grid(row=0,column=1)
    l22.grid(row=1)
    e3.grid(row=1,column=2)
    butt.grid(row=2)
    bi.grid(row=3)
    
    
def aftrsub():
        raise_frame(f3)
        
        b1=Button(f3,text='Cheese',image=p1,bd=10,command=che)
        b1.grid(row=1)
        b2=Button(f3,text='Corn',image=p,bd=10)
        b2.grid(row=1,column=2)
        b3=Button(f3,text='Paneer',image=p2,bd=10)
        b3.grid(row=2)
        b4=Button(f3,text='Chicken',image=p4,bd=10)
        b4.grid(row=2,column=2)
        b5=Button(f3,text='Pork',image=p3,bd=10)
        b5.grid(row=3)
        b6=Button(f3,text='Fish',image=p5,bd=10)
        b6.grid(row=3,column=2)
        
        
        
        
def enry():
    raise_frame(f2)
    
    l1=Label(f2,text='Mobile No.')
    e1=Entry(f2)
    o=e1.get()
    l1.grid(row=0)
    e1.grid(row=0,column=1)
    b1=Button(f2,text="Submit",command=aftrsub)
    b1.grid(columnspan=2)
    
    
    
    
but1=Button(f1,text="Buy Pizza",activebackground='blue',height=10,width=20,command=enry)
but1.pack()
raise_frame(f1)

root.mainloop()

