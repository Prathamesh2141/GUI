from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")

can_widget = Canvas(root, width=canvas_width, height=canvas_height)

can_widget.pack()

can_widget.create_line(0,0,800,400,fill="red")
can_widget.create_line(0,400,800,0, fill="red")
# for creating rectangle
can_widget.create_rectangle(3,5,700,300, fill="blue")
# for creating text
can_widget.create_text(200,200,text="Jay shri Ram",fill="orange")
# for creating oval
can_widget.create_oval(344,233,433,533)






root.mainloop()