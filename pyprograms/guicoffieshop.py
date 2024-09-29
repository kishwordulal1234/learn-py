import tkinter as tk
from tkinter import messagebox

# Function to handle item selection and payment
def check_item_availability():
    item = item_var.get().lower()
    user_money = 0

    if item in prices:
        price = prices[item]
        user_money = int(money_entry.get())
        if user_money == price:
            messagebox.showinfo("Payment Status", "You have paid the exact amount.")
            reset()
        elif user_money > price:
            change = user_money - price
            messagebox.showinfo("Payment Status", f"Your change is {change}. Have a good day!")
            reset()
        else:
            not_enough_money(price)
    else:
        messagebox.showerror("Error", "Sorry, that item is not available.")

# Function to handle insufficient funds
def not_enough_money(price):
    def terminate_or_repay():
        opt = option_var.get().lower()
        if opt == 'q':
            messagebox.showinfo("Thank You", "Thank you for shopping with us.")
            reset()
        elif opt == 'r':
            user_money = int(money_entry.get())
            if user_money >= price:
                if user_money > price:
                    change = user_money - price
                    messagebox.showinfo("Payment Status", f"Your change is {change}. Have a good day!")
                else:
                    messagebox.showinfo("Payment Status", "You have paid the exact amount. Enjoy!")
                reset()
            else:
                messagebox.showwarning("Insufficient Funds", "You still don't have enough money. Please try again.")
                option_var.set('')  # Reset the option variable for next input
                option_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Invalid Option", "Invalid option. Please enter 'q' or 'r'.")
    
    messagebox.showwarning("Insufficient Funds", "You don't have enough money.")
    option_frame = tk.Frame(root)
    option_frame.pack(pady=10)
    
    option_label = tk.Label(option_frame, text="Would you like to terminate the purchase or repay?")
    option_label.pack()

    tk.Label(option_frame, text="If terminate, please input 'q'. If repay, 'r'.").pack()

    option_var.set('')  # Clear previous input
    option_entry = tk.Entry(option_frame, textvariable=option_var)
    option_entry.pack()

    option_button = tk.Button(option_frame, text="Submit", command=terminate_or_repay)
    option_button.pack()

# Function to reset the application for new user
def reset():
    item_var.set('')
    money_var.set('')
    option_var.set('')
    item_entry.delete(0, tk.END)
    money_entry.delete(0, tk.END)
    if option_frame:
        option_frame.pack_forget()

# Prices of available items
prices = {
    'milk': 60,
    'tea': 25,
    'coffee': 160
}

# Initialize the main window
root = tk.Tk()
root.title("Coffee Shop")

# Welcome Label
welcome_label = tk.Label(root, text="Welcome to the coffee shop!", font=("Arial", 16))
welcome_label.pack(pady=10)

# Item Selection Frame
item_frame = tk.Frame(root)
item_frame.pack(pady=10)

item_label = tk.Label(item_frame, text="Enter the item that you would like to have:")
item_label.pack()

item_var = tk.StringVar()
item_entry = tk.Entry(item_frame, textvariable=item_var)
item_entry.pack()

# Money Entry Frame
money_frame = tk.Frame(root)
money_frame.pack(pady=10)

money_label = tk.Label(money_frame, text="Please provide the money:")
money_label.pack()

money_var = tk.StringVar()
money_entry = tk.Entry(money_frame, textvariable=money_var)
money_entry.pack()

# Option Entry Frame (initially hidden)
option_frame = None
option_var = tk.StringVar()

# Submit Button
submit_button = tk.Button(root, text="Submit", command=check_item_availability)
submit_button.pack(pady=20)

# Run the application
root.mainloop()
