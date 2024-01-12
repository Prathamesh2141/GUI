# python tkinter geometry?


from tkinter import *

p_root = Tk()  # Correcting the case of 'Tk'

p_root.geometry("68x88")  # Correcting the '*' to 'x'
p_root.minsize(200,100)
p_root.maxsize(300,300)
p_root.mainloop()


# python tkinter lable??

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tkinter Label Example")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")

# Pack the label widget to display it in the window
label.pack()

# Start the Tkinter event loop
root.mainloop()
