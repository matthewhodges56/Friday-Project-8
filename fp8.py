from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("500x350")
root.title("Customer Feedback")

titleLabel = StringVar()
titleLabel.set("Please provide feedback on your experience.")

label = ttk.Label(root, textvariable=titleLabel, font=("Arial", 14, "bold"),)
label.pack(pady=35)



root.mainloop()