import tkinter as tk
from tkinter import messagebox

DENOMINATIONS = [1000,500,100,50,20,10]

COLLOR_MAP = {
    1000: "#FFD700",
    500 : "#ff8c00",
    100 : "#adff2f",
    50 : "#FF6984",
    20 : "#ba55d3",
    10 : "#87cefa"}

def calculate_denominations():
    try:
        amount = int(entry_amount.get())
        if amount < 10:
            raise ValueError("Amount must be at least 10")
        remaining = amount
        for widget in frame_result.winfo_children():
            widget.destroy()
        for note in DENOMINATIONS:
            count = remaining//note
            remaining %= note  
            if count > 0 :
                label = tk.Label(frame_result, text=f"{note} taka x {count} = {note * count} taka" , bg = COLLOR_MAP[note] , fg="black", font=("Arial", 12 , "bold"), width=30)
                label.pack(pady=2)
        if remaining > 0:
            tk.Label(frame_result, text=f"Remaining amount: {remaining} taka", fg="red", font=("Arial", 11, "italic")).pack(pady=5)  
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer amount of at least 10.")
        
        
root = tk.Tk()
root.title("Denomination Calculator")
root.geometry("400x500")
root.config(bg="#f0f8ff")

tk.Label(root, text="taka denominator calculator",
         fg="#2f4f4f" , bg="#f0f8ff", font=("Arial", 16 , "bold")).pack(pady=15)

tk.Label(root , text="enter amount in taka:", font=("Arial", 12), bg="#f0f8ff").pack()
entry_amount = tk.Entry(root, font=("Arial", 12), justify="center")
entry_amount.pack(pady=10)

btn_calculate = tk.Button(root , text="calculate" , font=("arial" , 12 , "bold") , bg="#4682b4" , fg="white" , command=calculate_denominations)

btn_calculate.pack(pady=10)
frame_result = tk.Frame(root, bg="#e6f2ff" , bd=2, relief="ridge")
frame_result.pack(pady=10, fill="both", expand=True)
root.mainloop()
