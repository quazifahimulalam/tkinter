import tkinter as tk
from tkinter import messagebox

VALID_OPERATIONS = ["+", "-"]


def calculator():
    first = first.get()
    second = second.get()
    operation = operation.get()
    
    if operation not in VALID_OPERATIONS:
        messagebox.showinfo("enter a valid operation ie. + or -")
        return
    else:
        messagebox.showerror("operation seclected")
        answer = 10
        
        
        
root = tk.Tk()
root.title("calculator(+ or -)")
root.geometry("300x200")


tk.Label(root, text="first number:").grid(row=0, column=0, padx=10, pady=10 , sticky='w')  
first = tk.Entry(root , width = 25)
first.grid(row=0, column=1)

tk.Label(root, text="second number:").grid(row=1, column=0, padx=10, pady=10 , sticky='w')  
second = tk.Entry(root , width = 25)
second.grid(row=1, column=1)




login_button = tk.Button(root, text="calculate", width=15, command=calculator)
login_button.grid(row=3, column=2, pady=20)

root.mainloop()