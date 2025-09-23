import tkinter as tk
from tkinter import messagebox

VALID_OPERATIONS = ["+", "-"]

def calculator():
try:
num1 = float(first.get())
num2 = float(second.get())
op = operation.get()

    if op not in VALID_OPERATIONS:
        messagebox.showerror("Error", "Enter a valid operation: + or -")
        return

    if op == "+":
        answer = num1 + num2
    elif op == "-":
        answer = num1 - num2

    result_var.set(str(answer))

except ValueError:
    messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Calculator (+ or -)")
root.geometry("350x220")

tk.Label(root, text="First number:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
first = tk.Entry(root, width=25)
first.grid(row=0, column=1)

tk.Label(root, text="Second number:").grid(row=1, column=0, padx=10, pady=10, sticky='w')
second = tk.Entry(root, width=25)
second.grid(row=1, column=1)

tk.Label(root, text="Operation (+ or -):").grid(row=2, column=0, padx=10, pady=10, sticky='w')
operation = tk.Entry(root, width=25)
operation.grid(row=2, column=1)

tk.Label(root, text="Result:").grid(row=3, column=0, padx=10, pady=10, sticky='w')
result_var = tk.StringVar()
result = tk.Entry(root, width=25, textvariable=result_var, state="readonly")
result.grid(row=3, column=1)

calculate_button = tk.Button(root, text="Calculate", width=15, command=calculator)
calculate_button.grid(row=4, column=1, pady=20)

root.mainloop()