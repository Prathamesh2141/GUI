from tkinter import *

def pram(event):
    print(f"You clicked on button {event.x}, {event.y}")

root = Tk()

root.title("Prathamesh Magar")

root.geometry("655x455")

widget = Button(root, text="Click me please")
widget.pack()
widget.bind('<Button-1>', pram)  # Corrected event sequence
widget.bind('<Double-1>', quit)
root.mainloop()
