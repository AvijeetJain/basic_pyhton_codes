import tkinter
def display():
    x=e1.get()
    #print(x)
    l1=tkinter.Label(text="Welcome to Graphics "+x,font=("Monotype corsiva",30,"bold"),bg="cyan")
    l1.place(x=50,y=150)
    
wind= tkinter.Tk()
wind.geometry("500x500")
wind.configure(bg="cyan")
l1=tkinter.Label(text="Python Graphics",font=("Calibri",20,"bold"),bg="cyan")
l1.place(x=180,y=0)

l2=tkinter.Label(text="Enter your Name",font=("Arial",10,"bold"),bg="Pink")
l2.place(x=5,y=50)

e1=tkinter.Entry(width=20,font=("Arial",10,"bold"))
e1.place(x=150,y=50)

b1=tkinter.Button(text="Submit",font=("Arial",10,"bold"),bg="Green",command=display)#why no bracekts when calling function display
b1.place(x=180,y=100)
