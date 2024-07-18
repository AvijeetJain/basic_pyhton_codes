import tkinter

def msg():
    print("Journal , assignment and sample paper uploaded")
    lab=lab=tkinter.Label(w,text="GUI Project",font=("showcard gothic",36),fg="white", bg="pink")
    lab.grid(row=7,column=20)

w=tkinter.Tk()
w.geometry("500x400")

w.title("MY first GUI Program")
lab=tkinter.Label(w,text="Hello All",font=("Monotype Corsiva",36),fg="pink")
lab.grid(row=1,column=1)

b=tkinter.Button(w,text="Click Here", command=msg, font=("chiller",17), fg="green", bg="black")
b.grid(row=6,column=20) 
