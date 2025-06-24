import tkinter as tk
from tkinter import ttk, messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from datetime import datetime
import os
import platform
import subprocess

# Create invoices folder if not exists
if not os.path.exists("invoices"):
    os.mkdir("invoices")

products = []

# Company Info
company_name = "Vikash Tech Lab"
company_address = "123xyz Tech Street, Noida, UP - 201307"
company_phone = "Phone: +91-9999999999"
company_email = "Email: contact@vikashtechlab.in"
logo_path = "logo.png"  # Place your logo in project folder

def add_product():
    product = entry_product.get()
    quantity = entry_quantity.get()
    price = entry_price.get()

    if not (product and quantity and price):
        messagebox.showwarning("Missing Info", "Please fill all product fields!")
        return

    try:
        quantity = int(quantity)
        price = float(price)
        total = quantity * price
        products.append((product, quantity, price, total))

        tree.insert('', 'end', values=(product, quantity, f"₹{price:.2f}", f"₹{total:.2f}"))
        entry_product.delete(0, tk.END)
        entry_quantity.delete(0, tk.END)
        entry_price.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Invalid Input", "Enter valid numbers for quantity and price.")

def generate_invoice():
    name = entry_name.get()
    mobile = entry_mobile.get()
    tax = entry_tax.get()

    if not name or not mobile or not products:
        messagebox.showwarning("Missing Data", "Please enter customer name, mobile number and at least one product.")
        return

    try:
        tax = float(tax) if tax else 0.0
        total_amount = sum([p[3] for p in products])
        tax_amount = total_amount * (tax / 100)
        grand_total = total_amount + tax_amount

        filename = f"invoices/invoice_{name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
        c = canvas.Canvas(filename)

        # Draw logo if exists
        if os.path.exists(logo_path):
            logo = ImageReader(logo_path)
            c.drawImage(logo, 50, 770, width=60, height=60)

        # Company Info
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(300, 820, company_name)
        c.setFont("Helvetica", 10)
        c.drawCentredString(300, 805, company_address)
        c.drawCentredString(300, 792, company_phone + " | " + company_email)

        # Invoice Heading
        c.setFont("Helvetica-Bold", 14)
        c.drawString(220, 770, "INVOICE")

        # Customer Info
        c.setFont("Helvetica", 12)
        c.drawString(50, 750, f"Date: {datetime.now().strftime('%d-%m-%Y')}")
        c.drawString(50, 735, f"Customer Name: {name}")
        c.drawString(50, 720, f"Mobile: {mobile}")
        c.drawString(50, 705, f"Tax: {tax}%")

        # Product Table
        c.drawString(50, 680, "Product")
        c.drawString(200, 680, "Quantity")
        c.drawString(300, 680, "Price")
        c.drawString(400, 680, "Total")

        y = 660
        for product, qty, price, total in products:
            c.drawString(50, y, product)
            c.drawString(200, y, str(qty))
            c.drawString(300, y, f"₹{price:.2f}")
            c.drawString(400, y, f"₹{total:.2f}")
            y -= 20

        # Summary
        c.drawString(50, y - 10, "-" * 100)
        c.drawString(300, y - 30, "Subtotal:")
        c.drawString(400, y - 30, f"₹{total_amount:.2f}")
        c.drawString(300, y - 50, "Tax:")
        c.drawString(400, y - 50, f"₹{tax_amount:.2f}")
        c.drawString(300, y - 70, "Grand Total:")
        c.drawString(400, y - 70, f"₹{grand_total:.2f}")

        c.save()
        messagebox.showinfo("Invoice Saved", f"Saved as:\n{filename}")

        # 🔄 Print invoice directly
        print_invoice(filename)

        clear_all()

    except ValueError:
        messagebox.showerror("Invalid Tax", "Tax must be a number.")

def print_invoice(filename):
    try:
        if platform.system() == "Windows":
            os.startfile(filename, "print")
        else:
            subprocess.run(["lp", filename])
    except Exception as e:
        messagebox.showerror("Print Error", f"Failed to print invoice:\n{str(e)}")

def clear_all():
    entry_name.delete(0, tk.END)
    entry_mobile.delete(0, tk.END)
    entry_tax.delete(0, tk.END)
    entry_product.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    tree.delete(*tree.get_children())
    products.clear()

# GUI Setup
root = tk.Tk()
root.title("Invoice & Billing Software - Vikash Tech Lab")

# Customer Info
tk.Label(root, text="Customer Name").grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_name = tk.Entry(root, width=25)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Mobile Number").grid(row=0, column=2, padx=10, pady=5, sticky='e')
entry_mobile = tk.Entry(root, width=20)
entry_mobile.grid(row=0, column=3, padx=5, pady=5)

tk.Label(root, text="Tax (%)").grid(row=0, column=4, padx=10, pady=5, sticky='e')
entry_tax = tk.Entry(root, width=10)
entry_tax.grid(row=0, column=5, padx=5, pady=5)

# Product Entry
tk.Label(root, text="Product").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_product = tk.Entry(root, width=25)
entry_product.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Quantity").grid(row=1, column=2, padx=10, pady=5, sticky='e')
entry_quantity = tk.Entry(root, width=10)
entry_quantity.grid(row=1, column=3, padx=5, pady=5)

tk.Label(root, text="Price (₹)").grid(row=1, column=4, padx=10, pady=5, sticky='e')
entry_price = tk.Entry(root, width=10)
entry_price.grid(row=1, column=5, padx=5, pady=5)

tk.Button(root, text="Add Product", command=add_product, bg='blue', fg='white').grid(row=1, column=6, padx=10)

# Product Table
columns = ('Product', 'Qty', 'Price', 'Total')
tree = ttk.Treeview(root, columns=columns, show='headings', height=8)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor='center', width=100)
tree.grid(row=2, column=0, columnspan=7, padx=10, pady=10)

tk.Button(root, text="Generate Invoice", command=generate_invoice, bg='green', fg='white', height=2).grid(row=3, columnspan=7, pady=20)

root.mainloop()



