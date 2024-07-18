import tkinter
win=tkinter.Tk()
win.geometry("1000x1000")

l1=tkinter.Label(win, text="Welcome to my World", font=("calibri",20))
l1.place(x=350,y=0)

photo=tkinter.PhotoImage(file=r"d:\Pyhton\GUI\download.jfif‪")

b1=tkinter.Button(win, text="click me", image = photo)
b1.place(x=350,y=100) 
