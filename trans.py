from tkinter import *
from tkinter import messagebox

def getval():
    print("Submitting Form!")
    print("Name:", nameval.get())
    print("Phone:", phoneval.get())
    print("Gender:", genderval.get())
    print("Emergency Contact:", contactval.get())
    print("Payment Mode:", paymentval.get())
    print("Food Service:", foodser.get())

    with open("record.txt", "a") as f:
        f.write(f"\nName: {nameval.get()}\n")
        f.write(f"Phone: {phoneval.get()}\n")
        f.write(f"Gender: {genderval.get()}\n")
        f.write(f"Emergency Contact: {contactval.get()}\n")
        f.write(f"Payment Mode: {paymentval.get()}\n")
        f.write(f"Food Service: {foodser.get()}\n")
        f.write("-" * 20 + "\n")

    messagebox.showinfo("Success", "Order submitted successfully!")

root = Tk()
root.geometry("500x400")
root.title("Transport Orders")

Label(root, text="Welcome to Pratham Transport!", pady=15, font="comicsansms 16 bold").grid(row=0, column=1)

label_frame = LabelFrame(root, text="Customer Information", font=("Helvetica", 12), padx=10, pady=10)
label_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

labels = ["Name", "Phone", "Gender", "Emergency Contact", "Payment Mode"]
entry_variables = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar()]

for i, label_text in enumerate(labels):
    Label(label_frame, text=label_text, font=("Helvetica", 12)).grid(row=i, column=0, padx=10, pady=10)
    Entry(label_frame, textvariable=entry_variables[i], font=("Helvetica", 12)).grid(row=i, column=1, padx=10, pady=10)

food_service_var = IntVar()
Checkbutton(root, text="Food Service", variable=food_service_var, font=("Helvetica", 12)).grid(row=2, column=1, pady=10)

Button(root, text="Submit", command=getval, font=("Helvetica", 14)).grid(row=3, column=1, pady=20)

root.mainloop()
