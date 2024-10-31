from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("500x350")
root.title("Customer Feedback")

titleLabel = ttk.Label(root, text='Please provide feedback on your experience.', font=("Arial", 14, "bold"))
titleLabel.pack(pady=30)

nameLabel = ttk.Label(root, text="Name:", font=("Arial", 10, "normal"))
nameLabel.place(relx=0.35, rely=0.3, anchor='center')

nameEntry = ttk.Entry(root)
nameEntry.place(relx=0.53, rely=0.3, anchor='center')

emailLabel = ttk.Label(root, text="Email:", font=("Arial", 10, "normal"))
emailLabel.place(relx=0.35, rely=0.4, anchor='center')

emailEntry = ttk.Entry(root)
emailEntry.place(relx=0.53, rely=0.4, anchor='center')

feedbackLabel = ttk.Label(root, text="Feedback:", font=("Arial", 10, "normal"))
feedbackLabel.place(relx=0.325, rely=0.5, anchor='center')

feedbackEntry = ttk.Entry(root, width=40)
feedbackEntry.place(relx=0.6, rely=0.5, anchor='center')

root.mainloop()