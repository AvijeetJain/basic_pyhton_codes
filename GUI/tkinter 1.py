import tkinter
def display():
    print("hi! how are you")
window= tkinter.Tk()
window.geometry("500x700")
window.title("My first GUI")
l=tkinter.Label(window,text="welcome",font=("Monotype corsiva",30),fg="blue",bg="pink")
l.grid(row=1,column=1)
b=tkinter.Button(window,text="click here",command=window.destroy,font=("Monotype Corsiva",20),fg="Red",bg="Green")
b.grid(row=3,column=15)
