from tkinter import *
root = Tk()
root.geometry("390x350")
root.title("Qr Code Generator")

data = StringVar()

def Click():
    print(data.get())
    
def Clear():
    data.set("")

Ph = PhotoImage(file="./ico.png")
root.iconphoto(False,Ph)

Label(root,text="QR Code Generator",font=("Calibri",25)).place(x=60,y=10)

Label(root,text="Enter Some Data",font=("Calibri",15)).place(x=120,y=80)
e1 = Entry(root,font=("Calibri",20),textvariable=data)
e1.focus()
e1.place(x=50,y=120)

Button(root,text="Click Here!",font=("Calibri",20),command=Click).place(x=120,y=190)

Button(root,text="Clear",font=("Calibri",15),command=Clear).place(x=160,y=280)

root.mainloop()