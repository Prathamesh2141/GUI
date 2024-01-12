from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("4000x400")

try:
    # Load the image
    img = Image.open("vijay.jpg")
    photo = ImageTk.PhotoImage(img)

    # Create a label with the image
    pm_label = Label(root, image=photo)

    # Pack the label to display the image
    pm_label.pack()

except Exception as e:
    print(f"Error: {e}")

root.mainloop()

