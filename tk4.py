from tkinter import *

root = Tk()

root.geometry("444x233")

root.title("Prathamesh")

# Important Label Options
# text= adds the text
# bd= background
# fg= foreground
# font= sets the font
# padx= x padding
# pady= y padding
# relief= border styling- SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(root, text='''Hello guys, I am Prathamesh.
From Prabhaini, Maharashtra.''', bg="green", fg="white", padx=12, pady=94, font=("Helvetica", 16), relief=SUNKEN)

title_label.pack()

root.mainloop()
