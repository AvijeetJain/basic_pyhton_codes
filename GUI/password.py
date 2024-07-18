import tkinter
def check():
    if e1.get()=="DPS" and e2.get()=="bopal":
        login1=tkinter.Tk()
        login1.geometry("300x300")
        login1.configure(bg="green")
        l3=tkinter.Label(login1,text="Welcome to our project",font=("Monotype Corsiva",30,"bold"),bg="red")
        l3.place(x=120,y=100)
        login.destroy()
    else:
        l1=tkinter.Label(login,text="Login unsccessful", font=("Arial",10,"bold"),bg="pink")
        l1.place(x=150,y=200)
                         
login= tkinter.Tk()
login.geometry("500x500")
login.configure(bg="cyan")
l1=tkinter.Label(text="User Id",font=("Calibri",20,"bold"),bg="yellow")
l1.place(x=0,y=10)

e1=tkinter.Entry(login,width=25,font=("Arial",10,"bold")) #WHY use login , working without writing login
e1.place(x=200,y=10)

l2=tkinter.Label(text="Enter Password",font=("Arial",10,"bold"),bg="Pink")
l2.place(x=0,y=50)

e2=tkinter.Entry(login,width=25,font=("Arial",10,"bold"),show="*")
e2.place(x=200,y=50)

b1=tkinter.Button(text="Submit",font=("Arial",10,"bold"),bg="Green",command=check)
b1.place(x=150,y=150)
