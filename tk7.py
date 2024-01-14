# from tkinter import *

# def getVal():
#     print(uservalue.get())
#     print(passvalue.get())
    



# root = Tk()
# root.geometry("655x566")
# user = Label(root, text="Username")
# password = Label(root, text="Password")
# user.grid()
# password.grid(row=1)


# uservalue = StringVar()
# passvalue = StringVar()

# userentry = Entry(root, textvariable=uservalue)
# passentry = Entry(root, textvariable=passvalue)

# userentry.grid(row=0,column=1)
# passentry.grid(row=0,column=1)

# Button(text="Submit", command=getVal).grid()



# root.mainloop()

# from tkinter import *

# def getVal():
#     print(uservalue.get())
#     print(passvalue.get())

# root = Tk()
# root.geometry("655x566")

# user = Label(root, text="Username")
# password = Label(root, text="Password")
# user.grid()
# password.grid(row=1)

# uservalue = StringVar()
# passvalue = StringVar()

# userentry = Entry(root, textvariable=uservalue)
# passentry = Entry(root, textvariable=passvalue)

# userentry.grid(row=0, column=1)
# passentry.grid(row=1, column=1)  # Corrected grid placement for the password entry

# Button(text="Submit", command=getVal).grid(row=2, column=1)  # Adjusted the grid placement

# root.mainloop()


from tkinter import *

def submit_form():
    # This function could be extended to save data or perform other actions
    print("Form submitted!")

root = Tk()
root.title("Dance Class Registration Form")
root.geometry("400x300")

# Define colors
bg_color = "#FFD700"  # Light Goldenrod Yellow
label_color = "#333333"  # Dark Gray
button_color = "#4CAF50"  # Green

# Set background color
root.config(bg=bg_color)

# Header Label
header_label = Label(root, text="Dance Class Registration", font=("Helvetica", 16, "bold"), bg=bg_color, fg=label_color)
header_label.pack(pady=10)

# Name Entry
name_label = Label(root, text="Full Name:", font=("Helvetica", 12), bg=bg_color, fg=label_color)
name_label.pack(pady=5)
name_entry = Entry(root, font=("Helvetica", 12))
name_entry.pack(pady=5)

# Age Entry
age_label = Label(root, text="Age:", font=("Helvetica", 12), bg=bg_color, fg=label_color)
age_label.pack(pady=5)
age_entry = Entry(root, font=("Helvetica", 12))
age_entry.pack(pady=5)

# Dance Style Dropdown
style_label = Label(root, text="Select Dance Style:", font=("Helvetica", 12), bg=bg_color, fg=label_color)
style_label.pack(pady=5)
dance_styles = ["Ballet", "Hip Hop", "Contemporary", "Salsa", "Tap"]
style_var = StringVar(root)
style_var.set(dance_styles[0])
style_dropdown = OptionMenu(root, style_var, *dance_styles)
style_dropdown.config(font=("Helvetica", 12), bg=bg_color)
style_dropdown.pack(pady=5)

# Submit Button
submit_button = Button(root, text="Submit", command=submit_form, font=("Helvetica", 14, "bold"), bg=button_color, fg="white")
submit_button.pack(pady=15)

root.mainloop()
