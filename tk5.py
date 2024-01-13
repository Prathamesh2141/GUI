from tkinter import *

root = Tk()
root.title("🌺 Jay Shri Ram 🌺")
root.geometry("655x333")

f1 = Frame(root, bg="skyblue", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2 = Frame(root, bg="dark orange", borderwidth=6, relief=SUNKEN)
f2.pack(side=RIGHT, fill="x")

l = Label(f1, text="🏹🕉️🚩🙏🏽🕉️🌺 Jay Shri Ram 🌺🙏🏽🕉️🏹🕉️🚩")
l.pack(pady=142)

l1 = Label(f2, text="🏹🕉️🚩🙏🏽🕉️🌺 Jay Shri Ram 🌺🙏🏽🕉️🏹🕉️🚩", fg="red")
l1.pack(padx=142)

root.mainloop()




