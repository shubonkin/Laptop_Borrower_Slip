from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

# Database connection (as before)
conn = sqlite3.connect("laptop_borrower_system.db")
cursor = conn.cursor()

# GUI setup
root = Tk()
root.title("Laptop Borrower System")
root.geometry("800x600")

# Add a frame for the left-side layout
left_frame = Frame(root)
left_frame.pack(side=LEFT, padx=5, pady=5)

# Load and display the logo
try:
    logo = PhotoImage(file="Philsys.png")  # Replace with the actual path to your logo
    logo_label = Label(left_frame, image=logo)
    logo_label.pack()
except Exception as e:
    print(f"Error loading logo: {e}")
    logo_label = Label(left_frame, text="Logo Here", font=("Arial", 16), bg="lightgray", width=20, height=10)
    logo_label.pack()

# Add the main interface in the right frame
right_frame = Frame(root)
right_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

# Entry fields (place these in the right_frame as before)
frame = Frame(right_frame)
frame.pack(pady=10)

Label(frame, text="Laptop Number:").grid(row=0, column=0, padx=5, pady=5)
entry_laptop_number = Entry(frame)
entry_laptop_number.grid(row=0, column=1, padx=5, pady=5)

Label(frame, text="Serial Number:").grid(row=1, column=0, padx=5, pady=5)
entry_serial_number = Entry(frame)
entry_serial_number.grid(row=1, column=1, padx=5, pady=5)

Label(frame, text="Borrower Name:").grid(row=2, column=0, padx=5, pady=5)
entry_borrower_name = Entry(frame)
entry_borrower_name.grid(row=2, column=1, padx=5, pady=5)

Label(frame, text="Purpose:").grid(row=3, column=0, padx=5, pady=5)
entry_purpose = Entry(frame)
entry_purpose.grid(row=3, column=1, padx=5, pady=5)

Label(frame, text="Borrow Date (YYYY-MM-DD):").grid(row=4, column=0, padx=5, pady=5)
entry_borrow_date = Entry(frame)
entry_borrow_date.grid(row=4, column=1, padx=5, pady=5)

Label(frame, text="Return Date (YYYY-MM-DD):").grid(row=5, column=0, padx=5, pady=5)
entry_return_date = Entry(frame)
entry_return_date.grid(row=5, column=1, padx=5, pady=5)

Label(frame, text="Notes:").grid(row=6, column=0, padx=5, pady=5)
entry_notes = Entry(frame)
entry_notes.grid(row=6, column=1, padx=5, pady=5)

# Buttons
btn_frame = Frame(right_frame)
btn_frame.pack(pady=10)

Button(btn_frame, text="Add Borrower").grid(row=0, column=0, padx=5, pady=5)
Button(btn_frame, text="Update Status").grid(row=0, column=1, padx=5, pady=5)
Button(btn_frame, text="Delete Borrower").grid(row=0, column=2, padx=5, pady=5)
Button(btn_frame, text="Clear Fields").grid(row=0, column=3, padx=5, pady=5)

# Treeview
tree_frame = Frame(right_frame)
tree_frame.pack(pady=10)

columns = ("ID", "Laptop Number", "Serial Number", "Borrower Name", "Purpose", "Borrow Date", "Return Date", "Status", "Notes")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=10)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack()

# Run the GUI
root.mainloop()
