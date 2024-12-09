import tkinter as tk
from tkinter import messagebox

def show_notification():
    result = messagebox.showinfo("Honkai Star Rail", "dude, really it's 7 on the morning! go touch grass")
    if result == "ok":
        print("You pressed the OK button")
    else:
        print("You closed the notification.")

root = tk.Tk()
root.withdraw()  

root.after(100000, show_notification)

root.mainloop() 