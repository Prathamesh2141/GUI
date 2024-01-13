# from tkinter import *

# root = Tk()
# root.geometry("456x765")


# def hello():
#     print("hello Prathamesh")

# def cn():
#     cn=0
#     return cn   

# frame = Frame(root, borderwidth=6, bg="red", relief=SUNKEN)
# frame.pack(side=LEFT, pady=45)

# label = Label(frame, text="Print now", fg="green")
# label.pack()

# b1 = Button(frame, fg="yellow", text="Print ok",command=hello())
# b1.pack(side=RIGHT,padx=34,pady=34)

# b2 = Button(frame, fg="yellow", text="Print ok")
# b2.pack(side=LEFT, pady=24,padx=24)


# root.mainloop()
from tkinter import *

root = Tk()
root.geometry("456x765")

# Initialize a global variable
cn = 0

def hello():
    print("hello Prathamesh")

def increment_cn():
    global cn
    cn += 1
    print(f"cn value: {cn}")

frame = Frame(root, borderwidth=6, bg="red", relief=SUNKEN)
frame.pack(side=LEFT, pady=45)

label = Label(frame, text="Print now", fg="green")
label.pack()

b1 = Button(frame, fg="yellow", text="Print ok", command=hello)
b1.pack(side=RIGHT, padx=34, pady=34)

b2 = Button(frame, fg="yellow", text="Increment cn", command=increment_cn)
b2.pack(side=LEFT, pady=24, padx=24)

root.mainloop()
