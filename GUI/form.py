import tkinter
def display():
    print("Hello "+e1.get())
    if i.get()==1:
        print("You are a Male")
    elif i.get==2:
        print("You area Female")
    elif i.get()==3:
        print("You are others")
    if j.get()==2:
        print("You have selected Science Stream")
    elif j.get()==1:
        print("You have selected Commerce Stream")
                             
win= tkinter.Tk()
win.geometry("900x900")
frame1=tkinter.Frame(win,width=600, height=200, bg="pink")
frame1.place(x=0,y=0)

l1=tkinter.Label(frame1,text="Enter name",font=("Calibri",20,"bold"),bg="yellow")
l1.place(x=0,y=20)

e1=tkinter.Entry(frame1,width=30,font=("Arial",10,"bold"))
e1.place(x=150,y=20)

l2=tkinter.Label(text="Select Gender",font=("Arial",10,"bold"),bg="Pink")
l2.place(x=0,y=100)

i=tkinter.IntVar()

rad1=tkinter.Radiobutton(frame1, text="Male", font=(10),value=1,variable=i)
rad2=tkinter.Radiobutton(frame1, text="Female", font=(10),value=2,variable=i)
rad3=tkinter.Radiobutton(frame1, text="Others", font=(10),value=3,variable=i)
rad1.place(x=150,y=100)
rad2.place(x=300,y=100)
rad3.place(x=450,y=100)

frame2=tkinter.Frame(win,width=500, height=300, bg="cyan")
frame2.place(x=0,y=200)

j=tkinter.IntVar()
l2=tkinter.Label(frame2, text="Select Stream",font=(10),bg="cyan")
l2.place(x=0,y=50)

rad3=tkinter.Radiobutton(frame2,text="Commerce", font=(10), value=1, variable=j)
rad4=tkinter.Radiobutton(frame2,text="Science", font=(10), value=2, variable=j)

rad3.place(x=150,y=50)
rad4.place(x=300,y=50)

b1=tkinter.Button(frame2, text="Submit",font=(15),command=display)
b1.place(x=180,y=150)
