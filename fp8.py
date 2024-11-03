# Imports
from tkinter import *
from tkinter import ttk
import sqlite3

# Database Setup 
conn = sqlite3.connect("customer_feedback.db")
c = conn.cursor()

# Table operations (dont forget the primary key! im in 3860 as well...)
c.execute('''
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    feedback TEXT NOT NULL
)
''')
conn.commit()

# Setup tkinter and basic window elements
root = Tk()
root.geometry("500x350")
root.title("Customer Feedback")
root.resizable(False, False)

def submitData():
    # Get user input from each field, using strip to remove whitespace
    name = nameEntry.get().strip()
    email = emailEntry.get().strip()
    feedback = feedbackEntry.get("1.0", END).strip()  # Get multiline input from Text widget

    # Check if any field is empty
    if not name or not email or not feedback:
        # Create an error popup
        errorWindow = Toplevel(root)
        errorWindow.title("Error")
        errorWindow.geometry("250x100")
        errorWindow.resizable(False, False)
        
        # Error message 
        errorLabel = Label(errorWindow, text="All fields are required.", fg="red", font=("Arial", 10, "bold"))
        errorLabel.pack(pady=10)
        
        # Close button for error window
        closeButton = ttk.Button(errorWindow, text="OK", command=errorWindow.destroy)
        closeButton.pack(pady=5)
        return  
    
    # Insert the data into the feedback table if all fields are filled
    c.execute("INSERT INTO feedback (name, email, feedback) VALUES (?, ?, ?)", (name, email, feedback))
    conn.commit()
    
    # Clear the fields after submit
    nameEntry.delete(0, END)
    emailEntry.delete(0, END)
    feedbackEntry.delete("1.0", END)

    # Console msg
    print("Data submitted successfully!\n")

# Retrieve data button function
def retrieveData():
    # Nested function for password verification
    def checkPassword():
        enteredPassword = passwordEntry.get()
        # If password user entered is correct
        if enteredPassword == "skip": # what i do a lot...  
            # Close password window
            passwordWindow.destroy()

            # Get data from feedback table and print using loop
            c.execute("SELECT * FROM feedback")
            records = c.fetchall()
            for record in records:
                print(record)
        else: # If password user entered is incorrect
            errorLabel.config(text="Incorrect password. Try again.")

    # Popup window for password
    passwordWindow = Toplevel(root)
    passwordWindow.title("Password Required")
    passwordWindow.geometry("300x150")
    passwordWindow.grab_set() 
    passwordWindow.resizable(False, False)

    # Label/entry for password
    passwrodLabel = ttk.Label(passwordWindow, text="Enter Password:", font=("Arial", 10))
    passwrodLabel.pack(pady=10)
    
    passwordEntry = ttk.Entry(passwordWindow, show="*", width=25)
    passwordEntry.pack(pady=5)

    # Error message label
    errorLabel = Label(passwordWindow, text="", fg="red", font=("Arial", 8))
    errorLabel.pack()

    # Submit button for password
    passwordButton = ttk.Button(passwordWindow, text="Submit", command=checkPassword)
    passwordButton.pack(pady=10)

    # Prevents user from interacting with main window until popup is closed
    passwordWindow.wait_window() 

# Title 
titleLabel = ttk.Label(root, text='Please provide feedback on your experience.', font=("Arial", 14, "bold"))
titleLabel.place(relx=0.5, rely=0.15, anchor='center')

# Label/entry for name
nameLabel = ttk.Label(root, text="Name:", font=("Arial", 10, "normal"))
nameLabel.place(relx=0.37, rely=0.3, anchor='center')

nameEntry = ttk.Entry(root)
nameEntry.place(relx=0.55, rely=0.3, anchor='center')

# Label/entry for email
emailLabel = ttk.Label(root, text="Email:", font=("Arial", 10, "normal"))
emailLabel.place(relx=0.37, rely=0.4, anchor='center')

emailEntry = ttk.Entry(root)
emailEntry.place(relx=0.55, rely=0.4, anchor='center')

# Label for feedback
feedbackLabel = ttk.Label(root, text="Feedback:", font=("Arial", 10, "normal"))
feedbackLabel.place(relx=0.19, rely=0.6, anchor='center')

# Use text widget for feedback instead of entry since its multiline
feedbackEntry = Text(root, width=35, height=5, bd=0.5, relief="solid")
feedbackEntry.place(relx=0.55, rely=0.6, anchor='center')

# Submit button
submitButton = ttk.Button(root, text="Submit", takefocus=False, command=submitData)
submitButton.place(relx=0.47, rely=0.85, anchor='center')

# Retrieve data button
retrieveButton = ttk.Button(root, text="Retrieve Data", takefocus=False, command=retrieveData)
retrieveButton.place(relx=0.63, rely=0.85, anchor='center')

# Close the database connection when the window is closed
root.protocol("WM_DELETE_WINDOW", lambda: (conn.close(), root.destroy()))

root.mainloop()