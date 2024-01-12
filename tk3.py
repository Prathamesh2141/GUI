from tkinter import *

root = Tk()

root.geometry("400x400")

try:
    # Load the image
    photo = PhotoImage(file="ok.jpg")

    # Create a label with the image
    pm_label = Label(root, image=photo)

    # Pack the label to display the image
    pm_label.pack()

except Exception as e:
    print(f"Error: {e}")

root.mainloop()
