import tkinter as tk
from tkinter import messagebox,ttk

class resturantordermanagement():
    def __init__(self,root):
        self.root = root
        self.root.title("resturant management app")
        
        self.menu_items = {
            "fries meal" : 2,
            "lunch meal" : 2,
            "burger meal" : 3,
            "pizza meal" : 4,
            "chese burger" : 2.5,
            "drinks" : 1,
            "chicken wings" : 3.5,
            "salad" : 2,
            "ice cream" : 1.5,
            "coffee" : 1.2,
            "sandwich" : 2.8
        }
        
        self.exchange_rate = 120
        
        
        self.setup_background(root)
        
        frame = ttk.Frame(root)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        
        ttk.Label(frame , text="resturant order " , font=("arial" , 20 , "bold")).grid(row=0 , columnspan=4 , padx=10 , pady=10)
        
        self.menu_labels = {}
        self.menu_quantities = {}
        
        ttk.Label(frame , text="item" , font=("arial" , 12 , "bold")).grid(row=1 , column=0 , padx=10)
        ttk.Label(frame , text="price(USD)" , font=("arial" , 12 , "bold")).grid(row=1 , column=1 , padx=10)
        ttk.Label(frame , text="price(BDT)" , font=("arial" , 12 , "bold")).grid(row=1 , column=2 , padx=10)
        ttk.Label(frame , text="quantity" , font=("arial" , 12 , "bold")).grid(row=1 , column=3 , padx=10)
        
        for i , (item , price) in enumerate(self.menu_items.items() , start=2):
            bdt_price = price * self.exchange_rate
            ttk.Label(frame , text=f"{item}:" , font=("arial" , 12)).grid(row=i , column=0 , padx=10 ,pady = 5)
            ttk.Label(frame , text=f"${price:.2f}" , font=("arial" , 12)).grid(row=i , column=1 , padx=10 ,pady = 5)
            ttk.Label(frame , text=f"{bdt_price:.2f} BDT" , font=("arial" , 12)).grid(row=i , column=2 , padx=10 ,pady = 5)
            
            quantity_entry = ttk.Entry(frame , width=5 )
            quantity_entry.grid(row=i , column=3 , padx=10 ,pady = 5)
            self.menu_quantities[item] = quantity_entry
            
        order_button = ttk.Button(frame , text="place order" , command=self.place_order)
        order_button.grid(row=len(self.menu_items)+2 , columnspan=4 , pady=10 , padx = 10)
        
        clear_button = ttk.Button(frame , text="clear" , command=self.clear_order)
        clear_button.grid(row=len(self.menu_items)+3 , columnspan=2 , pady=10 , padx=10)
        
        self.total_var = tk.StringVar(value="total:  ৳0")
        total_label = ttk.Label(frame , textvariable=self.total_var , font=("arial" , 14 , "bold"))
        total_label.grid(row=len(self.menu_items)+3 , column=0 , pady=10 , columnspan=4)
        
        for entry in self.menu_quantities.values():
            entry.bind("<KeyRelease>" , self.update_total)
            
    def setup_background(self,root):
        bg_width , bg_height = 800 , 600
        canvas = tk.Canvas(root , width=bg_width , height=bg_height)
        canvas.pack()
        try:    
            original_image = tk.PhotoImage(file="Background.png")
            bankground_image = original_image.subsample(max(1, original_image.width()//bg_width) , max(1, original_image.height()//bg_height))
            canvas.create_image(0,0 , image=bankground_image , anchor=tk.NW) 
            canvas.image = bankground_image
        except Exception:
            pass   
        
    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n" 
        symbol = "৳"
        rate = self.exchange_rate
        for item , entry in  self.menu_quantities.image():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item]*rate
                cost = quantity * price
                total_cost += cost
                if quantity > 0:
                    order_summary += f"{item} : {quantity} x {symbol}{price:.0f} = {symbol}{cost:.0f}\n"
                    self.clear_order()
                    
            if total_cost > 0:
                order_summary += f"\nTotal Cost: {symbol}{total_cost:.0f}"
                messagebox.showinfo("Order Placed" , order_summary)
            else:
                messagebox.showwarning("No Items" , "Please select at least one item to place an order.")
                
    def clear_order(self):
        for entry in self.menu_quantities.values():
            entry.delete(0 , tk.END)
        self.total_var.set("total: ৳0")
        
    def update_total(self , event=None):
        total_cost = 0
        rate = self.exchange_rate
        for item , entry in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item]*rate
                cost = quantity * price
                total_cost += cost
        self.total_var.set(f"total:{total_cost:.0f}")
                    
                    
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = resturantordermanagement(root)
    root.mainloop()