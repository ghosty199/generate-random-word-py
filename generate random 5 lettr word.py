from tkinter import*
import random
root=Tk()
root.geometry("400x400")
root.title("Generate random word")
label1=Label(root,text="")
label1.place(relx=0.5, rely=0.6, anchor=CENTER)
luckyfriendnames=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
randomnumber=random.randint(0,25)
print(luckyfriendnames[randomnumber])
def luckyfriend():
    items1=random.randint(0,25)
    items2=random.randint(0,25)
    items3=random.randint(0,25)
    items4=random.randint(0,25)
    items5=random.randint(0,25)

    label1["text"]=luckyfriendnames[items1]+luckyfriendnames[items2]+luckyfriendnames[items3]+luckyfriendnames[items4]+luckyfriendnames[items5]
button1=Button(root,text="generate random word",command=luckyfriend)
button1.place(relx=0.5, rely=0.8, anchor=CENTER)





root.mainloop()