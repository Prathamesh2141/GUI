from tkinter import *

def getval():
    print("Submitting Form!")
    print("Name:", nameval.get())
    print("Phone:", phoneval.get())
    print("Gender:", genderval.get())
    print("Emergency Contact:", contactval.get())
    print("Payment Mode:", paymentval.get())
    print("Food Service:", foodser.get())

    with open("record.txt", "a") as f:  # Use "a" for append mode
        f.write(f"\nName: {nameval.get()}\n")
        f.write(f"Phone: {phoneval.get()}\n")
        f.write(f"Gender: {genderval.get()}\n")
        f.write(f"Emergency Contact: {contactval.get()}\n")
        f.write(f"Payment Mode: {paymentval.get()}\n")
        f.write(f"Food Service: {foodser.get()}\n")
        f.write("-" * 20 + "\n")  # Separate entries with a line of dashes


        

root = Tk()

root.geometry("644x344")

Label(root,text="welcome to pratham Transport!" ,pady=15,font="comicsansms 13 bold").grid(row=0,column=3)

name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
contact=Label(root,text="Emegency Contact")
payment=Label(root,text="Payment Mode")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
contact.grid(row=4,column=2)
payment.grid(row=5,column=2)

nameval= StringVar()
phoneval= StringVar()
genderval= StringVar()
contactval= StringVar()
paymentval= StringVar()
foodser= IntVar()

nameentry =Entry(root, textvariable=nameval)
phoneentry =Entry(root, textvariable=phoneval)
genderentry =Entry(root, textvariable=genderval)
contactentry =Entry(root, textvariable=contactval)
paymententry =Entry(root, textvariable=paymentval)


nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
contactentry.grid(row=4,column=3)
paymententry.grid(row=5,column=3)

foodserr =Checkbutton(text="Ok food",variable=foodser)
foodserr.grid(row=6, column=3)

Button(text="Ok click for food", command=getval).grid(row=7, column=3)
root.mainloop()