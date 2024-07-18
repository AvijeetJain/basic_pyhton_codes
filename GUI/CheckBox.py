import tkinter
def display():
    print("You have opted")
    if a.get()==1:
        print("Happy Potter")
    if b.get()==1:
        print("Game of Thrones")
    if c.get()==1:
        print("Throne of Glass")
    if d.get()==1:
        print("Divergent")
    if e.get()==1:
        print("Inheritence Cycle")
                             
win= tkinter.Tk()
win.geometry("900x1110")

l1=tkinter.Label(win,text="Select your Dream",font=("Calibri",20,"bold"),bg="green")
l1.place(x=0,y=10)

a=tkinter.IntVar()
b=tkinter.IntVar()
c=tkinter.IntVar()
d=tkinter.IntVar()
e=tkinter.IntVar()

c1=tkinter.Checkbutton(win, text="Happy Potter", font=(10),variable=a,onvalue=1)
c2=tkinter.Checkbutton(win, text="Game of Thrones", font=(10),variable=b,onvalue=1)
c3=tkinter.Checkbutton(win, text="Throne of Glass", font=(10),variable=c,onvalue=1)
c4=tkinter.Checkbutton(win, text="Divergent", font=(10),variable=d,onvalue=1)
c5=tkinter.Checkbutton(win, text="Inheritence Cycle", font=(10),variable=e,onvalue=1)

c1.place(x=150,y=50)
c2.place(x=350,y=50)
c3.place(x=550,y=50)
c4.place(x=750,y=50)
c5.place(x=950,y=50)

b1=tkinter.Button(win, text="Submit",font=(15),command=display)
b1.place(x=300,y=100)
