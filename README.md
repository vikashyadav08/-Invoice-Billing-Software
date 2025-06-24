
🧾 Invoice & Billing Software 
A simple and professional desktop application to create PDF invoices for customers with multi-product support, tax calculation, company branding (logo & address), and direct printing functionality.

🚀 Features
✅ Add multiple products with quantity & price

✅ Automatic calculation of subtotal, tax, and grand total

✅ Generates professional PDF invoice using ReportLab

✅ Includes company logo and contact details

✅ Input and display customer name & mobile number

✅ Print invoice directly after PDF generation

✅ Clean and responsive Tkinter GUI


🧰 Tech Stack
Technology	Purpose
Python	Core language
Tkinter	GUI interface
ReportLab	PDF generation
SQLite (optional)	Invoice history (future use)
OS / subprocess	Invoice printing

📁 Project Structure

invoice_billing/
├── invoice_app.py          # Main application code
├── invoices/               # Folder where invoices are saved
└── logo.png                # Your company logo
🔧 Setup Instructions
Clone the repository or download the files

Install the required Python library:

pip install reportlab
Place your logo.png in the project folder
Recommended size: 150x150 px

Run the application:

python invoice_app.py
📄 Sample PDF Invoice Output

Vikash Tech Lab
123 Tech Street, Lucknow, UP - 226001
Phone: +91-9876543210 | Email: contact@vikashtechlab.in

INVOICE

Customer Name: Vikki 
Mobile: 999999999
Date: 24-06-2025
Tax: 18%

Product       Quantity     Price     Total
------------------------------------------
USB Drive         2       ₹500.00   ₹1000.00
Notebook          1       ₹100.00   ₹100.00

Subtotal:                      ₹1100.00
Tax (18%):                    ₹198.00
Grand Total:                  ₹1298.00

